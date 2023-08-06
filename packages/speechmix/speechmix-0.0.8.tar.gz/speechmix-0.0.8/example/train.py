import argparse
import sys

import asrp

import speechmix
from datasets import load_dataset, Audio
import torch
from transformers import Wav2Vec2Processor, Trainer, TrainingArguments
from typing import Dict, List, Union, Optional
from dataclasses import dataclass


def main(arg=None):
    def prepare_dataset(batch):
        audio = batch["audio"]
        batch["input_values"] = model.processor(audio["array"], sampling_rate=16_000).input_values[0]
        batch["input_ids"] = batch["input_values"]
        batch["labels"] = model.tokenizer(batch["sentence"]).input_ids
        return batch

    def compute_metrics(pred):
        pred_ids = pred.predictions
        pred_ids = [i[i != -100] for i in pred_ids]

        pred_str = model.tokenizer.batch_decode(pred_ids)
        # we do not want to group tokens when computing the metrics
        label_ids = pred.label_ids
        label_ids = [i[i != -100] for i in label_ids]
        label_str = model.tokenizer.batch_decode(label_ids, group_tokens=False)

        cer = asrp.cer(label_str, pred_str)

        return {"cer": cer}

    @dataclass
    class DataCollatorWithPadding:
        processor: Wav2Vec2Processor
        tokenizer: Wav2Vec2Processor
        padding: Union[bool, str] = True
        max_length: Optional[int] = None
        max_length_labels: Optional[int] = None
        pad_to_multiple_of: Optional[int] = None
        pad_to_multiple_of_labels: Optional[int] = None

        def __call__(self, features: List[Dict[str, Union[List[int], torch.Tensor]]]) -> Dict[str, torch.Tensor]:
            # split inputs and labels since they have to be of different lenghts and need
            # different padding methods
            input_features = [{"input_values": feature["input_values"]} for feature in features]
            label_features = [{"input_ids": feature["labels"]} for feature in features]

            batch = self.processor.pad(
                input_features,
                padding=self.padding,
                max_length=self.max_length,
                pad_to_multiple_of=self.pad_to_multiple_of,
                return_tensors="pt",
            )

            labels_batch = self.tokenizer.pad(
                label_features,
                padding=self.padding,
                max_length=self.max_length_labels,
                pad_to_multiple_of=self.pad_to_multiple_of_labels,
                return_tensors="pt",
            )

            # replace padding with -100 to ignore loss correctly
            labels = labels_batch["input_ids"].masked_fill(labels_batch.attention_mask.ne(1), -100)

            batch["labels"] = labels
            batch.pop('attention_mask', None)
            return batch

    def parse_args(args):
        parser = argparse.ArgumentParser()
        parser.add_argument("--speech_model_config", type=str)
        parser.add_argument("--nlp_model_config", type=str)
        parser.add_argument("--SpeechMixEED", action='store_true')
        parser.add_argument("--SpeechMixED", action='store_true')
        parser.add_argument("--ftl", action='store_true')
        parser.add_argument("--lna", action='store_true')
        parser.add_argument("--fne", action='store_true')

        input_arg, model_arg = parser.parse_known_args(args)
        input_arg = {k: v for k, v in vars(input_arg).items() if v is not None}
        other_arg = {k.replace("--", ""): v for k, v in zip(model_arg[:-1:2], model_arg[1::2])}
        return input_arg, other_arg

    input_arg, other_arg = parse_args(sys.argv[1:]) if arg is None else parse_args(arg)
    print(input_arg)

    if input_arg['SpeechMixEED']:
        model_type = "SpeechMixEED"
        if input_arg['lna']:
            model_type += "_lna"
        elif input_arg['fne']:
            model_type += "_fne"
        model = speechmix.SpeechMixEED(input_arg['speech_model_config'], input_arg['nlp_model_config'],
                                       lna=input_arg['lna'], fne=input_arg['fne'])
    else:
        model_type = "SpeechMixED"
        if input_arg['ftl']:
            model_type += "_ftl"
        model = speechmix.SpeechMixED(input_arg['speech_model_config'], input_arg['nlp_model_config'],
                                      ftl=input_arg['ftl'])

    train_ds = load_dataset("common_voice", "zh-TW", split='train')
    valid_ds = load_dataset("common_voice", "zh-TW", split='test')

    train_ds = train_ds.cast_column("audio", Audio(sampling_rate=16_000))
    valid_ds = valid_ds.cast_column("audio", Audio(sampling_rate=16_000))

    train_ds = train_ds.map(prepare_dataset, num_proc=1)
    valid_ds = valid_ds.map(prepare_dataset, num_proc=1)

    data_collator = DataCollatorWithPadding(processor=model.processor, tokenizer=model.tokenizer, padding=True)

    training_args = TrainingArguments(
        output_dir=f"./{input_arg['speech_model_config']}_{input_arg['nlp_model_config']}_{model_type}",
        per_device_train_batch_size=3,
        per_device_eval_batch_size=3,
        gradient_accumulation_steps=10,
        eval_accumulation_steps=2,
        evaluation_strategy="steps",
        group_by_length=True,
        num_train_epochs=30,
        fp16=True,
        save_steps=400,
        eval_steps=400,
        logging_steps=400,
        learning_rate=3e-4,
        warmup_steps=500,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        compute_metrics=compute_metrics,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
        data_collator=data_collator,
        tokenizer=model.tokenizer
    )

    trainer.train()
    trainer.predict(train_ds)


if __name__ == "__main__":
    main()

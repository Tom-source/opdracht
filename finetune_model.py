#pip install transformers datasets in terminal
#pip install torch
#pip install accelerate


import logging
import mlflow
import mlflow.pytorch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up MLflow
mlflow.set_experiment("AI Act Fine-Tuning Experiment")

# Load the dataset
logger.info("Loading dataset...")
dataset = load_dataset('csv', data_files={'train': 'clean_ai_act_training_data.csv'})

# Load the tokenizer and model
logger.info("Loading tokenizer and model...")
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Set the padding token to be the end of sentence token
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained('gpt2')

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding='max_length', max_length=512)

logger.info("Tokenizing dataset...")
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./results',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    prediction_loss_only=True,
)

# Initialize the Trainer
logger.info("Initializing trainer...")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    data_collator=data_collator,
)

# Fine-tune the model
logger.info("Starting training...")

with mlflow.start_run() as run:
    # Log parameters
    mlflow.log_param("num_train_epochs", training_args.num_train_epochs)
    mlflow.log_param("per_device_train_batch_size", training_args.per_device_train_batch_size)

    # Train the model
    trainer.train()

    # Log the trained model
    mlflow.pytorch.log_model(model, "model")

    # Log metrics
    metrics = trainer.evaluate()
    for key, value in metrics.items():
        mlflow.log_metric(key, value)

# Save the model locally
logger.info("Saving model...")
model.save_pretrained('fine_tuned_gpt2')
tokenizer.save_pretrained('fine_tuned_gpt2')

logger.info("Training completed and model saved.")

#run once the python finetune_model.py

#to see mlflow load mlflow ui




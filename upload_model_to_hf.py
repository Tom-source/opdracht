import os
from huggingface_hub import HfApi, HfFolder, upload_folder

# Set the Hugging Face API token
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

# Save the token to the Hugging Face folder
HfFolder.save_token(os.environ['HUGGINGFACEHUB_API_TOKEN'])

# Initialize the HfApi
api = HfApi()

# Repository details
repo_name = 'fine_tuned_gpt2'  # Change this to your desired repository name
username = 'TomW9'  # Your Hugging Face username

# Path to the fine-tuned model directory
model_dir = 'fine_tuned_gpt2'

# Create the repository on Hugging Face if it doesn't exist
api.create_repo(repo_id=f'{username}/{repo_name}', exist_ok=True)

# Upload the folder to the repository
upload_folder(
    folder_path=model_dir,
    path_in_repo='.',
    repo_id=f'{username}/{repo_name}',
    token=os.environ['HUGGINGFACEHUB_API_TOKEN']
)

print(f'Model successfully uploaded to https://huggingface.co/{username}/{repo_name}')

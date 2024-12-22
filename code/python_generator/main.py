#!/bin/python3
import os
import yaml
import time
import argparse

from api.OpenAIWrapper import text_request as openai_text_request
from utilities.File import File, MergedFiles
from utilities.LoadSecrets import LoadSecrets
from utilities.Prompt import PromptGenerator

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate cognitive warmup.')
parser.add_argument('source_dir', type=str, help='Path to the input directory.')
parser.add_argument('output_dir', type=str, help='Path to the output directory.')
parser.add_argument('--config_file', type=str, default="../../config/tasking.yaml", help='Path to the config file.')
args = parser.parse_args()

# Load source files
myfiles = []
for root, dirs, files in os.walk(args.source_dir):
    for file in files:
        myfiles.append(File(os.path.join(root, file)))
merged_files = MergedFiles(myfiles)
print(merged_files.content)

# Load config file
with open(args.config_file, 'r') as file:
    config = yaml.safe_load(file)
    config_tasks = config.keys()

# Set up OpenAPI Wrapper
secrets = LoadSecrets(['openai'])

# Generate content
for task in config_tasks:
    if config[task]['enabled'] == False:
        continue
    role = config[task]['role'] if 'role' in config[task] else "system"
    role_content = config[task]['role_content'] if 'role_content' in config[task] else "You are a helpful assistant."
    model = config[task]['model'] if 'model' in config[task] else "gpt-4o-mini"
    print(f'Generating content for task: "{task}"')

    prompt = PromptGenerator("combine_with_context", config[task]['command'], merged_files.content).get_prompt()
    print("PROMPT: ", prompt)
    response = openai_text_request(api_key=secrets.openai, question_content=prompt, model=model, role_content=role_content)
    print("RESPONSE: ", response)
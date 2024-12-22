#!/bin/python3
import os
import yaml
import argparse

from api.OpenAI import OpenAI
from utilities.File import File, MergedFiles
from utilities.LoadSecrets import LoadSecrets
from utilities.Prompt import Prompt

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate cognitive warmup.')
parser.add_argument('source_dir', type=str, help='Path to the input directory.')
parser.add_argument('output_dir', type=str, help='Path to the output directory.')
parser.add_argument('--config_file', type=str, default="../../config/tasking.yaml", help='Path to the config file.')
args = parser.parse_args()

# Load config file
with open(args.config_file, 'r') as file:
    config = yaml.safe_load(file)
    config_tasks = config.keys()

# Load source files
myfiles = []
for root, dirs, files in os.walk(args.source_dir):
    for file in files:
        myfiles.append(File(os.path.join(root, file)))
merged_files = MergedFiles(myfiles)
print(merged_files.content)

# Set up OpenAPI Wrapper
secrets = LoadSecrets(['openai'])
OpenAI_Controller = OpenAI(secrets.openai)

# Generate content
for task in config_tasks:
    if config[task]['enabled'] == False:
        continue
    role = config[task]['role'] if 'role' in config[task] else "system"
    role_content = config[task]['role_content'] if 'role_content' in config[task] else "You are a helpful assistant."
    model = config[task]['model'] if 'model' in config[task] else "gpt-4o-mini"
    print(f'Generating content for task: "{task}"')

    #response = OpenAI_Controller.text_request(merged_files.content, config[task])
    # Error handling
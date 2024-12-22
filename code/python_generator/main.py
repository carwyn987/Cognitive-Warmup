#!/bin/python3
import os
import yaml
import argparse

from utilities.File import File, MergedFiles
from utilities.LoadSecrets import LoadSecrets
from api.OpenAI import OpenAI

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


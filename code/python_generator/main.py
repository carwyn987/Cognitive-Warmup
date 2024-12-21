#!/bin/python3
import os
import argparse

from utilities.File import File
from utilities.LoadSecrets import LoadSecrets
from api.OpenAI import OpenAI

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate cognitive warmup.')
parser.add_argument('source_dir', type=str, help='Path to the input directory.')
parser.add_argument('output_dir', type=str, help='Path to the output directory.')
args = parser.parse_args()

# Load files
myfiles = []
for root, dirs, files in os.walk(args.source_dir):
    for file in files:
        myfiles.append(File(os.path.join(root, file)))

print(myfiles)

# Set up OpenAPI Wrapper
secrets = LoadSecrets(['openai'])
OpenAI_Controller = OpenAI(secrets.openai)


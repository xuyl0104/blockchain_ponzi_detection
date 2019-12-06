import sys
import os
import shutil
import subprocess
import urllib.request
from datacollector import DataCollector
from get_contract_opcode import OpcodeColector
from features_of_all_contracts import ExtractFeatureOfAllContract
from train import Model

# OPTION 1: download all the dataset automatically and train
# create directories fo data storage
shutil.rmtree('./data/transactions/', ignore_errors=True)
shutil.rmtree('./data/internal_transactions/', ignore_errors=True)
shutil.rmtree('./data/contracts/', ignore_errors=True)
shutil.rmtree('./data/transactions/ponzi/', ignore_errors=True)
shutil.rmtree('./data/transactions/nonponzi/', ignore_errors=True)
shutil.rmtree('./data/internal_transactions/ponzi/', ignore_errors=True)
shutil.rmtree('./data/internal_transactions/nonponzi/', ignore_errors=True)
shutil.rmtree('./data/contracts/ponzi/', ignore_errors=True)
shutil.rmtree('./data/contracts/nonponzi/', ignore_errors=True)

os.mkdir('./data/transactions/')
os.mkdir('./data/internal_transactions/')
os.mkdir('./data/contracts/')
os.mkdir('./data/transactions/ponzi/')
os.mkdir('./data/transactions/nonponzi/')
os.mkdir('./data/internal_transactions/ponzi/')
os.mkdir('./data/internal_transactions/nonponzi/')
os.mkdir('./data/contracts/ponzi/')
os.mkdir('./data/contracts/nonponzi/')

# important files
ponzi_contract_csv = './data/ponziContracts.csv'
nonponzi_contract_csv = './data/non_ponziContracts.csv'
opcode_csv = './data/Opcodes.csv'

# Download transaction data
print("Downloading Opcode.csv file...(over 4 GB)")
subprocess.call(['./download_opcodes.sh'])
datacollector = DataCollector(ponzi_contract_csv, nonponzi_contract_csv)

# download opcode data
opcode_collector = OpcodeColector(
    ponzi_contract_csv, nonponzi_contract_csv, opcode_csv)

# OPTION 2: gdownload the dataset from this link; unzipped and place the data folder in the root folder
# Link: https://drive.google.com/open?id=1izaOs4Mlp6dxdRMtRYQeUfkDhlqLf4Z6

# Extract features
extract_feature_of_all_contract = ExtractFeatureOfAllContract()

# Train models
model_performance = Model()

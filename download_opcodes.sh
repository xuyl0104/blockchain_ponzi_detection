#!/usr/bin/env bash

# download dataset
cd data

wget http://ibasetest.inpluslab.com/scamedb/contract_download/static/file/_Opcodes.csv

mv _Opcodes.csv Opcodes.csv

cd ..
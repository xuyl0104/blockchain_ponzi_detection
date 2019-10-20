import os
import sys
import urllib.request
import json
import csv

class DataCollector:
    def __init__(self, ponzi_filename, non_ponzi_filename):
        self.ponzi_filename = ponzi_filename
        self.non_ponzi_filename = non_ponzi_filename
        self.ponzi_contract_list = []
        self.non_ponzi_contract_list = []
        self.baseURL = "http://ibasetest.inpluslab.com/scamedb/contract_download/static/file/Txs/ContractNormalTx/"

        self.get_ponzi_contract_list()
        self.get_nonponzi_contract_list()

        self.queryPonziUrlAndSaveToFiles()
        self.queryNonPonziUrlAndSaveToFiles()

    def get_ponzi_contract_list(self):
        with open(self.ponzi_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:  # line# = 0 -> header
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # print(f'\t{row[0]}, {row[1]}, {row[2]}.')
                    self.ponzi_contract_list.append(row[1])
                    line_count += 1

            # print(f'Processed {line_count} lines.')
            # print(self.ponzi_contract_list)

    def get_nonponzi_contract_list(self):
        with open(self.non_ponzi_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:  # line# = 0 -> header
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # print(f'\t{row[0]}, {row[1]}, {row[2]}.')
                    self.non_ponzi_contract_list.append(row[1])
                    line_count += 1

            # print(f'Processed {line_count} lines.')
            # print(self.ponzi_contract_list)

    def readUrlGetJson(self, contractAddress):
        contractUrl = self.baseURL + contractAddress + ".json"
        print(contractUrl)
        results = []
        with urllib.request.urlopen(contractUrl) as url:
            data = json.loads(url.read().decode())
            return data['result']


    def queryPonziUrlAndSaveToFiles(self):
        counter = 0
        for contratAddress in self.ponzi_contract_list:
            fileNameToSave = './data/transactions/ponzi/' + contratAddress + '.csv'
            if not os.path.exists(fileNameToSave):
                with open(fileNameToSave, 'w') as f:
                    pass

            results = self.readUrlGetJson(contratAddress)
            fieldnames = ['blockNumber', 'blockHash', 'timeStamp', 'hash', 'nonce', 'transactionIndex', 'from', 'to', 'value', 'gas', 'gasPrice', 'input', 'contractAddress', 'cumulativeGasUsed', 'gasUsed', 'confirmations', 'isError']
            with open(fileNameToSave, mode='w+') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    result['input'] = ''
                    print(result)
                    writer.writerow(result)

    def queryNonPonziUrlAndSaveToFiles(self):
        counter = 0
        for contratAddress in self.non_ponzi_contract_list:
            fileNameToSave = './data/transactions/nonponzi/' + contratAddress + '.csv'
            if not os.path.exists(fileNameToSave):
                with open(fileNameToSave, 'w') as f:
                    pass

            results = self.readUrlGetJson(contratAddress)
            fieldnames = ['blockNumber', 'blockHash', 'timeStamp', 'hash', 'nonce', 'transactionIndex', 'from', 'to', 'value', 'gas', 'gasPrice', 'input', 'contractAddress', 'cumulativeGasUsed', 'gasUsed', 'confirmations', 'isError']
            with open(fileNameToSave, mode='w+') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    result['input'] = ''
                    print(result)
                    writer.writerow(result)

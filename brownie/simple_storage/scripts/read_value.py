from brownie import accounts,config,SimpleStorage,network

def read_contract():
    # -1表示最新的合約
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()
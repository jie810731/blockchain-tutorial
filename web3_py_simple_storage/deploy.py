from solcx import compile_standard,install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol","r") as file:
    simple_storage_file = file.read()

install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)


with open("compiled/compiled_code.json","w") as file:
    json.dump(compiled_sol,file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

w3 = Web3(Web3.HTTPProvider("http://ganache:8545"))
chain_id = w3.eth.chain_id
my_address = "0x1bb9b9F3AA53b6614E1aF09C093d8B2C795EF173"
private_key = "0xd1766b604614a079f48f5390e26be9f4487802d97d83d3699a9ed07039d53ff0"

SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction({
    "chainId":chain_id,
    "gasPrice": w3.eth.gas_price,
    "from":my_address,
    "nonce":nonce
})

signed_txn = w3.eth.account.sign_transaction(transaction,private_key=private_key)
print(signed_txn)
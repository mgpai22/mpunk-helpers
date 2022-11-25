import json
import math

from dotenv import load_dotenv
import os
load_dotenv()
import requests
import web3
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://na.yakuzanode.io/02aba65f64449afdc75ea2fb3e08df9ab6d25bb1/"))
web3 = w3

my_wallet = "0x18ed95e4039ebcfE720a870Ede6E02789BBa427b"

balance = w3.eth.getBalance(my_wallet)
balance = w3.fromWei(balance, "ether")

nonce = requests.get("https://mpunkspool.com/latest.txt").json()['nonce']
nonce = int(nonce, 16)
contract = "0x595A8974C1473717c4B5D456350Cd594d9bdA687"
print(nonce)

abi = open('abi', 'r').read().replace('\n', '')

mpunk_contract = w3.eth.contract(address=contract, abi=abi)
block = web3.eth.get_block('latest')
next_gas_price = math.ceil(block.get('baseFeePerGas') * 1.251)
print(web3.fromWei(next_gas_price, 'gwei'))
print(web3.eth.get_transaction_count(my_wallet))
txn = mpunk_contract.functions.mint(
    nonce, 0
).buildTransaction({
    'from': my_wallet,
    'gasPrice': next_gas_price,
    'nonce': web3.eth.get_transaction_count(my_wallet),
})

signed_txn = web3.eth.account.sign_transaction(txn, private_key="0x" + os.getenv("PRIVATE_KEY"))
print(signed_txn)
# tx = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
#
# print(f"Sent" + web3.toHex(tx))


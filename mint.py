import math
import os
import requests
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()


def mint():
    web3 = Web3(Web3.HTTPProvider(os.getenv("NODE")))

    my_wallet = os.getenv("ADDRESS")

    balance = web3.eth.getBalance(my_wallet)
    balance = web3.fromWei(balance, "ether")

    nonce = requests.get("https://mpunkspool.com/latest.txt").json()['nonce']
    nonce = int(nonce, 16)
    contract = "0x595A8974C1473717c4B5D456350Cd594d9bdA687"
    print("nonce:", nonce)

    abi = open('abi', 'r').read().replace('\n', '')

    mpunk_contract = web3.eth.contract(address=contract, abi=abi)
    block = web3.eth.get_block('latest')
    next_gas_price = math.ceil(block.get('baseFeePerGas') * 1.251)
    print("gas price:", web3.fromWei(next_gas_price, 'gwei'))
    txn = mpunk_contract.functions.mint(
        nonce, 0
    ).buildTransaction({
        'from': my_wallet,
        'gasPrice': next_gas_price,
        'nonce': web3.eth.get_transaction_count(my_wallet),
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key="0x" + os.getenv("PRIVATE_KEY"))
    print(signed_txn)
    tx = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f"Sent: " + web3.toHex(tx))
    return web3.toHex(tx)

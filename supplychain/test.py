from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/0f27e0b2439f4a9887f2dc785011e634'))

print(w3.is_connected())
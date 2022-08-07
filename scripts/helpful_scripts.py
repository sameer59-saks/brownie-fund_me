from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000

#price function has 8 decimals
#DECIMALS = 8
#STARTING_PRICE = 200000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet","mainnet-fork","mainnet-fork-dev"]

LOCAL_BLOCKCHAIN_ENVIRONMENTS= ["development","ganache-local"]

def get_account():
    #if network.show_active() == "development":
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active netowrk is  {network.show_active()}")
    print("deployming mocks")
    if len(MockV3Aggregator) <= 0:
        #MockV3Aggregator.deploy(18, Web3.toWei(2000,"ether"), {"from":get_account()})
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from":get_account()})
    print("Mocks  Deployed!")
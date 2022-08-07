from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import ( 
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import os
from web3  import Web3


def deploy_fund_me():
    # account  = get_account()
   # fund_me = FundMe.deploy({"from":account}, publish_source=True)
   # print(f"Contract deployed to {fund_me.address}")
   
    account=get_account()
        #pass price feed address to the fund me contract
        
        #if we are on persistance n/w linke rinkeby, use the associated address
        #otherwise deploy mocks
        
    #if network.show_active()!= "development":
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        #call mock from helpful scripts
        deploy_mocks()
        #  move  the code in double ## to separate section in helpful scripts
        # #print(f"The active netowork  is {network.show_active()}")
        ##print("Deploying  mocks")
        #deploy_mocks()
        
        #m ock_aggregator=MockV3Aggregator.deploy(18,2000000000000000000, {"from": account})
        #if len(MockV3Aggregator) <=0:
         #   mock_aggregator = MockV3Aggregator.deploy(18,  Web3.toWei(2000, "ether"), {"from": account})
        
        #price_feed_address = mock_aggregator.address
                 #use most recently deploy mock v3 aggregator
        print("Mocks Deploying")
        price_feed_address = MockV3Aggregator[-1].address
        
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        #verifying the deployment from config
        publish_source=config["networks"][network.show_active()].get("verify"),
        #publish_source=True,
    )
    print(f"contract deployed to {fund_me.address}")
    #for test to have the fundme contract
    return fund_me
    
    
def main():
    deploy_fund_me()
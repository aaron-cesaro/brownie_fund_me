from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)


def deploy_fund_me():
    account = get_account()
    # pass contructor parameters along with deploy paramenters

    # if we are in a persistent network like Rinkeby, use associated address
    print(f"Active network is {network.show_active()}")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    # otherwise, deploy mocks
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deploy to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()

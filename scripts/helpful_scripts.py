from typing import ForwardRef
from brownie import accounts, config, network, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks....")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks deployed!")

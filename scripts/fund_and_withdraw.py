from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() + 100
    print(f"entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"Account {account}")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"withdraw to {account}...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

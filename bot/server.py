from collections import defaultdict
from datetime import datetime

wallets = defaultdict(lambda: {"balance": 0.0, "transactions": []})

def get_balance(user_id):
    return wallets[user_id]["balance"]

def fund_wallet(user_id, amount):
    wallets[user_id]["balance"] += amount
    wallets[user_id]["transactions"].append(
        {"type": "fund", "amount": amount, "time": str(datetime.now())}
    )

def withdraw(user_id, amount):
    if wallets[user_id]["balance"] >= amount:
        wallets[user_id]["balance"] -= amount
        wallets[user_id]["transactions"].append(
            {"type": "withdraw", "amount": amount, "time": str(datetime.now())}
        )
        return True
    return False

def get_transactions(user_id):
    return wallets[user_id]["transactions"][-5:]

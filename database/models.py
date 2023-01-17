from datetime import datetime
from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    tg_ID = Required(str, unique=True)
    nick = Optional(str)
    create_date = Optional(str)
    wallet = Required('Wallet')
    sended_transactions = Set('Transaction', reverse='sender')
    recelved_transactions = Set('Transaction', reverse='user')


class Wallet(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Optional(User)
    balance = Required(float, default="0.0")
    private_key = Required(str, unique=True)
    address = Required(str, unique=True)
    transactions = Set('Transaction', reverse='wallet')
    received_transactions = Set('Transaction', reverse='receiver_wallet')


class Transaction(db.Entity):
    id = PrimaryKey(int, auto=True)
    sender = Optional(User, reverse='sended_transactions')
    wallet = Required(Wallet, reverse='transactions')
    user = Optional(User, reverse='recelved_transactions')
    receiver_wallet = Optional(Wallet, reverse='received_transactions')
    amount_btc_with_fee = Optional(float)
    amount_btc_without_fee = Required(float)
    fee = Required(float)
    date_of_transaction = Required(datetime)
    tx_hash = Required(str, unique=True)
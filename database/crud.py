import datetime

import config
import pydantic_models
import models
import bit


wallet = bit.PrivateKeyTestnet(config.testnet_wallet)
print(wallet.get_balance())
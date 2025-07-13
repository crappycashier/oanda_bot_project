from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
import os
from dotenv import load_dotenv

load_dotenv()

api = API(access_token=os.getenv("OANDA_API_KEY"))

r = accounts.AccountDetails(accountID=os.getenv("OANDA_ACCOUNT_ID"))
api.request(r)

print(r.response)
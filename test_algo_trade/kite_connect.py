from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

# Get from .env
api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")
access_token = os.getenv("KITE_ACCESS_TOKEN")


# Setup Kite Connect
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

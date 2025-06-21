from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")
request_token = os.getenv("KITE_REQUEST_TOKEN")

kite = KiteConnect(api_key=api_key)

data = kite.generate_session(request_token, api_secret=api_secret)
access_token = data["access_token"]

print("Access token:", access_token)
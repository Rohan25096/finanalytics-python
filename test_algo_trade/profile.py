import pandas as pd
from kite_connect import kite


holdings = kite.holdings()
df_holdings = pd.DataFrame(holdings)
print(df_holdings[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'pnl']].to_string(index=False))

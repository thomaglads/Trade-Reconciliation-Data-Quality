
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Configuration ---
NUM_TRADES = 100
START_DATE = datetime(2025, 8, 1)
TICKERS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'JPM', 'V', 'WMT', 'JNJ']

# --- Generate Base Data (The "Golden Source") ---
def create_base_trades():
    data = {
        'TradeID': range(1, NUM_TRADES + 1),
        'Ticker': np.random.choice(TICKERS, NUM_TRADES),
        'TradeDate': [START_DATE + timedelta(days=np.random.randint(0, 20)) for _ in range(NUM_TRADES)],
        'Quantity': np.random.randint(100, 5000, NUM_TRADES) * np.random.choice([-1, 1], NUM_TRADES),
        'Price': np.round(np.random.uniform(150.0, 500.0, NUM_TRADES), 2)
    }
    df = pd.DataFrame(data)
    df['SettlementDate'] = df['TradeDate'] + timedelta(days=2) # T+2 Settlement
    df['TradeValue'] = df['Quantity'] * df['Price']
    return df

base_trades = create_base_trades()

# --- Create Front-Office System Data ---
front_office = base_trades.copy()
front_office.rename(columns={'TradeID': 'trade_id', 'Ticker': 'ticker', 'TradeDate': 'trade_date', 'Quantity': 'quantity', 'Price': 'price', 'SettlementDate': 'settlement_date', 'TradeValue': 'trade_value'}, inplace=True)

# Introduce discrepancies:
# 1. Drop 5 random trades
front_office.drop(front_office.sample(5).index, inplace=True)
# 2. Modify quantity for 3 trades
for idx in front_office.sample(3).index:
    front_office.loc[idx, 'quantity'] *= 1.1 
# 3. Add 2 new trades that won't be in the back office
new_fo_trades_data = {
    'trade_id': [101, 102],
    'ticker': ['DIS', 'PFE'],
    'trade_date': [START_DATE + timedelta(days=5), START_DATE + timedelta(days=6)],
    'quantity': [1000, -2500],
    'price': [105.50, 45.20],
}
new_fo_trades_df = pd.DataFrame(new_fo_trades_data)
new_fo_trades_df['settlement_date'] = new_fo_trades_df['trade_date'] + timedelta(days=2)
new_fo_trades_df['trade_value'] = new_fo_trades_df['quantity'] * new_fo_trades_df['price']

front_office = pd.concat([front_office, new_fo_trades_df], ignore_index=True)


# --- Create Back-Office System Data ---
back_office = base_trades.copy()
back_office.rename(columns={'TradeID': 'TransactionReference', 'Ticker': 'SecurityID', 'TradeDate': 'ValueDate', 'Quantity': 'Units', 'Price': 'ExecutionPrice', 'SettlementDate': 'ExpectedSettlement', 'TradeValue': 'GrossAmount'}, inplace=True)

# Introduce discrepancies:
# 1. Drop 4 different random trades
back_office.drop(back_office.sample(4).index, inplace=True)
# 2. Modify settlement date for 3 trades (T+3)
for idx in back_office.sample(3).index:
    back_office.loc[idx, 'ExpectedSettlement'] += timedelta(days=1)
# 3. Add 3 new trades that weren't in the front office (e.g., corporate actions)
new_bo_trades_data = {
    'TransactionReference': [201, 202, 203],
    'SecurityID': ['GOOGL', 'TSLA', 'MSFT'],
    'ValueDate': [START_DATE + timedelta(days=8), START_DATE + timedelta(days=9), START_DATE + timedelta(days=10)],
    'Units': [50, -100, 200],
    'ExecutionPrice': [2800.00, 750.00, 300.00],
}
new_bo_trades_df = pd.DataFrame(new_bo_trades_data)
new_bo_trades_df['ExpectedSettlement'] = new_bo_trades_df['ValueDate'] + timedelta(days=2)
new_bo_trades_df['GrossAmount'] = new_bo_trades_df['Units'] * new_bo_trades_df['ExecutionPrice']

back_office = pd.concat([back_office, new_bo_trades_df], ignore_index=True)


# --- Save to CSV ---
front_office.to_csv('front_office_trades.csv', index=False)
back_office.to_csv('back_office_trades.csv', index=False)

print("Successfully generated 'front_office_trades.csv' and 'back_office_trades.csv'")

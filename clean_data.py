import pandas as pd
calls = pd.read_csv("option_data/AAPL_call_options_Jul 11, 2025.csv")

def clean_data(df):

    float_cols = ['strike', 'last_price', 'bid', 'ask', 'change', 'volume', 'open_interest', 'implied_volatility']
    pct_cols = ['pct_change', 'implied_volatility']
    datetime = ['expiry', 'last_trade_date_(edt)']

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace('%', 'pct')
        .str.replace(' ', '_')
        .str.replace('.', '')
    )
    
    for col in pct_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('%', '', regex=False)
                .astype(float)
            ) / 100 

    for col in datetime:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    
    for col in float_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('-', '0', regex=False)
                .astype(float)
            )

    return df

if __name__ == "__main__":
    df_clean = clean_data(calls)
    df_clean.to_csv(f"AAPL_calls_clean.csv", index=False)

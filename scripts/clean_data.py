import pandas as pd
import os

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
    raw_folder = "raw"
    clean_folder = "clean"
    os.makedirs(clean_folder, exist_ok=True)

    for filename in os.listdir(raw_folder):
        if filename.endswith(".csv"):
            raw_filepath = os.path.join(raw_folder, filename)

            try:
                df_raw = pd.read_csv(raw_filepath)
                df_clean = clean_data(df_raw)
                expiry = df_clean['expiry'].iloc[0].strftime('%Y-%m-%d')

                #Change name for option type
                save_filename = f"[CLEAN]_AAPL__{expiry}.csv"
                save_path = os.path.join(clean_folder, save_filename)
                df_clean.to_csv(save_path, index=False)
                print(f"file saved: {save_filename}")

            except Exception as e:
                print(f"failed {filename}: {e}")  



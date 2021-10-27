def fix_df_coingecko(df):
    import pandas as pd
    df["Dates"] = df["prices"]
    df["prices"] = df["prices"].apply(lambda x: x[1])
    df["market_caps"] = df["market_caps"].apply(lambda x: x[1])
    df["total_volumes"] = df["total_volumes"].apply(lambda x: x[1])
    df["Dates"] = df["Dates"].apply(lambda x: x[0])
    df["Dates"] = pd.to_datetime(df["Dates"], unit='ms')


def trp(l,n):
    return l[:n] + [None] * (n-len(l))
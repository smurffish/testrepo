import pandas as pd
import yfinance as yf
import math as m

def fetch(symbol):
    global df
    symbol = symbol.upper()
    df = yf.download(symbol, period='1y')
    df.columns = df.columns.get_level_values(0)
    df[['Volume']] = df[['Volume']] / 1000000
    df[['Volume']] = round(df[['Volume']], 2)
    df.rename(columns={'Volume': 'Vol'}, inplace=True)
    df[['Close']] = round(df[['Close']], 2)
    df[['High']] = round(df[['High']], 2)
    df[['Low']] = round(df[['Low']], 2)
    df[['Open']] = round(df[['Open']], 2)
    df.drop('Adj Close', axis=1, inplace=True)
    print(df)
    uptrend()
    year()
def uptrend():
    global trend
    shortTrend = df.iloc[-1]['Close'] > df.iloc[-10]['Close']
    longTrend = df.iloc[-10]['Close'] > df.iloc[-50]['Close']
    trend = shortTrend and longTrend
    if trend:
        print("There is an uptrend")
    else:
        print("There is not an uptrend")

def year():
    global profit
    profit = round((df.iloc[-1]['Close'] / df.iloc[0]['Close'] - 1) * 100)
    print("Profits since last year: " + str(profit) + "%")

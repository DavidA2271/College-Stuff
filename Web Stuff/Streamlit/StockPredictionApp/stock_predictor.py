from datetime import date
import yfinance as yf
import streamlit as st
from prophet import Prophet


class predictor:
    def __init__(_self, start, stock, years) -> None:
        _self.start = start
        _self.today = date.today().strftime("%Y-%m-%d")
        _self.selected_stock = stock
        _self.period = years * 365
    
    @st.cache_data
    def load_data(_self):
        data = yf.download(_self.selected_stock, _self.start, _self.today)
        data.reset_index(inplace=True)
        return data
    
    def predict(_self, data):
        df_train = data[['Date','Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=_self.period)
        forecast = m.predict(future)
        return (m, forecast)

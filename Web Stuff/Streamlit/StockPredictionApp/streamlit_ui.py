import streamlit as st
from plotly import graph_objs as go
from prophet.plot import plot_plotly


class ui:
    def __init__(self) -> None:
        st.title('Stock Forecast App')
    
    def setup_stock_selections(self, stocks):
        self.selected_stock = st.selectbox('Select dataset for prediction', stocks)

    def setup_prediction_years(self, min_years, max_years):
        self.n_years = st.slider('Years of prediction:', min_years, max_years)

    def write_raw_data(self, data):
        st.subheader('Raw data')
        st.write(data.tail())

    def plot_raw_data(self, data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    
    def plot_forecast(self, m, forecast):
        st.subheader('Forecast data')
        st.write(forecast.tail())
    
        st.write(f'Forecast plot for {self.n_years} years')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

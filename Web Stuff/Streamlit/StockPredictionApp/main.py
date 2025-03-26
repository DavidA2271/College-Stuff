import streamlit_ui
import stock_options
import stock_predictor


def main():
    ui = streamlit_ui.ui()
    stock_optns = stock_options.options()
    ui.setup_stock_selections(stock_optns.stocks)
    ui.setup_prediction_years(stock_optns.min_years, stock_optns.max_years)

    predictor = stock_predictor.predictor(stock_optns.start, ui.selected_stock, ui.n_years)
    data = predictor.load_data()

    ui.write_raw_data(data)
    ui.plot_raw_data(data)

    m, forecast = predictor.predict(data)
    ui.plot_forecast(m, forecast)


if __name__ == "__main__":
    main()

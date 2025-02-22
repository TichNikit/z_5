import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")

    if 'RSI' in data:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['RSI'], label='RSI', color='orange')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.title(f"RSI для {ticker}")
        plt.xlabel("Дата")
        plt.ylabel("RSI")
        plt.legend()
        plt.savefig(f"{ticker}_{period}_RSI_chart.png")
        print(f"График RSI сохранен как {ticker}_{period}_RSI_chart.png")

    if 'MACD' in data:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['MACD'], label='MACD')
        plt.plot(data['Date'], data['MACD_Signal'], label='MACD Signal', linestyle='--')
        plt.title(f"MACD для {ticker}")
        plt.xlabel("Дата")
        plt.ylabel("MACD")
        plt.legend()
        plt.savefig(f"{ticker}_{period}_MACD_chart.png")
        print(f"График MACD сохранен как {ticker}_{period}_MACD_chart.png")

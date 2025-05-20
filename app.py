from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock/<stock_id>')
def get_stock(stock_id):
    try:
        ticker = f"{stock_id}.TW"
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        price = round(data["Close"].iloc[-1], 2)
        return jsonify({"price": price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

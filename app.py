from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock/<market>/<stock_id>')
def get_stock(market, stock_id):
    try:
        suffix = {
            "tw": ".TW",
            "us": "",
            "hk": ".HK"
        }.get(market.lower(), "")

        ticker = f"{stock_id}{suffix}"
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        if data.empty:
            return jsonify({"error": f"無法取得 {ticker} 的資料"}), 404

        price = round(data["Close"].iloc[-1], 2)
        return jsonify({"price": price})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
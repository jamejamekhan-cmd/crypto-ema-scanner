import requests

BOT_TOKEN = "اپنا نیا Bot Token یہاں لکھیں"
CHAT_ID = "6933246018"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })
from binance.client import Client

client = Client()

coins = [
    "BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT",
    "DOGEUSDT","ADAUSDT","TRXUSDT","LINKUSDT","AVAXUSDT",
    "SUIUSDT","TONUSDT","DOTUSDT","LTCUSDT","BCHUSDT",
    "UNIUSDT","ATOMUSDT","APTUSDT","NEARUSDT","HBARUSDT"
]

print("🚀 Crypto EMA Scanner Started")

for coin in coins:
    klines = client.get_klines(symbol=coin, interval=Client.KLINE_INTERVAL_5MINUTE, limit=30)

    closes = [float(k[4]) for k in klines]

    ema21 = sum(closes[-21:]) / 21

    last = closes[-1]
    prev = closes[-2]

    if prev < ema21 and last > ema21:
    send_telegram(f"🟢 BUY Signal: {coin}")

elif prev > ema21 and last < ema21:
    send_telegram(f"🔴 SELL Signal: {coin}")

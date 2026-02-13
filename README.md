# Binance Futures Testnet Trading Bot

A simplified CLI-based trading bot built in Python that places **Market** and **Limit** orders on **Binance Futures Testnet (USDT-M)**.

This project demonstrates:

* API integration
* Structured project design
* Input validation
* Logging
* Exception handling
* Clean CLI interface

---

# Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports **BUY** and **SELL**
* CLI-based user input
* Logs API requests and responses
* Handles invalid input and API errors
* Clean modular architecture

---

# Setup Instructions

Follow these steps carefully.

---

## Create Binance Futures Testnet Account

1. Register at Binance Futures Testnet.
2. Generate:

   * API Key
   * Secret Key
3. Keep them secure.

---

## Clone or Download the Project

If using Git:

```
git clone <your-repository-link>
cd trading_bot
```

Or extract the zip folder.

---

## Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Add Your API Credentials

Open `cli.py` and replace:

```
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
```

With your actual Binance Testnet API credentials.

---

# How to Run

All commands must be run from the project root folder.

---

## MARKET Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example output:

```
--- Order Request Summary ---
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

--- Order Response ---
Order ID: 123456789
Status: FILLED
Executed Quantity: 0.001
Average Price: 43000.50

Order placed successfully!
```

---

## LIMIT Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
```

For LIMIT orders:

* `--price` is mandatory
* Order will execute only when price is reached

---

# Log File

All API requests, responses, and errors are logged in:

```
trading.log
```

This file contains:

* Timestamps
* Order parameters
* API responses
* Error details (if any)

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
└── README.md
```

---

# Assumptions

1. User has a Binance Futures Testnet account.
2. API key and secret are valid and active.
3. User has sufficient testnet balance.
4. Symbol format follows Binance standard (e.g., BTCUSDT).
5. Only USDT-M futures are supported.
6. This bot does not manage leverage or margin settings.
7. This application is for educational/testing purposes only.

---

# Important Notes

* This project uses Binance **Testnet**, not real trading.
* No real funds are used.
* Do not share your API keys publicly.
* Always verify symbol and quantity before placing orders.

---

# Technologies Used

* Python 3.x
* python-binance
* argparse
* logging

---

# Evaluation Focus

This project demonstrates:

* Correct order placement on testnet
* Clean and modular code structure
* Input validation and error handling
* Useful logging implementation
* Professional CLI design

---


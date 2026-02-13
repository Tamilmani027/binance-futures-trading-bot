import os
import argparse
import logging
from dotenv import load_dotenv
from bot.orders import create_order
from bot.logging_config import setup_logging



def main():
    setup_logging()
    load_dotenv()

    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")

    if not API_KEY or not API_SECRET:
        print("API keys not found. Please check your .env file.")
        return

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price: {args.price}")

        result = create_order(
            API_KEY,
            API_SECRET,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Quantity: {result['executedQty']}")
        print(f"Average Price: {result['avgPrice']}")
        print("\n✅ Order placed successfully!")

    except Exception as e:
        logging.error(str(e))
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()

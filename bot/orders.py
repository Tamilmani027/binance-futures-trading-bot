from bot.client import BinanceFuturesClient
from bot.validators import validate_order_input

def create_order(api_key, api_secret, symbol, side, order_type, quantity, price=None):
    validate_order_input(symbol, side, order_type, quantity, price)

    client = BinanceFuturesClient(api_key, api_secret)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    response = client.place_order(**params)

    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice", "N/A"),
    }

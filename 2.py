def get_min_amount(exchange_id, symbol):
    exchange = eval("ccxt.{0}()".format(exchange_id))

    exchange.load_markets()

    return float(exchange.markets[symbol]["limits"]["amount"]["min"])
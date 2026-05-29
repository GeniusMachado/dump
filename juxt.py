"""
https://gist.github.com/dansmithy/fde6f2838de3002e1bdc44fe0319ed80

Trading
Background
At our bank we allow traders to book foreign exchange trades. A trade has:

Some currency being bought

Some currency being sold

For example, a trade might involve buying 1000 USD and selling 770 GBP.

Our trading system must consume a stream of events representing trading activity.

Our trading system will provide some aggregated information about the trades in the system.

Part 1
Create a data model for events that will represent trading activity.

Part 2
Create some code to aggregate a given collection of trade events and produce the net balance for each currency.

Each trade adjusts the corresponding currency balances: buying a currency increases its balance, and selling a currency decreases its balance.

During this exercise, think carefully about the interface to your code, and appropriate testing.

We’re here to answer questions about the requirements and clarify where things are not clear.


"""






balance = {"USD": 3785, "GBP": 2347}

def populate(input_parameter):
    global balance
    
    keys = list(input_parameter.keys())
    currency1 = keys[0]
    currency2 = keys[1]
    
    value_currency1 = input_parameter[currency1][0] - input_parameter[currency1][1]
    value_currency2 = input_parameter[currency2][0] - input_parameter[currency2][1]

    new_balance = {currency1: balance[currency1] + value_currency1, currency2: balance[currency2] + value_currency2}
    balance = new_balance

populate({"USD": [1000, 0], "GBP": [0, 770]})


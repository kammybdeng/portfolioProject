
def calForwardDiv(lastDiv, price):
    '''
    forward dividend yield
    using the last div payment, whereas the actual calculation should be
    based on the latest/announced div, but since api would not contain info of that
    last div payment is used.
    '''
    
    return lastDiv * 4 / price


def calTrailingDiv(historicals, price):
    '''
    trailing dividend yield
    '''

    if len(historicals) >= 4:
        annualDivTotal = sum([historicals[i]['dividend'] for i in range(4)])
        calculatedDivYield = annualDivTotal / price
        return calculatedDivYield


def calTotalVal(price, shares):
    return price * shares

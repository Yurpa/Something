from utils.functions import censored, checkout, last_struggle


def test_Censored():
    assert censored('Visa Gold 3589276410671603') == 'Visa Gold 3589 27** **** 1603'

def test_Checkout():
    assert checkout() == [863064926, 801684332, 154927927, 114832369, 482520625]

def test_last_struggle():
    assert last_struggle() == last_struggle()

test_Checkout()
test_last_struggle()
test_Censored()
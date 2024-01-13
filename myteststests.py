import mytests as main


def test_say_hello():
    assert main.say_hello() == "Hello World"


def test_hey_you():
    assert main.hey_you("Nate") == "Hello, Nate!"


def test_age_in_2050_born_1990():
    assert main.age_in_2050(1990) == (2050 - 1990)


def test_can_I_take_your_order_cost():
    assert main.can_i_take_your_order(2, 3, 4) == (2 * 4.5 + 3 * 1.5 + 4 * 1.00)
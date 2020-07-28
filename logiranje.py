import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def add (x, y):

    return x + y

def substract (x, y):

    return x - y

def multiply (x, y):

    return x*y

def divide (x, y):

    return x/y

br1 = 20
br2= 5

zbroj = add(br1, br2)
logging.debug('Zbroj: {} + {} = {}'.format(br1, br2, zbroj))

razlika = substract(br1, br2)
logging.debug('Razlika: {} - {} = {}'.format(br1, br2, razlika))

umnozak = multiply(br1, br2)
logging.debug('Umnozak: {} * {} = {}'.format(br1, br2, umnozak))

dijel = divide(br1, br2)
logging.debug('Dijeljenje: {} / {} = {}'.format(br1, br2, dijel))
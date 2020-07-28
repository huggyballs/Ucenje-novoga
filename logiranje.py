import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
filehandler = logging.FileHandler('test.log')
filehandler.setFormatter(formatter)

stream = logging.StreamHandler()
stream.setFormatter(formatter)

logger.addHandler(filehandler)
logger.addHandler(stream)

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
logger.debug('Zbroj: {} + {} = {}'.format(br1, br2, zbroj))

razlika = substract(br1, br2)
logger.debug('Razlika: {} - {} = {}'.format(br1, br2, razlika))

umnozak = multiply(br1, br2)
logger.debug('Umnozak: {} * {} = {}'.format(br1, br2, umnozak))

dijel = divide(br1, br2)
logger.debug('Dijeljenje: {} / {} = {}'.format(br1, br2, dijel))
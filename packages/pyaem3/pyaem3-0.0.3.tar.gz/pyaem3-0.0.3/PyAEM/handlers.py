from bs4 import BeautifulSoup

from . import exception


def auth_fail(response):
    code = response['http_code']
    message = 'Authentication failed - incorrect username and/or password'

    raise exception.PyAemException(code, message, response)


def method_not_allowed(response):
    code = response['http_code']
    soup = BeautifulSoup(response['body'])
    message = soup.title.string

    raise exception.PyAemException(code, message, response)


def unexpected(response):
    code = response['http_code']
    message = 'Unexpected response\nhttp code: {0}\nbody:\n{1}'.format(response['http_code'], response['body'])

    raise exception.PyAemException(code, message, response)

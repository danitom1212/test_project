import pytest

import logging

from py import test
from selfData import Date
import pytest
import logging

d1 = Date(29, 3, 2013)
d2 = Date(21, 3, 2013)


def test_init():
    if (d1 >= Date(20, 7, 2022)):
        assert logging.warning('This is a warning message')
    assert isValid


def test_str():
    try:
        d1
    except:
        logging.error('This is an info message')
        assert None


def test_eq():
    try:
        assert d1 == d2
    except:
        logging.warning('This is a debug message')
        assert d1 == d2

def test_gt():
    if d1 > d2:
        assert d1 > d2
    else:
        logging.warning('This tests failed  data2 is smaller ')
        assert d1 > d2


def test_lt():
    if d1 < d2:
        assert d1 < d2
    else:
        logging.warning('This tests failed  data2 is bigger.')
        assert d1 < d2


def test_le():
    if d1 <= d2:
        assert d1 <= d2
    else:
        logging.warning('tests failed  data1 is bigger or equal')
        assert d1 <= d2

def test_ge():
    if d1 >= d2:
        assert d1 >= d2
    else:
        logging.warning('tests failed  data1 is smellr or equal')
        assert d1 >= d2


def test_ne():
    if d1 != d2:
        assert d1 != d2
    else:
        logging.warning('This test failed because the dates is not equals .')
        assert d1 != d2


def test_sub():
    if d1 - d2:
        assert d1 - d2
    else:
        logging.error("How did you manage to get something non-date into your mouth?")
        assert d1 - d2


def isValid():
    try:
        assert d1
    except:
        logging.info("The is invalid")
        assert d1


def test_get_next_day():
    d = d1.get_next_days()
    if d > d1:
        assert d > d1
    else:
        logging.error("Check date ")


def test_get_next_days():
    d = d2.get_next_days()
    if d > d2:
        assert d > d2
    else:
        logging.error("Check date ")



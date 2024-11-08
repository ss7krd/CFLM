from helpers import * 
import pytest
import numpy as np

import logging

LOGGER = logging.getLogger(__name__)


def test_split_data():
    old_data = np.array([5,1,2,3,4,5])
    get = split_data(old_data, 3)[0].shape
    expect = (2,)
    assert(get == expect)
    # assert all shapes are equal 


def test_avg_weights():
    # using body of function to make this easier
    num_clients = 2
    client_weights = list()
    w1 = np.array([2,4])
    w2 = np.array([4,8])
    client_weights.append(w1)
    client_weights.append(w2)
    client_weights = np.vstack(client_weights)
    avg_weights = np.mean(client_weights, axis=0) # See docs to understand why axis=0 at https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    assert(np.array_equal(avg_weights, np.array([3,6])))


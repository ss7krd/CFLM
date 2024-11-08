import numpy as np
import pickle
import subprocess
import docker 
import os
import time
def split_data(data, num_clients):
    '''
    Returns data divided for each num_client. 
    Client's 0 data accessed at zeroeth index of the returned list
    '''
    return np.split(data, num_clients)

def avg_weights(model, num_clients):
    '''
    Loads pickled data from ./client_results directory
    Averages weights
    Returns the array of weights
    '''
    client_weights = list() # Weights for client 0 will be in 0th index
    # Load all data
    for client in range(num_clients): 
        weights = pickle.load(open(f'./weights/client{client}_weights', 'rb'))
        client_weights.append(weights)
    average_weights = np.mean(client_weights, axis=0) # See docs to understand why axis=0 at https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    return average_weights 
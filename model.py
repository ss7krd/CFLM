import tensorflow as tf
import os
import pickle
import numpy as np
from helpers import *
import docker 
import subprocess
import time

def main():
    try:
        app()
    finally:
        cleanup()

def cleanup():
    subprocess.run("docker container kill $(docker ps -q)", shell=True)

def app():
    mnist = tf.keras.datasets.mnist

    # Load data
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    # Describe model
    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile model 
    model.compile(optimizer='adam',
                loss='mse',
                metrics=['accuracy'])
    # dump model definition 
    pickle.dump(model, open('data/model', 'wb'))
    # Set num_clients
    num_clients = 2
    # Set epochs 
    epochs = 1

    # Split data equally for each clients, where the indices specify the client - e.g. x_train[0] is client 0's data
    # ! Note - must be able to be equally split . . . RaggedTensors beware.
    x_train, y_train = split_data(x_train, num_clients), split_data(y_train, num_clients)

    # Initialize master node (this) and list of containers
    master = docker.from_env()
    containers = list()

    # Working loop 
    client_scripts_path = os.path.abspath('./client_scripts')
    data_path = os.path.abspath('./data')
    weights_path = os.path.abspath('./weights')
    for epoch in range(epochs):
        if epoch == 0:
            # Start the containers and give them their data 
            for client in range(num_clients):
                # spin up a docker container for it, naming it client0, client1 . . . 
                worker = master.containers.run('tensorflow/tensorflow:latest', detach=True, 
                volumes = [f'{client_scripts_path}:/client_scripts', f'{data_path}:/data', f'{weights_path}:/weights'], tty=True, stdin_open=True)
                worker.start()
                # Load it's model
                # worker.exec_run(f'python client_scripts/load_model.py {client}')
                # give it it's section of the data, using client # as idx 
                x_train_data, y_train_data = x_train[client], y_train[client] 
                # dump it
                pickle.dump(x_train_data, open('./data/x_train', 'wb'))
                pickle.dump(y_train_data, open('./data/y_train', 'wb'))


                # append to list of containers 
                containers.append(worker)
        else: 
            # Average the weights from previous epoch results 
            weights = avg_weights(model, num_clients)
            # Dump weights to a shared resource location - in this case, a file called 'weights' in the 'data' shared volume dir
            pickle.dump(weights, open('./data/weights', 'wb'))

        for client in range(num_clients):
            # containers[client].exec_run(f'python client_scripts/set_weights.py {client}')
            # Train the epoch and dump new weights
            containers[client].exec_run(f'python client_scripts/train_epoch.py {client}')
            #weights_folder_filled = len(os.listdir('./weights')) != 0
                     

    # Finally, get the avg weights and evaluate 
    weights = avg_weights(model, num_clients)
    model.set_weights(weights)
    model.evaluate(x_test, y_test)


if __name__ == '__main__':
    main()
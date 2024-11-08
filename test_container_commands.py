import tensorflow as tf
import os
import pickle
import numpy as np
from helpers import *
import docker 
import subprocess

client_scripts_path = os.path.abspath('./client_scripts')
data_path = os.path.abspath('./data')
weights_path = os.path.abspath('./weights')
master = docker.from_env()
client = 0
# spin up a docker container for it, naming it client0, client1 . . . 
worker = master.containers.run('tensorflow/tensorflow:latest', detach=True, 
volumes = [f'{client_scripts_path}:/client_scripts', f'{data_path}:/data', f'{weights_path}:/weights'], tty=True, stdin_open=True)
worker.start()
worker.exec_run(f'python client_scripts/train_epoch.py {client}')

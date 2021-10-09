#!/usr/bin/python3
import yaml
filepath='../files/postgres.yaml'

def read_vars_from_file ():
    with open(filepath) as f:
        my_dict = yaml.safe_load(f)
    f.close()
    return my_dict

def get_ansible_vars (dict):
    tag = dict.get('tag')
    container_name = dict.get('container_name')
    running = dict.get('running')

#def get_container_envs ():


get_ansible_vars(read_vars_from_file())
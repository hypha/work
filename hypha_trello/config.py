import os
import cPickle as pickle

def get_config_dir():
    home = os.path.expanduser("~/")
    config = os.path.join(home, ".config/")
    if not os.path.exists(config):
        os.makedirs(config)
    trello = os.path.join(config, "trello/")
    if not os.path.exists(trello):
        os.makedirs(trello)
    return trello


def file_config():
    config_dir = get_config_dir()
    config_file = os.path.join(config_dir, "mytrello" + ".conf")
    return config_file


def save_set(credentials):
    with open(file_config(), "wb")as f:
        pickle.dump(credentials, f)


def read_set():
    with open(file_config(), "rb") as f:
        saved_config = pickle.load(f)
    return saved_config


def set_credentials():
    api = raw_input("Your API is: ")
    token = raw_input("Your Token is: ")
    credentials = {"api": api, "token": token}
    save_set(credentials)
    return credentials


def get_credentials():
    try:
        credentials = read_set()
        return credentials
    except IOError:
        credentials = set_credentials()
        save_set(credentials)
        return credentials


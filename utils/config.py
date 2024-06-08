import configparser
import os

icon_path = "assets/icon.ico"
version = "0.0.1"


def load_config():

    config = configparser.ConfigParser()

    if os.path.exists('config.ini'):
        config.read('config.ini')
        return config
    else:
        print("Error: config.ini not found. Creating a new one...")
        create_config()
        return None


def create_config():
    config = configparser.ConfigParser()

    config['SETTINGS'] = {
        'init_data': 'your_init_data_here',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("A new config.ini file has been created. Please fill in your Init data and user agent.")
import configparser
import os

icon_path = "assets/icon.ico"
version = "0.0.1"
common_headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru',
    'Origin': 'https://tonclayton.fun',
    'Host': 'tonclayton.fun',
    'Referer': 'https://tonclayton.fun/',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty'
}
def load_config():

    config = configparser.RawConfigParser()

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
    input("Enter to exit...")
    exit()
from utils.config import load_config
config = load_config()
if __name__ == "__main__":
    if config:
        init_data = config['SETTINGS']['init_data']
        user_agent = config['SETTINGS']['user_agent']
        print(f"Init data: {init_data}")
        print(f"User Agent: {user_agent}")
import smeshi
import json

def get_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    return config

def main():
    config = get_config()
    smeshi.start(config)

if __name__ == '__main__':
    main()
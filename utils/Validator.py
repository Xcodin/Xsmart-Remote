import configparser, os, inspect
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
config = configparser.ConfigParser()
# Main Folder
mainFolder = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), os.pardir))
# configuration file path
confPath = mainFolder + '/etc/Xsmart.conf'


class Validate:
    def __init__(self):

        try:
            config.read_file(open(confPath))
            logging.info('Configuration File Opened.')
        except Exception as error:
            logging.error('Can\'t open configuration file')
            logging.debug(error)

    def get_actiontype(self):
        return config.get("settings", "actionType")

    def get_blinkTime(self):
        return config.getint("settings", "blink_time")

    def get_pinId(self):
        return config.getint("settings", "pin_id")

# TODO "action Types list to be defined"

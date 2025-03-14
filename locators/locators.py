import configparser
import os


class Locators:

    def locator(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        _file_path = str(os.path.abspath(cur_dir))[:-8]
        # print(_file_path)
        _file = _file_path + "\\" + "locators.ini"
        # print(_file)
        parser = configparser.ConfigParser()
        parser.read(_file)
        return parser

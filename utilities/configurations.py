import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read("/Users/alexkibryk/PycharmProjects/Education/utilities/properties.ini")
    return config
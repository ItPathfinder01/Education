import configparser
import psycopg2

def getConfig():
    config = configparser.ConfigParser()
    config.read("/Users/alexkibryk/PycharmProjects/Education/utilities/properties.ini")
    return config



connection_config = {
    "user": getConfig()["SQL"]["user"],
    "password": getConfig()["SQL"]["password"],
    "database": getConfig()["SQL"]["database"],
    "host": getConfig()["SQL"]["host"]
}


def getConnection():
    try:
        conn = psycopg2.connect(**connection_config)
        if not conn.closed:
            print("Connection established")
            return conn
    except Exception as e:
        print("Error:", str(e))

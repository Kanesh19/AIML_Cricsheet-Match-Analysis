import utils
print("Using utils from:", utils.__file__)

import pymysql
from sqlalchemy import create_engine
from utils import get_conf_values
from urllib.parse import quote_plus
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__name__))

config_file_path = path + os.sep + "project.ini"

conf = get_conf_values(config_file_path)

# print(conf)

host = conf["database"]["host"]
port = conf["database"]["port"]
user_name = conf["database"]["user_name"]
password = conf["database"]["password"]
database = conf["database"]["database"]

encode_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://{user_name}:{encode_password}@{host}:{port}/{database}")

data_path = path + os.sep + "data" + os.sep + "csv"

for file_name in os.listdir(data_path):
    path = os.path.join(data_path,file_name)
    df = pd.read_csv(path)
    if file_name == "odis.csv":
        df.to_sql(name="odi_matches",con=engine,if_exists="replace",index=False)
        print("Odis data uploaded to SQL database")
    elif file_name == "t20s.csv":
        df.to_sql(name="t20_matches",con=engine,if_exists="replace",index=False)
        print("t20s data uploaded to SQL database")
    elif file_name == "tests.csv":
        df.to_sql(name="test_matches",con=engine,if_exists="replace",index=False)
        print("tests data uploaded to SQL database")

import pymysql
from sqlalchemy import create_engine
import pandas as pd
from utils import get_conf_values
import os
from urllib.parse import quote_plus

path = os.path.dirname(os.path.abspath(__name__))

conf_path = path + os.sep + "project.ini"

conf = get_conf_values(conf_path)

host = conf["database"]["host"]
port = conf["database"]["port"]
user_name = conf["database"]["user_name"]
password = conf["database"]["password"]
database = conf["database"]["database"]

encryp_password =  quote_plus(password)



def get_sql_data(query):
    uri = f"mysql+pymysql://{user_name}:{encryp_password}@{host}:{port}/{database}"
    engine = create_engine(uri)
    df = pd.read_sql(query,con=engine)
    return df


def start_sql_anayse():
    print("ODI Match SQL Anaylsis")
    sql_queries = [
        "select batter,runs_batter from odi_matches order by runs_batter DESC LIMIT 10;",
        "SELECT batter, SUM(runs_batter) AS total_runs FROM odi_matches  GROUP BY batter ORDER BY COUNT(runs_batter) DESC;",
        "select winner,count(winner) as total_win from odi_matches group by winner order by count(winner) desc;",
        """SELECT 
                LEAST(team_1, team_2) AS team_A,  
                GREATEST(team_1, team_2) AS team_B,
                COUNT(*) AS total_matches,
                SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) AS team_1_wins,
                SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) AS team_2_wins,
                ROUND(100 * SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_1_win_rate,
                ROUND(100 * SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_2_win_rate
            FROM odi_matches  
            WHERE winner IS NOT NULL  
            GROUP BY team_A, team_B
            ORDER BY total_matches DESC;
        """,
        "select batter,runs_batter from t20_matches order by runs_batter DESC LIMIT 10;",
        "SELECT batter, SUM(runs_batter) AS total_runs FROM t20_matches  GROUP BY batter ORDER BY COUNT(runs_batter) DESC;",
        "select winner,count(winner) as total_win from t20_matches group by winner order by count(winner) desc;",
        """SELECT 
            LEAST(team_1, team_2) AS team_A,  
            GREATEST(team_1, team_2) AS team_B,
            COUNT(*) AS total_matches,
            SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) AS team_1_wins,
            SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) AS team_2_wins,
            ROUND(100 * SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_1_win_rate,
            ROUND(100 * SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_2_win_rate
        FROM t20_matches  
        WHERE winner IS NOT NULL  
        GROUP BY team_A, team_B
        ORDER BY total_matches DESC;
        """,
        "select batter,runs_batter from test_matches order by runs_batter DESC LIMIT 10;",
        "SELECT batter, SUM(runs_batter) AS total_runs FROM test_matches  GROUP BY batter ORDER BY COUNT(runs_batter) DESC;",
        "select winner,count(winner) as total_win from test_matches group by winner order by count(winner) desc;",
        """SELECT 
        LEAST(team_1, team_2) AS team_A,  
        GREATEST(team_1, team_2) AS team_B,
        COUNT(*) AS total_matches,
        SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) AS team_1_wins,
        SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) AS team_2_wins,
        ROUND(100 * SUM(CASE WHEN winner = team_1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_1_win_rate,
        ROUND(100 * SUM(CASE WHEN winner = team_2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS team_2_win_rate
        FROM test_matches  
        WHERE winner IS NOT NULL  
        GROUP BY team_A, team_B
        ORDER BY total_matches DESC;
        """ 
    ]
    for idx,query in enumerate(sql_queries):
        if idx <=3:
            print(f"ODI MATCH SQL oder No :{idx+1}")
            df = get_sql_data(query)
            print(df)
        elif idx<=7:
            print(f"T20 Match SQL oder No:{idx+1}")
            df = get_sql_data(query)
            print(df)
        elif idx<=11:
            print(f"Test matched SQL query no:{idx+1}")
            df = get_sql_data(query)
            print(df)
    return True

start_sql_anayse()
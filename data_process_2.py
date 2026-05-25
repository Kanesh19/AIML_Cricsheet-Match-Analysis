import pandas as pd
import zipfile
import os
import json
from pathlib import Path

path = os.path.dirname(os.path.abspath(__name__))

extracted_folder = path + os.sep + "extracted_json"

odis_path = path + os.sep + "cricsheet_json" + os.sep + "odis_json.zip"
t20s_path = path + os.sep + "cricsheet_json" + os.sep + "t20s_json.zip"
tests_path = path + os.sep + "cricsheet_json" + os.sep + "tests_json.zip"

data_folder = path + os.sep + "data"+ os.sep + "csv"


os.makedirs(extracted_folder,exist_ok=True)
os.makedirs(data_folder,exist_ok=True)


def get_data_from_json(zip_path):


    with zipfile.ZipFile(zip_path,"r") as zip_ref:
        zip_ref.extractall(extracted_folder)

    records =[]
    for file_name in os.listdir(extracted_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(extracted_folder,file_name)

            with open(file_path,"r") as f:
                data = json.load(f)

            match_info = {
                "match_type":data["info"]["match_type"],
                "venue":data["info"]["venue"],
                "city":data["info"].get("city",""),
                "date":data["info"]['dates'][-1],
                "team_1":data["info"]['teams'][0],
                "team_2":data["info"]["teams"][1],
                "toss_winner":data["info"]["toss"]["winner"],
                "toss_decision":data["info"]["toss"]["decision"],
                "winner":data["info"]["outcome"].get("winner",""),
                "win_by_runs": data["info"]["outcome"].get("by",{}).get("runs","")
            }

            for inning in data["innings"]:
                team = inning["team"]
                for overs in inning["overs"]:
                    over_num = overs["over"]
                    for ball in overs["deliveries"]:
                        delivery_info = {
                            "team":team,
                            "over":over_num,
                            "batter":ball["batter"],
                            "bowler":ball["bowler"],
                            "non_striker":ball["non_striker"],
                            "runs_batter":ball["runs"]["batter"],
                            "runs_extras":ball["runs"]["extras"],
                            "runs_total":ball["runs"]["total"]
                        }
                        if "wickets" in ball:
                            delivery_info["wickets_player_out"] = ball["wickets"][0]["player_out"]
                            delivery_info["wickets_kind"] = ball["wickets"][0]["kind"]
                            # delivery_info["wickets_catch_by"] = ball["wickets"][0]["fielders"][-1]["name"]
                        else:
                            delivery_info["wickets_player_out"] = None
                            delivery_info["wickets_kind"] = None
                            # delivery_info["wickets_catch_by"] = None
                        delivery_info.update(match_info)
                    records.append(delivery_info)
    return records

odis_recods = get_data_from_json(odis_path)
if odis_recods:
    odi_df = pd.DataFrame(odis_recods)
    df_odi_path = data_folder + os.sep + "odis.csv"
    odi_df.to_csv(df_odi_path,index=False)
    delete_odis = [file.unlink() for file in Path(extracted_folder).glob("*") if file.is_file()]
    print("Odis files deleted")

t20s_records = get_data_from_json(t20s_path)
if t20s_records:
    t20s_df = pd.DataFrame(t20s_records)
    df_t20s_path= data_folder + os.sep + "t20s.csv"
    t20s_df.to_csv(df_t20s_path,index=False)
    delete_t20s = [file.unlink() for file in Path(extracted_folder).glob("*") if file.is_file()]
    print("Deleted t20s data")

tests_records = get_data_from_json(tests_path)
if tests_records:
    test_df = pd.DataFrame(tests_records)
    tests_path = data_folder + os.sep + "tests.csv"
    test_df.to_csv(tests_path,index=False)
    delete_test = [file.unlink() for file in Path(extracted_folder).glob("*") if file.is_file()]
    print("Delted tests data")







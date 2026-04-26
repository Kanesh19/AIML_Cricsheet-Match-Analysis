import pandas as pd
import os
import json
import glob

class match_summary:
    def __init__(self, json_folder):
        self.json_folder = json_folder
        self.match_list = self.get_files()
        

    def get_files(self):
        all_files = []
        for root, dris, files in os.walk(self.json_folder):
            files = glob.glob(os.path.join(root,'*.json'))
            for f in files:
                all_files.append(os.path.abspath(f))
        return all_files
    
    def load_json(self):
        tournament_list = []
        for match_detail in self.match_list:
            with open (match_detail, 'r', encoding='utf-8') as doc:
                exp = json.load(doc)
                tournament_list.append(exp)
        return tournament_list

    def get_over_data(self):
        tournament_list = self.load_json()
        match_dataframes = []

        for exp in tournament_list:
            match_info = exp.get('info', {})
            match_details = {
                "city": match_info.get("city", "Unknown"),
                "date": match_info.get("dates", ["Unknown"])[0],
                "event_name": match_info.get("event", {}).get("name", "Unknown"),
                "match_type": match_info.get("match_type", "Unknown"),
                "winner": match_info.get("outcome", {}).get("winner", "Unknown"),
                "player_of_match": ", ".join(match_info.get("player_of_match", ["Unknown"]))
            }


            innings = exp.get('innings',[])
            deliveries_list = []
            
            for inning_data in innings:
                inning_name = inning_data.get('team', 'Unknown Team')
                overs = inning_data.get('overs', [])
                
                for over_data in overs:
                    over_number = over_data.get('over', None)
                    deliveries = over_data.get('deliveries', [])
                    
                    for delivery in deliveries:
                        delivery['inning'] = inning_name
                        delivery['over'] = over_number
                        
                        runs = delivery.get('runs', {})
                        delivery['runs_batter'] = runs.get('batter', 0)
                        delivery['runs_extras'] = runs.get('extras', 0)
                        delivery['runs_total'] = runs.get('total', 0)
                        
                        full_delivery = {**match_details, **delivery}
                        deliveries_list.append(full_delivery)

            df = pd.DataFrame(deliveries_list)
            
            col_to_remove = ['extras', 'wickets', 'replacements', 'review', 'runs']
            df = df.drop(columns=[col for col in col_to_remove if col in df.columns], errors='ignore')
            match_dataframes.append(df)

        final_df = pd.concat(match_dataframes, ignore_index=True)

        return final_df 
    
json_folder = 'ipl_json'
match_sum = match_summary(json_folder)
ipl_data_table = match_sum.get_over_data()
print(ipl_data_table)

json_folder = 'odis_json'
match_sum = match_summary(json_folder)
odi_data_table = match_sum.get_over_data()
print(odi_data_table)

json_folder = 't20s_json'
match_sum = match_summary(json_folder)
t20_data_table = match_sum.get_over_data()
print(t20_data_table)

json_folder = 'tests_json'
match_sum = match_summary(json_folder)
test_data_table = match_sum.get_over_data()
print(test_data_table) 
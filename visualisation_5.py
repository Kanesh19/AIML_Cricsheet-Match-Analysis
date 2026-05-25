import matplotlib.pyplot as plt
import pandas as pd
import os

path = os.path.dirname(os.path.abspath(__name__))

exec_path = path + os.sep + "data" + os.sep + "csv"



image_path = path + os.sep + "data" + os.sep + "image"
os.makedirs(image_path,exist_ok=True)


for file_name in os.listdir(exec_path):
    if file_name.endswith(".csv"):
        if file_name == "odis.csv":
            print("Starting ODI match pictures")
            current_path = os.path.join(exec_path,file_name)
            odi_df = pd.read_csv(current_path)
            winner_df = odi_df.dropna(how="any",axis=0)
            # Overs Vs Total Runs
            # analyse trends over times line chart
            plt.figure(figsize=(10, 6))
            print("Starting the Line chart")
            plt.plot(odi_df["over"],odi_df['runs_total'],color="blue",ls="--",marker="*")
            plt.xlabel("Over",fontsize=14)
            plt.ylabel("Total Runs",fontsize=14)
            plt.title("Overs Vs Total Runs")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"ODI_line_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # bar chart - catagerical comparision
            plt.figure(figsize=(10, 6))
            plt.bar(winner_df['team'],winner_df['winner'],color='purple')
            plt.xlabel("Team",fontsize=14)
            plt.ylabel("Winners",fontsize=14)
            plt.title("Team Vs Winners")
            plt.xticks(rotation=90,ha='center',fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"ODI_bar_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # hist - find data distribution
            plt.figure(figsize=(10, 6))
            plt.hist(odi_df['team'],bins=30,color="orange")
            plt.xlabel("Team")
            plt.ylabel("Team Freq")
            plt.xticks(rotation=90,fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"ODI_histogram.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # box-blot - find outlier
            plt.figure(figsize=(10, 6))
            plt.boxplot(odi_df['runs_batter'],patch_artist=True)
            plt.xlabel("Player")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"ODI_boxplot.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")
        elif file_name == "t20s.csv":
            print("Starting T20s match pictures")
            current_path = os.path.join(exec_path,file_name)
            t20_df = pd.read_csv(current_path)
            winner_df = t20_df.dropna(how="any",axis=0)
            # Overs Vs Total Runs
            # analyse trends over times line chart
            print("Starting the Line chart")
            plt.figure(figsize=(10, 6))
            plt.plot(t20_df["over"],t20_df['runs_total'],color="blue",ls="--",marker="*")
            plt.xlabel("Over")
            plt.ylabel("Total Runs")
            plt.title("Overs Vs Total Runs")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"T20_line_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # bar chart - catagerical comparision
            plt.figure(figsize=(10, 6))
            plt.bar(winner_df['team'],winner_df['winner'],color='purple')
            plt.xlabel("Team")
            plt.ylabel("Winners")
            plt.title("Team Vs Winners")
            plt.xticks(rotation=90,ha='center',fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"T20_bar_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # hist - find data distribution
            plt.figure(figsize=(10, 6))
            plt.hist(t20_df['team'],bins=30,color="orange")
            plt.xlabel("Team")
            plt.ylabel("Team Freq")
            plt.xticks(rotation=90,fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"T20_histogram.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # box-blot - find outlier
            plt.figure(figsize=(10, 6))
            plt.boxplot(t20_df['runs_batter'],patch_artist=True)
            plt.xlabel("Player")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"T20_boxplot.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")
        elif file_name == "tests.csv":
            print("Starting Test match pictures")
            current_path = os.path.join(exec_path,file_name)
            t20_df = pd.read_csv(current_path)
            winner_df = t20_df.dropna(how="any",axis=0)
            # Overs Vs Total Runs
            # analyse trends over times line chart
            print("Starting the Line chart")
            plt.figure(figsize=(10, 6))
            plt.plot(t20_df["over"],t20_df['runs_total'],color="blue",ls="--",marker="*")
            plt.xlabel("Over")
            plt.ylabel("Total Runs")
            plt.title("Overs Vs Total Runs")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"Test_line_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # bar chart - catagerical comparision
            plt.figure(figsize=(10, 6))
            plt.bar(winner_df['team'],winner_df['winner'],color='purple')
            plt.xlabel("Team")
            plt.ylabel("Winners")
            plt.title("Team Vs Winners")
            plt.xticks(rotation=90,ha='center',fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"Test_bar_chart.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # hist - find data distribution
            plt.figure(figsize=(10, 6))
            plt.hist(t20_df['team'],bins=30,color="orange")
            plt.xlabel("Team")
            plt.ylabel("Team Freq")
            plt.xticks(rotation=90,fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"Test_histogram.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")

            # box-blot - find outlier
            plt.figure(figsize=(10, 6))
            plt.boxplot(t20_df['runs_batter'],patch_artist=True)
            plt.xlabel("Player")
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12) 
            img_path = os.path.join(image_path,"Test_boxplot.png")
            plt.savefig(img_path,dpi=300,bbox_inches="tight")
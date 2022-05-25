#This program parses Jatin's CSV data of Premier League players in the 21-22
#season and creates a TKinter GUI for data analysis and visualisation.
#https://www.kaggle.com/datasets/jkanthony/premier-league-stats-top-50-players?datasetId=2203030
import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import ttk

#------------------------------------TODO:-------------------------------------------
#Add matplotlib graph feature
#Add style!
#Tweak formatting to make it a bit neater.
#More filtering options?


#Initialises SQLite3 connection
con = sqlite3.connect("pl_players.sql")

#Creates and configures main application window with a grid layout
root = tk.Tk()
root.title("Premier League Players 21-22")
root.geometry("1200x700")
for i in range(0,12):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

#------- Creates GUI elements for Form -----------
heading = tk.Label(root, text="Filter Results:")
heading.grid(row=0, column=0, sticky="EW")

#Filter by team...
teams = ("Any", "Arsenal", "Aston Villa", "Brentford", "Brighton", "Burnley",
"Chelsea", "Crystal Palace", "Everton", "Leeds", "Leicester", "Liverpool",
"Manchester City", "Manchester United", "Newcastle United", "Norwich", "Southampton",
"Tottenham", "Watford", "West Ham", "Wolverhampton Wanderers")
team_label = tk.Label(root, text="Team:")
team_label.grid(row=1, column=0, sticky="EW")
from_team = ttk.Combobox(root, values=teams, textvariable=teams, state="readonly")
from_team.current(0)
from_team.grid(row=1,column=1, sticky="W")

#By minutes played...
mins_label = tk.Label(root, text="Minimum Minutes Played:")
mins_label.grid(row=2, column=0, sticky="EW")
mins = tk.IntVar()
mins_played = ttk.Spinbox(root, from_=0.0, to=3000, textvariable=mins,
state="readonly", increment=500)
mins_played.grid(row=2, column=1, sticky="W")

#By appearances...
apps_label = tk.Label(root, text="Minimum Appearances:")
apps_label.grid(row=3, column=0, sticky="EW")
apps = tk.IntVar()
appearances = ttk.Spinbox(root, from_=0.0, to=38, textvariable=apps,
state="readonly")
appearances.grid(row=3, column=1, sticky="W")

stats_button = tk.Button(root, text="Generate Stats",
command=lambda : generate_stats(mins_played.get(), appearances.get(), from_team.get()))
stats_button.grid(row=4, column=1, sticky="W")

#--------Uses TKinter's Treeview class to create a table displaying results----------
table = ttk.Treeview(root, columns=("Team", "Apps", "Mins", "G", "A",
"xGp90", "xAp90"))
table["columns"] = ("Team", "Apps", "Mins", "G", "A","xGp90", "xAp90")
table.grid(row=5, column=0, columnspan=3, sticky="E")
for i in table["columns"]:
    table.column(i, width=80)
    table.heading(i, text=str(i))


#--------Parses CSV File into Pandas DataFrame, then initialises SQL Database---------
df = pd.read_csv("Premier_league_players.csv")
df = df.drop(columns=["№", "xG", "xA"])
print(df.head())
df.to_sql("pl_players", con, if_exists="replace")

#--------Generate Stats function, triggered on click of button----------
def generate_stats(mins, apps, team):
    for i in table.get_children(): #Clears table
        table.delete(i)
    if team == "Any": #Uses if statement to check for all teams selected
        df = pd.read_sql_query(f"""SELECT * FROM pl_players WHERE (Apps >= {apps})
    AND (Min >= {mins})""", con)
    else:
        df = pd.read_sql_query(f"""SELECT * FROM pl_players WHERE (Apps >= {apps})
        AND (Min >= {mins}) AND Team = '{team}'""", con)
    print(df.head())
    data = [] #Adds each row of new dataframe into a list, then inserts each item in list to table
    for row in df.iterrows():
        data.append([row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6], row[1][7], row[1][8]])
    for i in data:
        table.insert("", tk.END, text = i[0], values=i[1:])
    return df

root.mainloop()
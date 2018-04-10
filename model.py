# model.py

import csv

BB_FILE_NAME = 'umbball.csv'

FB_FILE_NAME = 'umfootball.csv'

b_seasons = []


def init_ball(csv_file_name):
    global b_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        if csv_file_name == BB_FILE_NAME:
            next(reader)
            next(reader)
        elif csv_file_name == FB_FILE_NAME:
            next(reader)
        global b_seasons
        b_seasons = []
        for r in reader:
            year = r[1]
            win = int(r[3])
            lose = int(r[4])
            if csv_file_name == BB_FILE_NAME:
                win_per = float(r[5])
            elif csv_file_name == FB_FILE_NAME:
                win_per = float(r[6])
            else:
                win_per = 0
            res = [year, win, lose, win_per]
            b_seasons.append(res)


def get_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 0
    elif sortby == 'wins':
        sortcol = 1
    elif sortby == 'pct':
        sortcol = 3
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(b_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list

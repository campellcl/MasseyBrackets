"""
Driver.py
    Driver for Massey Bracketology Program. Takes 1 command line argument:
        1. The name of the file to read.
@Author: Chris Campell
@Version: 1.0
@Date: 2/28/2016
"""
import sys
import traceback
import json
import numpy as np
import sklearn
from pprint import pprint

def main(cmd_args):
    M = None
    y = None
    data = None
    teams = []
    num_teams = 0
    num_games = 0

    try:
        with open(cmd_args[1]) as input_file:
            data = json.load(input_file)
            num_games = len(data)
        for game in data:
            home_team = game['home']['team']
            away_team = game['away']['team']
            if home_team not in teams:
                teams.append(home_team)
                num_teams += 1
            if away_team not in teams:
                teams.append(away_team)
                num_teams += 1
        M = [[np.NaN for y in range(num_teams)] for x in range(num_games)]
        y = []
        game_index = 0
        for game in data:
            home_team = game['home']['team']
            away_team = game['away']['team']
            team_index = 0
            for team in teams:
                if teams[team_index] == home_team:
                    M[game_index][team_index] = 1
                elif teams[team_index] == away_team:
                    M[game_index][team_index] = -1
                else:
                    M[game_index][team_index] = 0
                team_index += 1
            #Construct y matrix of score differences (home-away) for each game.
            y.append(game['home']['pts'] - game['away']['pts'])
            game_index += 1
        # Singularize the matrices
        M.append([1 for x in range(num_teams)])
        y.append(0)
        # M = [[np.NaN for x in range(num_teams - 1)] for x in range(num_games - 1)]
        # y = [np.NaN for x in range(num_games - 1)]
        M = np.array(M)
        y = np.array(y)
        # print(np.dot(M.T,M))
        # print(np.dot(M.T,y))
        r = np.linalg.lstsq(M,y)[0]
        np.round(r,2,r)
        print(r)
        team_list = {'team_name': None , 'team_rating': None}
        for team in teams:
            # TODO: associate team with team name

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        raise Exception

if __name__ == '__main__':
    main(sys.argv)
import csv
import os
from bs4 import BeautifulSoup as bs
import re
import requests
league_id = input("Enter league ID (e.g. 943463): ")
league_name = input("Enter league name (e.g. Out of Your League): ")
teams = {}
season_start = input("Enter season start (e.g. 2012): ")
season_end = input("Enter season end (e.g. 2024): ")

class Team:
    def __init__(self, owner_id):
        self.team_name = ""
        self.owner = ""
        self.owner_id = owner_id
        self.wins = 0
        self.losses = 0
        self.ties = 0

def create_teams(season):
    owners_url = 'https://fantasy.nfl.com/league/' + league_id + '/history/' + season + '/owners'
    owners_page = requests.get(owners_url)
    owners_html = owners_page.text
    owners_page.close()
    owners_soup = bs(owners_html, 'html.parser')
    teamWraps = owners_soup.find_all('tr', class_ = re.compile('team-'))
    for teamWrap in teamWraps :
        team_id = teamWrap.attrs['class'][0].split('-')[1]   
        team_url = f"https://fantasy.nfl.com/league/943463/history/{season}/teamhome?teamId={team_id}"
        team_page = requests.get(team_url)
        team_html = team_page.text
        team_soup = bs(team_html, 'html.parser')
        team_page.close()
        # get owner and id
        owner = team_soup.find('span', class_ = re.compile('userId-'))
        owner_id = owner['class'][1].split('-')[1]
        team = Team(owner_id)
       # get team name and owner name
        team.team_name = teamWrap.find('a', class_ = 'teamName').text.strip()
        team.owner = teamWrap.find('td', class_ = 'teamOwnerName').text.strip()

        # get W-L-T
        record = team_soup.find('ul', class_ = 'teamStats').find_all('li')[1].find('span').text.split('-')
        team.wins = int(record[0])
        team.losses = int(record[1])
        team.ties = int(record[2])

        if owner_id not in teams:
            teams[owner_id] = team
        else:
            teams[owner_id].wins += team.wins
            teams[owner_id].losses += team.losses
            teams[owner_id].ties += team.ties   
            teams[owner_id].team_name = team.team_name

    return teams

for season in range(int(season_start), int(season_end) + 1):
    print(f'Loading season {season}')
    season = str(season)
    teams_all = create_teams(season)

path = './' + league_name + '-League-History/'
if not os.path.isdir(path) :
    os.mkdir(path)	

path = path + 'Range_Combined_Script/'
if not os.path.isdir(path): 
    os.mkdir(path)

with open(path + f'{season_start}-{season_end}.csv', 'w', newline='') as f :
    writer = csv.writer(f)
    writer.writerow(['Owner ID',
                     'Owner',
                     'Team Name',
                     'Wins', 'Losses',
                     'Losses',
                     'Ties']) #writes header as the first line in the new csv file
    for team in teams_all:
        writer.writerow([teams_all[team].owner_id,
                         teams_all[team].owner,
                         teams_all[team].team_name,
                         teams_all[team].wins,
                         teams_all[team].losses,
                         teams_all[team].ties])
    print(f'File saved to {path + f"{season_start}-{season_end}.csv"}')


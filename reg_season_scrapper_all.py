import csv
import os
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import requests
leagueID = str(943463)
league_name = 'Out of Your League'


class Team:
    def __init__(self, team_id):
        self.team_name = ""
        self.team_id = team_id
        self.owner = ""
        self.owner_id = ""
        self.rank = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.final_place = ""

def create_teams(season):
    owners_url = 'https://fantasy.nfl.com/league/' + leagueID + '/history/' + season + '/owners'
    owners_page = requests.get(owners_url)
    owners_html = owners_page.text
    owners_page.close()
    owners_soup = bs(owners_html, 'html.parser')
    teams = {}
    teamWraps = owners_soup.find_all('tr', class_ = re.compile('team-'))
    for teamWrap in teamWraps :
        team_id = teamWrap.attrs['class'][0].split('-')[1]   
        team = Team(team_id)
        team.team_name = teamWrap.find('a', class_ = 'teamName').text.strip()
        team.owner = teamWrap.find('td', class_ = 'teamOwnerName').text.strip()
        # get rank
        team_url = f"https://fantasy.nfl.com/league/943463/history/{season}/teamhome?teamId={team_id}"
        team_page = requests.get(team_url)
        team_html = team_page.text
        team_soup = bs(team_html, 'html.parser')
        team_page.close()
        team.rank = int(team_soup.find('ul', class_ = 'teamStats').find_all('li')[0].find('strong').text)
        # get W-L-T
        record = team_soup.find('ul', class_ = 'teamStats').find_all('li')[1].find('span').text.split('-')
        team.wins = int(record[0])
        team.losses = int(record[1])
        team.ties = int(record[2])
        #get final place
        team.final_place = team_soup.find('li', class_ = 'seasonResult').find('strong').text
        
        # get owner id
        owner = team_soup.find('span', class_ = re.compile('userId-'))
        if owner:
            team.owner_id = owner['class'][1].split('-')[1]
        teams[team_id] = team
                                   

    if not os.path.isdir('./' + league_name + '-League-History') :
        os.mkdir('./' + league_name + '-League-History')
	

    path = './' + league_name + '-League-History/' + season #the path of the folder where the weekly csv files are stored

    with open('./' + league_name +'-League-History/' + season + '.csv', 'w', newline='') as f :
        writer = csv.writer(f)
        writer.writerow(['Owner ID', 'Owner', 'Team ID', 'Team Name', 'Rank', 'Wins', 'Losses', 'Ties', 'Final Place']) #writes header as the first line in the new csv file
        for team in teams:
            writer.writerow([teams[team].owner_id, teams[team].owner, teams[team].team_id, teams[team].team_name, teams[team].rank, teams[team].wins, teams[team].losses, teams[team].ties, teams[team].final_place])
    return teams

for season in range(2012, 2024 + 1):
    print(season)
    season = str(season)
    teams = create_teams(season)



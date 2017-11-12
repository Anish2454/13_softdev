'''
Anish Shenoy
SoftDev1 pd 7
HW13 -- A RESTful Journey Skyward
2017-11-09
'''
from flask import render_template, Flask
import urllib2
import json
import random

app = Flask(__name__)
nasa_api_key = "E79xFj7MoBIAJ6CvVW50Q9VNrNxjrs2n5nLRRrpy"
nba_api_key = "5010b3883a104877bb7ab92cb6daa7f3"

def getData(url):
    temp = urllib2.Request(url, headers={'Ocp-Apim-Subscription-Key': nba_api_key})
    uresp = urllib2.urlopen(temp)
    #print uresp
    d = json.loads(uresp.read())
    #print d
    uresp.close()
    return d

@app.route("/")
def home():

    url1 = "https://api.nasa.gov/planetary/apod?api_key=" + nasa_api_key
    url2 = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=" + nasa_api_key
    d1 = getData(url1)
    d2 = getData(url2)
    #print d1
    #print d2
    title1 = d1['title']
    src1 = d1['url']
    desc1 = d1['explanation']
    rand_int = random.randint(0, 3)
    title2 = "Picture Taken By: " + d2['photos'][rand_int]['camera']['full_name']
    #print d2['photos'][rand_int]
    src2 = d2['photos'][rand_int]['img_src']
    desc2 = "Taken On: " + d2['photos'][rand_int]['earth_date']


    url_nba_team = "https://api.fantasydata.net/v3/nba/scores/JSON/AllTeams"
    teams = getData(url_nba_team)
    rand_int2 = random.randint(0, len(teams))
    team = teams[rand_int2]
    src3 = team.pop("WikipediaLogoUrl")
    url_nba_players = "https://api.fantasydata.net/v3/nba/stats/JSON/PlayerSeasonStats/2017"
    players = getData(url_nba_players)
    rand_int3 = random.randint(0, len(players))
    player = players[rand_int3]
    return render_template("template.html", title1 = title1, src1 = src1, desc1 = desc1, title2 = title2, src2 = src2, desc2 = desc2, team = team, src3 = src3, player = player)



if __name__ == '__main__':
    app.debug = True
    app.run()

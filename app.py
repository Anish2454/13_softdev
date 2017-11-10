from flask import render_template, Flask
import urllib2
import json
import random

app = Flask(__name__)
api_key = "E79xFj7MoBIAJ6CvVW50Q9VNrNxjrs2n5nLRRrpy"

def getDict(url):
    uresp = urllib2.urlopen(url)
    #print uresp
    d = json.loads(uresp.read())
    #print d
    return d

@app.route("/")
def home():
    url1 = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    url2 = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=" + api_key
    d1 = getDict(url1)
    d2 = getDict(url2)
    print d1
    print d2
    title1 = d1['title']
    src1 = d1['url']
    desc1 = d1['explanation']
    rand_int = random.randint(0, 3)
    title2 = "Picture Taken By: " + d2['photos'][rand_int]['camera']['full_name']
    #print d2['photos'][rand_int]
    src2 = d2['photos'][rand_int]['img_src']
    desc2 = "Taken On: " + d2['photos'][rand_int]['earth_date']
    return render_template("template.html", title1 = title1, src1 = src1, desc1 = desc1, title2 = title2, src2 = src2, desc2 = desc2)

if __name__ == '__main__':
    app.debug = True
    app.run()

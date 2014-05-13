# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Scraping François Hollande's public calendar
# -------------------

# <codecell>

from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import re
import lxml
from time import sleep
import random

Request("http://www.elysee.fr/Agenda").add_header('From:', "jag2296@columbia.edu")
connection = urlopen("http://www.elysee.fr/Agenda")
data = connection.read()
page_code = BeautifulSoup(data) 

url = page_code.find("script")
url = url.getText()
url = url[19:]
url = url[:-2]

Request(url).add_header('From:',"jag2296@columbia.edu")  

connection = urlopen(url)
data = connection.read()
page = BeautifulSoup(data)
minipage = page.find("div","post")
b = int(minipage.find("h1","post-title").getText().strip().split(" ")[-1])
minipage = minipage.find("ul","agenda-list")

day = []
time = []
event = []
year = []

while True:

    print url
    for a in minipage.find_all("li","agenda-list-week"):
        
        d = a.find("h3","day-title").getText().strip()
        
       
        for e in a.find_all("li","agenda-list-day"):
            
            t = ""
            try: t = e.find("span","time").getText().strip()
            except: pass
            
            w = ""
            try: w = e.find("p","title").getText().strip()
            except: pass
    
            print "Date:",d
            print "Time:",t
            print "What:",w
            print "Year", b
            
            day.append(d)
            event.append(w)
            time.append(t)
            year.append(b)
            
    nextlink = page.find("a","icon-arrow_r_wh")

    if nextlink and nextlink.attrs.has_key("href"):
        
        link = "http://www.elysee.fr/"+nextlink["href"]
        print link
        
        #sleep(random.randrange(0,1))
        connection = urlopen(link)
        data = connection.read()
        page = BeautifulSoup(data)
        minipage = page.find("div","post")
        b = int(minipage.find("h1","post-title").getText().strip().split(" ")[-1])
        minipage = minipage.find("ul","agenda-list")

        
    else: break

# <codecell>

import pandas
calendar = pandas.DataFrame({"day":day, "year":year, "time":time,"event":event})
calendar
shape(calendar)

# <codecell>

calendar["date"] = calendar["day"]+" "+str(calendar["year"])

# <codecell>

for i in range(len(calendar["day"])): 
    calendar["date"][i] = calendar["day"][i]+" "+str(calendar["year"][i])

# <codecell>

women = calendar[calendar["event"].str.match(".*Mme\.*.")]
women_count = women.shape[0]
women_count

# <codecell>

men = calendar[calendar["event"].str.match(".*M\.*.")]
men_count = men.shape[0]

# <codecell>

from re import sub, match, findall
VALLS = calendar[calendar["event"].str.match(".*VALLS.*")]
VALLS["event"].value_counts()

# <codecell>

calendar["date"].value_counts()

# <codecell>

calendar["date"].value_counts().mean()

# <codecell>

calendar["year"].value_counts()

# <codecell>

from time import time
from flask import Flask, request, make_response, render_template
from string import Template

# Create an application object

app = Flask("François Hollande calendar")

def frequency():
    
    import datetime
    import StringIO
    import random
 
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    import matplotlib.pyplot as plt
    from matplotlib.dates import DateFormatter
 
    fig=plt.figure()
    
    fig.add_subplot(1,1,1)
    calendar["date"].value_counts(sort=False).plot(figsize=[20,5])
    
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

def gender(): 
    
    import datetime
    import StringIO
    import random
 
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    import matplotlib.pyplot as plt
    from matplotlib.dates import DateFormatter
 
    fig=plt.figure(figsize=[10,10])
    
    sub = fig.add_subplot(1,1,1)
    labels = "percentage of women", "percentage of men"
    fracs = [women_count, men_count]
    colors = "red","white"
    sub.pie(fracs, labels=labels, colors=colors)
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

app.add_url_rule("/gender",view_func=gender)
app.add_url_rule("/hollande",view_func=Hollande) 
app.add_url_rule("/frequency",view_func=frequency)

app.run('0.0.0.0',9800)

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>

 

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>



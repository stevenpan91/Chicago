from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import csv
from datetime import datetime
import numpy as np 

import plotly.plotly as py 
import plotly.graph_objs as go 
from sepdata import ChiData
import math
import ephem

sun = ephem.Sun()
observer = ephem.Observer()

ChiData1=ChiData('ChicagoCrimes2001-now.csv',1,math.inf,5,"Homicide")

categories=[]
counter=[]


for iter1 in range(len(ChiData1.Date)):
    observer.lat, observer.lon, observer.elevation = ChiData1.Latitude[iter1], ChiData1.Longitude[iter1], 181 #181 m elev
    observer.date=ChiData1.Date[iter1]
    sun.compute(observer)
    sunangle=sun.alt*180/math.pi
    #print(sunangle)
    nightday=""
    if(sunangle<-6):
        nightday="night"+ChiData1.LocationDesc[iter1]
    else:
        nightday="day"+ChiData1.LocationDesc[iter1]
    if nightday not in categories:
        categories.append(nightday)
        counter.append(1)
    else:
        counter[categories.index(nightday)]+=1

data = [go.Bar(
            x=categories,
            y=counter
    )]

plot(data,filename='NightDayBarChartHomicide.html')

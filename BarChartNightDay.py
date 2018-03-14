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

ChiData1=ChiData('ChicagoCrimes2001-now.csv',1,math.inf)

categories=[]
counter=[]

for nightday in ChiData1.Date:
    observer.lat, observer.lon, observer.elevation = '48.730302', '9.149483', 400

    if crimetype not in categories:
        categories.append(crimetype)
        counter.append(1)
    else:
        counter[categories.index(crimetype)]+=1

data = [go.Bar(
            x=categories,
            y=counter
    )]

plot(data,filename='NightDayBarChart.html')

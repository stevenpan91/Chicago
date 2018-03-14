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


ChiData1 = ChiData('ChicagoCrimes2001-now.csv',1,math.inf,5,"Homicide")

categories=[]
counter=[]

for block in ChiData1.Block:
    tempstring=""
    for c in range(len(block)):
        if c>5:
            tempstring+=block[c]
    if tempstring not in categories:
        categories.append(tempstring)
        counter.append(1)
    else:
        counter[categories.index(tempstring)]+=1

data = [go.Bar(
            x=categories,
            y=counter
    )]

plot(data,filename='HomicideBlockBarChart.html')

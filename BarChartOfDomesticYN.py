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

for domestic in ChiData1.LocationDesc:
    if domestic not in categories:
        categories.append(domestic)
        counter.append(1)
    else:
        counter[categories.index(domestic)]+=1

data = [go.Bar(
            x=categories,
            y=counter
    )]

plot(data,filename='DomesticYNHomicideBarChart.html')

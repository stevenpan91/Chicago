from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import csv
from datetime import datetime

import plotly.plotly as py 
import plotly.graph_objs as go 
import numpy as np 

#print (__version__)

ID, CaseNum, Date, Block, IUCR, PrimaryType, Desc, LocationDesc=([] for i in range(8))
Arrest, Domestic, Beat, District, Ward, Community, FBICode, XCoord=([] for i in range(8))
YCoord, Year, UpdatedOn, Latitude, Longitude, Location=([] for i in range(6))

with open('ChicagoCrimes2001-now.csv','r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    next(reader)
    counter=0
    for row in reader:
        counter+=1
        if counter<=10:
        #if True:
            ID.append(row[0])
            CaseNum.append(row[1])
            Date.append(datetime.strptime(row[2],'%m/%d/%Y %H:%M:%S %p'))
            #print (', '.join(row))
        else:
            break

        print(row)

#data=[go.Histogram(x=Date)]


#print(ID)
#print(CaseNum)
#print(Date)

#plot(data)
#plot([Scatter(x=[1,2,3],y=[3,1,6])])
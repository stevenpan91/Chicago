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

def quicksort(A,lo,hi):
    if lo<hi:
        p = partition(A,lo,hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)


def partition(A,lo,hi):
    pivot = A[hi]
    i=lo-1
    for j in range (lo, hi):
        if(A[j]<pivot):
            i+=1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp

    if (A[hi]<A[i+1]):
        temp=A[i+1]
        A[i+1]=A[hi]
        A[hi]=temp

    return i+1

ChiData1 = ChiData('ChicagoCrimes2001-now.csv',1,math.inf,5,"Homicide")

#coord of Chicago
layout = {
    'xaxis': {
        'range': [-87.978706, -87.497368]
    },
    'yaxis': {
        'range': [41.613081, 42.043378]
    },
    'shapes': [
        # Line Vertical
        {
            'type': 'line',
            'x0': -87.709337,
            'y0': 42.019040,
            'x1': -87.674633,
            'y1': 42.019040,
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 3,
                'dash': 'dashdot'
            },
        },
        # Line Horizontal
        {
            'type': 'line',
            'x0': -87.800942,
            'y0': 41.797998,
            'x1': -87.800942,
            'y1': 41.774466,
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 3,
                'dash': 'dashdot',
            },
        },
        # Line Diagonal
        {
            'type': 'line',
            'x0': -87.616735,
            'y0': 41.644731,
            'x1': -87.524259,
            'y1': 41.644731,
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 3,
                'dash': 'dashdot',
            },
        },
    ]
}

#the_array=Date
#print(the_array)
#quicksort(the_array,0,len(the_array)-1)
#print(the_array)

#data=[go.Histogram(x=the_array)]

#plot(data)

# Create a trace
trace = go.Scatter(
    x = ChiData1.Longitude,
    y = ChiData1.Latitude,
    mode = 'markers'
)

data=[trace]

fig={
    'data':data,
    'layout':layout,

}

plot(fig,filename='LongLatChicagoHomicides.html')

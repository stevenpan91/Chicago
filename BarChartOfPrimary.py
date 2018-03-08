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



ChiData1=ChiData('ChicagoCrimes2001-now.csv',1,math.inf)

categories=[]
counter=[]

for crimetype in ChiData1.PrimaryType:
    if crimetype not in categories:
        categories.append(crimetype)
        counter.append(1)
    else:
        counter[categories.index(crimetype)]+=1

data = [go.Bar(
            x=categories,
            y=counter
    )]

plot(data,filename='PrimaryTypeBarChart.html')

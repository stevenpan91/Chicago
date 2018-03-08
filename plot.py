from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import csv
from datetime import datetime

import plotly.plotly as py 
import plotly.graph_objs as go 
import numpy as np 
from sepdata import ChiData
import math


ChiData1 = ChiData('ChicagoCrimes2001-now.csv',1,math.inf)

data=[go.Histogram(x=ChiData1.Date)]

plot(data)
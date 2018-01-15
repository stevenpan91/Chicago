import csv
from datetime import datetime
import numpy as np 

def quicksort(A,lo,hi):
    if （lo<hi):
        p = partition(A,lo,hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def partition(A,lo,hi):
    pivot = A[hi]
    i=lo-1
    



ID, CaseNum, Date, Block, IUCR, PrimaryType, Desc, LocationDesc=([] for i in range(8))
Arrest, Domestic, Beat, District, Ward, Community, FBICode, XCoord=([] for i in range(8))
YCoord, Year, UpdatedOn, Latitude, Longitude, Location=([] for i in range(6))

with open('ChicagoCrimes2001-now.csv','r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    next(reader)
    counter=0
    for row in reader:
        counter+=1
        if counter<=100000:
        #if True:
            ID.append(row[0])
            CaseNum.append(row[1])
            Date.append(datetime.strptime(row[2],'%m/%d/%Y %H:%M:%S %p'))
            #print (', '.join(row))
        else:
            break
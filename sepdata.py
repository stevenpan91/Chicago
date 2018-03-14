#separate csv data into multiple arrays
#Steven Pan

import math
import csv
from datetime import datetime
import re

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

class ChiData:

    def __init__(self,filename,startpoint=1,pointcount=math.inf,condition_index=None,condition=""):
        self.ID, self.CaseNum, self.Date, self.Block, self.IUCR, self.PrimaryType, self.Desc, self.LocationDesc=([] for i in range(8))
        self.Arrest, self.Domestic, self.Beat, self.District, self.Ward, self.Community, self.FBICode, self.XCoord=([] for i in range(8))
        self.YCoord, self.Year, self.UpdatedOn, self.Latitude, self.Longitude, self.Location=([] for i in range(6))

        with open(filename,'r') as csvfile:
            reader=csv.reader(csvfile, delimiter=',')
            next(reader)
            counter=0
            for row in reader:
                counter+=1
                if counter>=startpoint and counter<startpoint+pointcount:
                #if counter<=1000:
                #if True:
                    if condition_index==None or (re.search(condition,row[condition_index],re.IGNORECASE)):
                        self.ID.append(row[0])
                        self.CaseNum.append(row[1])
                        self.Date.append(datetime.strptime(row[2],'%m/%d/%Y %H:%M:%S %p'))
                        self.Block.append(row[3])
                        self.IUCR.append(row[4])
                        self.PrimaryType.append(row[5])
                        self.Desc.append(row[6])
                        self.LocationDesc.append(row[7])
                        self.Arrest.append(row[8])
                        self.Domestic.append(row[9])
                        self.Beat.append(row[10])
                        self.District.append(row[11])
                        self.Ward.append(row[12])
                        self.Community.append(row[13])
                        self.FBICode.append(row[14])
                        self.XCoord.append(row[15])
                        self.YCoord.append(row[16])
                        self.Year.append(row[17])
                        self.UpdatedOn.append(datetime.strptime(row[18],'%m/%d/%Y %H:%M:%S %p'))
                        self.Latitude.append(row[19])
                        self.Longitude.append(row[20])
                        self.Location.append(row[21])
                        #print (', '.join(row))
                else:
                    break

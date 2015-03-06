import csv
import urllib
from pandas import *
import numpy
#import tables
#Tables/pytables is needed for HDFStore (Python's data store) to operate, however,
#because of installing error, tables cannot be imported.

#The following function pulls NHS data for each of a year and store it in HDFStore
#This is important as a machine's memory is not enough to process data of such a size.
def storingdata(datalocation,monthyear):
    monthyear = HDFStore('file.h5')
    for chunk in read_csv(datalocation,chunksize = 10 ** 5):
        monthyear.append(chunk)

#The following is repeated 52 times starting from November 2014 all the way back to August 2010. Due to the iteration nature, I have included request to pull it twice.
#A function could be built to store data automatically with the use of Python function and calender, however due to time limitation I have refrained from doing so.
storingdata(http://datagov.ic.nhs.uk/presentation/2014_11_November/T201411PDPI+BNFT.CSV,nov14)
storingdata(http://datagov.ic.nhs.uk/presentation/2014_01_January/T201401PDPI+BNFT.CSV,oct14)

#The following code is used to remove the columns that are not needed for our purpose
allmonths = [aug10,sept10,oct10,...,nov14]
for data in allmonths:
    data.drop('')
    DF.drop(['SHA','PCT','PRACTICE','BNF CODE','NIC','ACT COST'], 1)

#the function below obtains the rows that only contains the values. We are specifically interested in Methylphenidate,atomoxetine, dexamfetamine, lisdexamfetamin.

def rows_extraction(monthyear, key, value):
    return df[df[key] == value]
medicines = ['Dexamfet Sulf','methylphenidate','dexamfetamine','lisdexamfetamine']    
for month in allmonths:
    for med in medicines: #Note it requires the full names of medicines with mg but as time is limited I haven't included any
        month.rows_extraction('BNF NAME',med)


"""I am not able to finish this code. However, if I had time, I would have plotted a time series plot to obtain a general plot. I hope this will
show if we have an increasing or decreasing treand.
From there we can answer our question whether ADHD prescriptions are increasing or decreasing."""




    




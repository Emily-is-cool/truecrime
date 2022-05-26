# truecrime
##SPD crime data Jan 1 - May 13, 2022

Just messing around with the bare basics here.
The data file is taken from Seattle.gov/police/information-and-data/public-data-sets
and is the 911 incident response csv file. 

https://data.seattle.gov/Public-Safety/Call-Data/33kz-ixgy
The following are examples of code and the data it produced. Much of this was done on the full .csv file. The portion in the .csv file loaded here is only this year's data for managability reasons. 

##Column names:

print('column names: ', column_names)
Column Names Are:  ['Event Clearance Description', 'Call Type', 'Priority', 'Initial Call Type', 'Final Call Type', 'Original Time Queued', 'Arrived Time', 'Precinct', 'Sector', 'Beat']
<class 'pandas.core.frame.DataFrame'>
##Call Data Info:

print(calldata.info())

 0   CAD Event Number             int64
 1   Event Clearance Description  object
 2   Call Type                    object
 3   Priority                     int64
 4   Initial Call Type            object
 5   Final Call Type              object
 6   Original Time Queued         object
 7   Arrived Time                 object
 8   Precinct                     object
 9   Sector                       object
 10  Beat                         object
dtypes: int64(2), object(9)

##This is the totals given for each type of call in the final call type:

print(calldata.groupby('Final Call Type') ['Final Call Type'].count())
Final Call Type
--ALARM-COMM (INC BANK, ATM, SCHOOLS, BSN)         72096
--ALARM-COMM ROBB (BANK, PANIC, DURESS)             7087
--ALARM-OTHER (VARDA,PDT,FIRE,LOCAL,METRO,ETC))     3287
--ALARM-RESIDENTIAL BURG                           62492
--ALARM-RESIDENTIAL PANIC OR DURESS                 7032
                                                   ...
WARRANT PICKUP - FROM OTHER AGENCY                    70
WATER FLOODS (BROKEN MAINS/HYDRANTS, NO HAZ)          30
WEAPN - GUN,DEADLY WPN (NO THRTS/ASLT/DIST)          507
WEAPN-IP/JO-GUN,DEADLY WPN (NO THRT/ASLT/DIST)       281
WIRES DOWN (PHONE, ELECTRICAL,ETC.)                  148
Name: Final Call Type, Length: 428, dtype: int64

##This is just for the purpose of seeing how the time data was displayed:
print(calldata['Original Time Queued'].head(10))
0    07/30/2013 09:05:36 PM
1    06/08/2020 09:10:46 AM
2    07/01/2011 10:01:37 AM
3    11/09/2011 09:52:24 AM
4    10/22/2011 10:32:03 PM
5    09/19/2011 08:16:46 AM
6    05/21/2013 08:48:07 AM
7    04/14/2012 08:57:28 PM
8    10/31/2011 10:36:17 AM
9    08/15/2012 07:45:51 AM
Name: Original Time Queued, dtype: object

##Seeing how many calls there were of each priority: 
print(calldata.groupby('Priority') ['Priority'].count())
Priority
-1        644
 1     582074
 2    1123412
 3    1608619
 4     144797
 5     122029
 6      38401
 7    1086046
 8          4
 9     211498
Name: Priority, dtype: int64

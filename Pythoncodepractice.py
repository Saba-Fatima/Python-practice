ydict = {
  "kind": "youtube#searchListResponse",
  "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/PaiEDiVxOyCWelLPuuwa9LKz3Gk\"",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/QpOIr3QKlV5EUlzfFcVvDiJT0hw\"",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/AWutzVOt_5p1iLVifyBdfoSTf9E\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "Eqa2nAAhHN0"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/2dIR9BTfr7QphpBuY3hPU-h5u-4\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "IirngItQuVs"
      },
     "movies":["ddlj","mnik","ff"]
    }
  ]
}
for i in ydict:
   if isinstance(i,str) and (i == "etag"):
       print(ydict["etag"])
   if isinstance(ydict[i],list):
       for j in ydict[i]:
           print(j["etag"])
   if "movies" in j:
        print(j["movies"])
		
---------files
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:00:09 2019

@author: demopc
"""

"""fobj = open("D:temp.txt","w")
fobj.write("p programming\n")
fobj.close()"""


"""with open("D:temp.txt","w") as fobj:
    fobj.write("some sample text")"""
    
with open("D:temp.txt","r") as fobj:
    for i in fobj:
        print(i)
-----files2-----------------
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:00:09 2019

@author: demopc
"""

"""fobj = open("D:temp.txt","w")
fobj.write("p programming\n")
fobj.close()"""


"""with open("D:temp.txt","w") as fobj:
    fobj.write("some sample text")"""
    
with open("D:temp.txt","r") as fobj:
    for i in fobj:
        i=i.strip()
        print(i)
        
try:        
     with open("C:\\Users\\demopc\\Downloads\\Sacramentorealestatetransactions.csv","r") as fobjec:
          for i in fobjec:
              print(i)
except FileNotFoundError as error:
    print("file not found exception..please check")
    print("file not found exception",error)              
except ValueError as error:
    print("invalid input... please check")
    print("invalid input",error)    
except TypeError as error:
    print("operation error")
    print("operation error",error)
------------file3--------------------------------------
# -*- coding: utf-8 -*-
import csv
"""
Created on Thu Oct 24 12:00:09 2019

@author: demopc
"""

"""fobj = open("D:temp.txt","w")
fobj.write("p programming\n")
fobj.close()"""

-----------------file4------------------------------------------
# -*- coding: utf-8 -*-
import csv
"""
Created on Thu Oct 24 12:00:09 2019

@author: demopc
"""

"""fobj = open("D:temp.txt","w")
fobj.write("p programming\n")
fobj.close()"""


"""with open("D:temp.txt","w") as fobj:
    fobj.write("some sample text")"""
    
    
fobj=open("C:\\Users\\demopc\\Downloads\\Sacramentorealestatetransactions.csv","r")
reader=csv.reader(fobj)
for line in reader:
    print(line[0])
        
    
    
    
"""with open("D:temp.txt","r") as fobj:
    for i in fobj:
        i=i.strip()
        print(i)
        
try:        
     with open("C:\\Users\\demopc\\Downloads\\Sacramentorealestatetransactions.csv","r") as fobjec:
         lst = []
         
         for i in fobjec:
             print(i.split(',')[0]+""+i.split(',')[1])        
             print(i.split(',')[0])
             lst.append(i.split(',')[1])
             print(set(lst))      
     
             
                 
except FileNotFoundError as error:
    print("file not found exception..please check")
    print("file not found exception",error)              
except ValueError as error:
    print("invalid input... please check")
    print("invalid input",error)    
except TypeError as error:
    print("operation error")
    print("operation error",error)    """

              
*************************Functions**********************************************************
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:49:46 2019

@author: demopc
"""
#fixed args
def dispaly(first,sec):
    print(first,sec)
display(10,20) 


#default args
def dispaly(first=1,sec=2,third='default'):
    print(first,second,third)
display()
display(10)
display(10,20)
display(10,20,30)    

#keyword args
def dispaly(first,sec):
    print(first,sec)
display(first=10,sec=40)

#variable length args
"""single star refers to a tuple"""
def dislay(*info):
    for val in info:
        print(val)
display(10,20,30,"unix")  

"""double star refers to a dictionary"""
def display(**var):
    print(var)
display(chap1="saba",chap2="fatima")      
        


"""with open("D:temp.txt","w") as fobj:
    fobj.write("some sample text")"""
    
with open("D:temp.txt","r") as fobj:
    for i in fobj:
        i=i.strip()
        print(i)
        
try:        
     with open("C:\\Users\\demopc\\Downloads\\Sacramentorealestatetransactions.csv","r") as fobjec:
         
         for i in fobjec:
             print(i.split(',')[0]+""+i.split(',')[1])        
             
                 
except FileNotFoundError as error:
    print("file not found exception..please check")
    print("file not found exception",error)              
except ValueError as error:
    print("invalid input... please check")
    print("invalid input",error)    
except TypeError as error:
    print("operation error")
    print("operation error",error)    

-------------files5----------------------------------------

import os
import getpass
import calendar
from os import makedirs	
from datetime import datetime

"""for root, dirs, files in os.walk("D:\\"):
    for filename in files:
        print(filename)
   
for files in os.get_terminal_size():
          print(files)"""
          
print(getpass.getuser())
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)


dateTimeObj = datetime.now()
print(dateTimeObj)
print ("The calender of year 2019 is : ") 
print (calendar.calendar(2019,1,0,2,4)) 
print(os.getpid())
print(dir_path)
"""directory = "my first directory"
parent_dir = "D:\\"
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
print("Directory '%s' created" %directory) """
for count in range (1,100):
    var=os.makedirs("C:\\Users\\demopc\\Downloads".format(count))
    print(var)

"""for count in range (1, 100):
    os.makedirs("D:\\DirecFold".format(count))"""
    
          
          
----------------------------------REST-------------------------------------------------
import requests

response = requests.get('https://www.google.com/');

print(response)
              
    
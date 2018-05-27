import csv
import collections
from datetime import datetime
from datetime import timedelta
import sys
fmt = '%Y-%m-%d %H:%M:%S'

output=open(sys.argv[3],'a')

input_period = open(sys.argv[2])
period=input_period.read()


with open(sys.argv[1]) as input:
     reader = csv.reader(input,delimiter=',')
    
     next(reader,None)
     dictionary = collections.OrderedDict()
     
     for row in reader:
         #print row
         ip = row[0]
         date = row[1]+' '+row[2]
         
         for key in dictionary.keys():
             lis = dictionary[key]
             tstamp1 = datetime.strptime(lis[-1],fmt)
             
             tstamp2 = datetime.strptime(date,fmt)
             difference = tstamp2-tstamp1
             td_seconds = int(round(difference.total_seconds()))
                       
            
               
 
             if(td_seconds>=(int(period)+1)):                
                start = datetime.strptime(lis[0],fmt)
                end = datetime.strptime(lis[-1],fmt)
                start_end = end - start
                duration_second = 1+int(round(start_end.total_seconds()))
                count_webpage = len(lis)
                output.write(key + ',' + lis[0]+','+lis[-1]+','+str(duration_second)+','+str(count_webpage)+'\n')
                
#                print key + ',' + lis[0]+','+lis[-1]+','+str(duration_second)+','+str(count_webpage)+'\n'
                del dictionary[key]            
             
                
            
         dictionary.setdefault(ip,[]).append(date)
     for key in dictionary.keys():
       lis2 = dictionary[key]
       start2 = datetime.strptime(lis2[0],fmt)
       end2 = datetime.strptime(lis2[-1],fmt)
       start2_end2 = end2 - start2
       duration_second2 = 1+int(round(start2_end2.total_seconds()))
       count_webpage2 = len(lis2)
       output.write(key + ',' + lis2[0] +','+ lis2[-1] + ',' + str(duration_second2)+','+str(count_webpage2)+'\n')
         
 #      print key + ',' + lis2[0] +','+ lis2[-1] + ',' + str(duration_second2)+','+str(count_webpage2)+'\n'
           
     
    
         
       

     
     


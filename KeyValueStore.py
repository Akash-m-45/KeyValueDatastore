import threading 
from threading import*
import time

d={} #'d' is the dictionary in which we will store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" or "create(key_name,value)"

def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error type1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error type2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error type3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error type4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error type4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error type5
        else:
            del d[key]
            print("key is successfully deleted")
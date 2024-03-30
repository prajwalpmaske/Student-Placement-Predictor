from model.Prediction import *

def get_result(res):

    # Branch
    if(res[0]== "EXTC"):
        res[0] = 2
    elif(res[0] == "COMPUTER"):
        res[0] = 0
    elif(res[0]=="IT"):
        res[0] = 3
    elif(res[0] =="INSTRUMENTATION"):
        res[0] = 4
    else:
        res[0] = 1

    # 10th
    if(res[1]<=50 and res[1]>=0):
        res[1] = 0
    
    elif(res[1]>50 and res[1]<=75):
            res[1] = 1
    
    elif(res[1]>75 and res[1]<=100):
        res[1] = 2

    # 12th
    if(res[-4]<=50 and res[-4]>=0):
        res[-4] = 0
    
    elif(res[-4]>50 and res[-4]<=75):
            res[-4] = 1
    
    elif(res[-4]>75 and res[-4]<=100):
        res[-4] = 2

    #Diploma
    if(res[-3]<=50 and res[-3]>=0):
        res[-3] = 0
    
    elif(res[-3]>50 and res[-3]<=75):
        res[-3] = 1
    
    elif(res[-3]>75 and res[-3]<=100):
        res[-3] = 2
    
    #Gap
    if(res[-6] == 0):
        res[-6] = 0
    else:
        res[-6] = 1

    #Aptitude
    if(res[-5]>12):
        res[-5]=1
    else:
        res[-5]=0

    return predictStatus(res)

def get_result2(res):

    # Branch
    if(res[0]== "EXTC"):
        res[0] = 2
    elif(res[0] == "COMPUTER"):
        res[0] = 0
    elif(res[0]=="IT"):
        res[0] = 3
    elif(res[0] =="INSTRUMENTATION"):
        res[0] = 4
    else:
        res[0] = 1

    # 10th
    if(res[1]<=50 and res[1]>=0):
        res[1] = 0
    
    elif(res[1]>50 and res[1]<=75):
            res[1] = 1
    
    elif(res[1]>75 and res[1]<=100):
        res[1] = 2

    # 12th
    if(res[-4]<=50 and res[-4]>=0):
        res[-4] = 0
    
    elif(res[-4]>50 and res[-4]<=75):
            res[-4] = 1
    
    elif(res[-4]>75 and res[-4]<=100):
        res[-4] = 2

    #Diploma
    if(res[-3]<=50 and res[-3]>=0):
        res[-3] = 0
    
    elif(res[-3]>50 and res[-3]<=75):
        res[-3] = 1
    
    elif(res[-3]>75 and res[-3]<=100):
        res[-3] = 2
    
    return predictSalary(res)
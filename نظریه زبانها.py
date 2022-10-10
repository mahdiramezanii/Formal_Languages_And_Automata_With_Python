
#========================================= Import libraries ===============================================

import random

#=========================================      Variables    =====================================================

L1=input("enter L1: ")
L2=input("enter L2: ")

number=["1","2","3","4","5","6","7","8","9","10","n","q","w","e","r","t","y","u","i","o","p","s","d","f","g","h","j","k","l","z","x","c","v","m"]

number_2="12345678910"

string="qwertyuioplkjhgfdsazxcvbnm"

data="ab"

power_l1=[]
power_l2=[]

string_l1=[]
string_l2=[]

#condition language
condition_l1=""
condition_l2=""


l1={}
l2={}

l1_for_division=""
l2_for_division=""

number_condition_l1={}
number_condition_l2={}

result_l1=[]
result_l2=[]

final_result_l1=[]
final_result_l2=[]

#========================================= End Variables =====================================================

#==========================================     L1       =====================================================

for i in range(len(L1)):
    
    if L1[i] in number:
        
        power_l1.append(L1[i])
        
        
    elif L1[i] in data:
        string_l1.append(L1[i])
        
    elif L1[i] == ":":
        
        for j in range(i+1,len(L1)):
            
            condition_l1+=L1[j]
        
        break 
    
       
for i in string_l1:
    
    for j in power_l1:
        
        l1[i]=j
        power_l1.remove(j)
        break
#==========================================    End L1       =====================================================

#==========================================      L2         =================================================       
     
for i in range(len(L2)):
    
    if L2[i] in number:
        
        power_l2.append(L2[i])
        
    elif L2[i] in data:
        string_l2.append(L2[i])
        
    elif L2[i] == ":":
        
        for j in range(i+1,len(L2)):
            
            condition_l2+=L2[j]
            
        break
    
for i in string_l2:
    
    for j in power_l2:
        
        l2[i]=j
        power_l2.remove(j)
        break        

#==========================================    End L2       =====================================================

#===================================== Generating random language strings L2 =================================

#copy l2 for Generate multiple random strings for language
copy_l2=l2.copy()


for string,power in l2.items():
    
    
    if power in number_2:
        
        l2_for_division+=(string*int(power))
        
        #============== String To List L2 ==============
        
        result_l2.append(l2_for_division)
        
        
    else:
        
        for i in range(len(condition_l2)):
            
            
            if (condition_l2[i] in "qwertyuioplkjhgfdsazxcvbnm"):
                
                if ((i+1) < len(condition_l2)):
                
                    number_condition_l2[condition_l2[i]]=condition_l2[i+2]
        
        
        
        for k,v in number_condition_l2.items():
            
            
            for key,value in copy_l2.items():
                
                
                if value==k:
                    
                    #Generate multiple random strings for language
                    for i in range((random.randint(int(v),5)),random.randint(int(v),10)):
                        
                        for j in range(3):
                        
                            #result_l2.append(key*(i+(random.randint(0,2))))
                            result_l2.append(key*(i+j))
                        
                        break
                        
                    copy_l2.pop(key)
                    
                break
#===================================== End Generating random language strings L2 =================================
                        
#=====================================  Generating random language strings L1 =================================

#copy l1 for Generate multiple random strings for language
copy_l1=l1.copy()


for string,power in l1.items():
    
    if power in number_2:
        
        l1_for_division+=(string*int(power))
        
        
        #============== String To List L1 ==============
        
        result_l1.append(l1_for_division)
        
        
    else:
        
        for i in range(len(condition_l1)):
            
            
            if (condition_l1[i] in "qwertyuioplkjhgfdsazxcvbnm"):
                
                if ((i+1) < len(condition_l1)):
                
                    number_condition_l1[condition_l1[i]]=condition_l1[i+2]
        
            
        for k,v in number_condition_l1.items():
            
            for key,value in copy_l1.items():
                
                
                if value==k:
                    
                    
                    #Generate multiple random strings for language
                    for i in range((random.randint(int(v),5)),random.randint(int(v),10)):
                        
                        
                        for j in range(3):
                        
                            #result_l1.append(key*(i))
                            result_l1.append(key*(i+j))
                        
                        break
                        
                    copy_l1.pop(key)
                    
                break
            
#===================================== End Generating random language strings L1 =================================


#=====================================            Create Final Result L1           ============================
                           
for i in range(0,len(result_l1)//2):
    
    final_result_l1.append(result_l1[i])
    
j=0

for i in range(len(result_l1)//2,len(result_l1)):
    
    while j < len(final_result_l1):
    
        final_result_l1[j]+=(result_l1[i])
        
        j=j+1
        break
    
#=====================================           End Create Final Result L1         ============================
                                    
#=====================================            Create Final Result L2           ============================
                           
for i in range(0,len(result_l2)//2):
    
    final_result_l2.append(result_l2[i])
    
j=0

for i in range(len(result_l2)//2,len(result_l2)):
    
    while j < len(final_result_l2):
        
        final_result_l2[j]+=(result_l2[i])
        
        j=j+1
        break
    
#=====================================         End Create Final Result L2         ============================
        
#=======================================              END                     ==========================
 
print("l2: ",final_result_l2)
print("l1: ",final_result_l1)

#========================================             End                         =========================


#===================================    Random strings made from input languages    =============================
L1=["ab","aabb","aabb","aaab"]
L2=['b','b','bb',"b"]
l1=[]
l2=[]
#===================================  End  Random strings made from input languages  =============================
result=[]
#===================================           Start the division operation          ==========================               

for i in range(len(final_result_l1)):  
    
    #===== Constructing a string of randomly generated strings   ====
    for i in final_result_l1:
        for j in i:
            l1.append(j)
        final_result_l1.remove(i)
        break
    

    for i in final_result_l2:
        for j in i:
            l2.append(j)
        final_result_l2.remove(i)
        break  

    #===== End Constructing a string of randomly generated strings ====
    
    #====================================== Variables ==================================================
    
    data=[]
    data.extend(l1)
    data.extend(l2)

    flag=True
    flag_del=True
    siz=0
    
    #====================================== End Variables ==================================================

    while siz != len(l1)-1:
    
        flag_del=True
    
        for j in data:
        
            flag_del=True
        
            for k in l2:
                flag_del=True
            
            
                if (j + k == l1) or (j + "" == l1[siz]):
                
                    if flag==True:
                        result.append(j)
                    
                        if (j + "" in l1[siz]) or (k + "" in l1[siz]):
                        
                            l1.remove(l1[siz])
                            flag_del=False
                        
                
                    if j+k == l1:
                        flag=False 
                
                if flag==False:
                    break
            
                if flag_del==False:
                    break
            
            if flag==False:
                break
        
            if flag_del==False:
                    break
            
        if flag_del==False:
            continue
    
            siz=siz+1
            
    #Clear strings for new values     
    l1.clear()
    l2.clear()   

#============================================== End ======================================
             
#The result of dividing L1 and L2
L1_L2={
    "a":0,
    "b":0
}

for item in result:
     

    L1_L2[item]+=1
    
     
print("L1/L2: ",L1_L2)    
    
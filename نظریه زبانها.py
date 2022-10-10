l1=["a","b","a","a"]
l2=["a"]

data=[]
data.extend(l1)
data.extend(l2)

result=[]

flag=True
flag_del=True
siz=0

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
        
print(l1)
print(flag)              
print(result)
                
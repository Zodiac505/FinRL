import os
with open('p2.txt','r') as f:
    for i,line in enumerate(f.readlines()):
        if i > -1:
            print("*"*20,i,line,"*"*20,sep='\n')
            os.system(line)

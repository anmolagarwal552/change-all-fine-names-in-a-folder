import os 

path = os.chdir("C:\\Users\\Desktop") #change path before running the code

i = 0

for file in os.listdir(path):
    
    new_file_name = "pic{}.PNG".format(i) #change extension accordingly 
    
    os.rename(file, new_file_name)
    
    i = i+1

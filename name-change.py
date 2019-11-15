import os 

path = os.chdir("C:\\Users\\") #change the path

i = 0

for file in os.listdir(path):
    
    new_file_name = "pic{}.PNG".format(i) #change extension before using code
    
    os.rename(file, new_file_name)
    
    i = i+1

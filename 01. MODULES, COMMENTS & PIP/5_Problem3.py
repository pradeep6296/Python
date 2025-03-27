# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

# Select the directory whose content you want to list
directory_path ='/'
 
# Use the os module to list the directory content 
contents = os.listdir(directory_path)
 
#  Print the content of the  directory
print(contents)
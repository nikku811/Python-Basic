# 5. Label the program written in problem 4 with comments.
import os

#Select the directroy whose content you want to list
path = './'

#use the os module to list the directroy content
contents = os.listdir(path)

#print the content of directroy
print(contents)
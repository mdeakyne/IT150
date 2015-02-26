__author__ = 'Matthew'
import os,subprocess

student_dir = "C:\\Users\\Matthew\\Dropbox\\IT 150\\ToGrade\\Labs-Lab_2\\"
print student_dir

for dir, subdir, files in os.walk(student_dir):
    for file in files:
        print file
        execfile(dir+"\\"+file)
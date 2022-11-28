import os
import sys, re
import glob

def scan_folder(parent):
    file_name =glob.glob(parent + '/**/*.faa', recursive=True)
    f = open(file_name[0])
    lines = f.read()
    prot = ''.join(lines.split('\n')[1:])
    return prot
    # print(lines)
    # iterate over all the files in directory 'parent'
    # for file_name in os.listdir(parent):
    #     if file_name == "protein.faa":
    #         # if it's a txt file, print its name (or do whatever you want)
    #         print(file_name)
    #         f = open(file_name)
    #         lines = f.read()
    #         print(lines)
            
    #     else:
    #         current_path = "".join((parent, "/", file_name))
    #         if os.path.isdir(current_path):
    #             # if we're checking a sub-directory, recursively call this method
    #             scan_folder(current_path)

print(scan_folder("C:\Codes\Predicting protein behaviour\TPCN2_datasets"))
# file_name = "C:\Codes\Predicting protein behaviour\TPCN2_datasets\dummy.txt"
# l = open(file_name)
# lines = l.read()
# print(lines)

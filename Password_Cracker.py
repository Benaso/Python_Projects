import Library

"""
version: 2.0
author: Victor
projectDetail: Compressed packet password exhaustive breaker
"""

# My initial idea of this program is  to use the dictionary to save the password,
# and then the dictionary to walk to find the password

#Dictionaries are limited in content,so add an iterator option

choose = int(input("Please choose the ways you want to try: "
                   "\n1.Dictionary exhaustion \t2.iteration\n"
                   "----------------------------------------\n"))
if choose == 1:
    key = int(input("Unzip one file or multiple files: "
                    "\n3.multiple \t4.single\n "
                    "----------------------------------------\n"))
    if key == 3:
        dic = str(input("Enter the path of your dictionary: \n"))
        zipfile = str(input("Enter the path of the zip file: \n"))
        Library.findPwd(dic, zipfile, 0, key)
    if key == 4:
        dic = str(input("Enter the path of your dictionary: \n"))
        zipfile = str(input("Enter the path of the zip file: \n"))
        filename = str(input("Enter the detail file name you want to uncompress: \n"))
        Library.findPwd(dic, zipfile, filename, key)
if choose == 2:
    zipPath = str(input("Enter the path of the zip file: \n"))
    Library.Iteration_(zipPath)

import zipfile
import itertools

def findPwd (dic, zfile, filename, key):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print("The zip file you passed in cannot be found.")
        return
    # define a str variable
    password = ''
    #then open the file to traverse the passwords
    with open(dic, 'r') as catalogue:
        data = catalogue.readlines()
        for item in data:
            # use strip() function to delete the blank characters
            password = item.strip()
            #start trying
            if key == 3:
                try:
                    myzip.extractall(pwd=password.encode())#解压全部文件
                    print("The password is: ", password)
                    return
                except Exception:
                    print("Error")
            # myZip.extract()#解压单个文件****功能完善点
            if key == 4:
                try:
                    myzip.extract(filename, pwd=password.encode())
                    print("The password is: ", password)
                    return
                except Exception:
                    print("Error")
        print("Sorry, there is no correct password in your dictionary")

length = 1
chars = '0123456789qwertyuiopasdfghjklzxcvbnm,./<>?":;}{|\][~`!@#$%^&*()_+-=QAZWSXEDCRFVTGBYHNUJMIKOLP'
def Iteration_(zfile):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print("The zip file you passed in cannot be found.")
        return
    global length
    passwords = itertools.product(chars, repeat= length)
    for password in passwords:
        password = ''.join(password)

        try:
            myzip.extractall(pwd=password.encode())
            print("The password is: ", password)
            return
        except Exception:
            print("Error:\t" + password)
    length += 1
    Iteration_(zfile)



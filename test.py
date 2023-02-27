def md5():
    import hashlib 
    str2hash = input("enter")
    result = hashlib.md5(str2hash.encode())
    print("The hexadecimal equivalent of hash is : ", end ="") 
    print(result.hexdigest()) 

def encrypt():
    msg = input("enter")
    l=[]
    l1=[]
    c=1
    for i in msg:
        if i == " ":
            l1.reverse()
            l.append(l1)
            l1=[]
            c=c+1
        else:
            l1.append(i)
    l1.reverse()
    l.append(l1)
    for i in range(0,c):
        counter=0
        for j in l[i]:
            counter=counter+1
        space=1
        for k in range(0,counter+1):
            l[i].insert(space," ")
            space=space+2
    if c%2==0:
        a=int(c/2)
        for i in range(0,a):
            ele=l.pop(0)
            l.append(ele)
    else:
        a=int((c+1)/2)
        for i in range(0,a):
            ele=l.pop(0)
            l.append(ele)
    length=len(l)
    s=""
    first=0
    for m in range(0,c):
        second=0
        for n in l[m]:
            s1=str(ord(l[first][second]))
            if s1=="32":
                s=s+"*"
            else:
                s=s+s1
            second=second+1
        first=first+1
    sfinal=s.replace("**","%")
    print(sfinal)


def decrypt():
    key=input("enter encrypted key")
    l=[]
    counter=0
    a=0
    c=0
    for i in key:
        if i=="%":
            s=key[a:counter]
            list1=s.split("*")
            l.append(list1)
            a=counter+1
            c=c+1
        counter=counter+1
    first=0
    mylist=[]
    for i in range (0,c):
        second=0
        l1=[]
        for j in l[i]:
            asc=int(l[first][second])
            asci=chr(asc)
            l1.append(asci)
            second=second+1
        l1.reverse()
        mylist.append(l1)
        first=first+1
    if c%2==0:
        a=int(c/2)
        for i in range(0,a):
            ele=mylist.pop(0)
            mylist.append(ele)
    else:
        a=int((c-1)/2)
        for i in range(0,a):
            ele=mylist.pop(0)
            mylist.append(ele)
    for i in range(0,c):
        for j in mylist[i]:
            print(j,end="")
        print(" ",end="")

def bruteforce_uppercase():
    import zipfile

    charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = int(input("enter the maximum length of the password"))
    complete = []
    for current in range(length):
        a = [i for i in charlist]
        for x in range(current):
            a = [y + i for i in charlist for y in a]
            complete = complete + a

    filename = input("enter the zip file name")
    z = zipfile.ZipFile(filename + '.zip')


    tries = 0
    extractfile = input("enter the filename to extract")
    print(complete)
    for password in complete:
        try:
            tries += 1
            z.setpassword(password)
            z.extract(extractfile + '.txt')
            print(f'Password was found after (tries) tries) It was {password}!')
        except:
            pass

def bruteforce_numeric():
    import zipfile
    charlist = '0123456789'
    length = int(input("enter the maximum length of the password"))
    complete = []
    for current in range(length):
        a = [i for i in charlist]
        for x in range(current):
            a = [y + i for i in charlist for y in a]
            complete = complete + a

    filename = input("enter the zip file name")
    z = zipfile.ZipFile(filename + '.zip')
    print(complete)
    tries = 0
    extractfile = input("enter the filename to extract")
    for password in complete:
        try:
            tries += 1
            z.setpassword(password)
            z.extract(extractfile + '.txt')
            print(f'Password was found after (tries) tries) It was {password}!')
        except:
            pass

def bruteforce_lowercase():
    import zipfile

    charlist = 'abcdefghijklmnopqrstuvwxyz'
    length = int(input("enter the maximum length of the password"))
    complete = []
    for current in range(length):
        a = [i for i in charlist]
        for x in range(current):
            a = [y + i for i in charlist for y in a]
            complete = complete + a

    filename = input("enter the zip file name")
    print(complete)
    z = zipfile.ZipFile(filename + '.zip')

    tries = 0
    extractfile = input("enter the filename to extract")
    for password in complete:
        try:
            tries += 1
            z.setpassword(password)
            z.extract(extractfile + '.txt')
            print(f'Password was found after (tries) tries) It was {password}!')
        except:
            pass

print("\ \        / /  ____| |    / ____/ __ \|  \/  |  ____|")
print(" \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   ")
print("  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  ")
print("   \  /\  /  | |____| |___| |___| |__| | |  | | |____ ")
print("    \/  \/   |______|______\_____\____/|_|  |_|______|")
print("")
print("      +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+")
print("      |P|A|S|S|W|O|R|D| |P|R|O|C|E|S|S|I|N|G|")
print("      +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+")
print("")
print("")
print("Enter 1 to see encryption working")
print("Enter 2 to see decryption working")
print("Enter 3 to see md5 hash working")
print("Enter 4 to see brute-force attack on md5 - numeric")
print("Enter 5 to see brute-force attack on md5 - uppercase")
print("Enter 6 to see brute-force attack on md5 - lowercase")
print("")
a=int(input("Enter the number of your choice"))
print("")
if a==1:
    print("ENCRYPTION")
    encrypt()
elif a==2:
    print("DECRYPTION")
    decrypt()
elif a==3:
    print("MD5 HASH")
    md5()
elif a==4:
    print("BRUTE-FORCE ATTACK - NUMERIC")
    bruteforce_numeric()
elif a==5:
    print("BRUTE-FORCE ATTACK - UPPERCASE")
    bruteforce_uppercase()
elif a==6:
    print("BRUTE-FORCE ATTACK - LOWERCASE")
    bruteforce_lowercase()
print("")
print("Do you wish to continue?")
b=input("Enter y/n")
print("")
while b=="y":
    a=int(input("Enter the number of your choice"))
    print("")
    if a==1:
        print("ENCRYPTION")
        encrypt()
    elif a==2:
        print("DECRYPTION")
        decrypt()
    elif a==3:
        print("MD5 HASH")
        md5()
    elif a==4:
        print("BRUTE-FORCE ATTACK - NUMERIC")
        bruteforce_numeric()
    elif a==5:
        print("BRUTE-FORCE ATTACK - UPPERCASE")
        bruteforce_uppercase()
    elif a==6:
        print("BRUTE FORCE ATTACK - LOWERCASE")
        bruteforce_uppercase()
    print("")
    print("Do you wish to continue?")
    b=input("Enter y/n")
    print("")

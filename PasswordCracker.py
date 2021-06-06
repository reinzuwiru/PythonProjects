import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest() #ffunction of hashlib library

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password found")
        print("Password is " + word)
        flag = 1
        break

#if password not in list set flag anything but 0

if flag == 0:
    print("password/passphrase is not in the list")
    
# forfiles /s /m *.jpg /c "cmd /c CertUtil -hashfile @path MD5" type in cmd to get md5 hash of all jpg files
# single files

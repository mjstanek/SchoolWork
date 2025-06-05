import hashlib
import shutil
import time

#configuration
checkinterval = 60
passwordfile = '/etc/passwd'
backupfile = '/secure_backup/passwd.bk'
knowngoodhash = 'a1a78d857d93312255ac564d9dfcb3d18d6648774330ef14f8c60cdee856f8e3'

#computes the SHA-256 hash of a file
def computehash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

#creates a backup of the password file
def subfunction():
    shutil.copy(backupfile, passwordfile)
    print("Backup created.")

#Compares the hash of the passwd file to the last known good hash recorded.
#Sends alerts if a change is detected and restores a backup copy of the last known good passwd file
def mainfunction():
    while True:
        currenthash = subfunction(passwordfile)
        if currenthash != knowngoodhash
            print("Unauthorized change detected in /etc/passwd.")
            restore_from_backup()
        else:
            print("No unauthorized changes detected.")

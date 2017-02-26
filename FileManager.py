import urllib.request
import os
import sys
import zipfile

#Download the zip file from github
def DownloadZipFile():
    url = "https://github.com/pirate/sites-using-cloudflare/archive/master.zip"

    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb') 
    file_size = int(u.getheader("Content-Length"))

    print ("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while file_size_dl < file_size:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%d bytes: [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        sys.stdout.write ("\r" + status)

    f.close()
    print(": Download complete")

#Unzip the file
def ExtractList():
    zf = zipfile.ZipFile("master.zip", "r")
    zf.extract("sites-using-cloudflare-master/sorted_unique_cf.txt")
    zf.close()

#Load the file into a dictionary
def LoadLeakList():
    leaklist = open("sites-using-cloudflare-master/sorted_unique_cf.txt")
    #Build a dictionary full of empty strings.  
    leakcache = {}
    for host in leaklist:
        leakcache[host[:-1]] = "" #There's extra newlines in the file.  We delete them.  
    return leakcache

#Output list of leaks.  This can be better.
def WriteLeakList(vulnerabilityList):
    f = open("SiteResults.txt", "w")
    for vulnerablesite in vulnerabilityList:
        f.write(vulnerablesite + "\n")
    f.close()

#Remove large files and archives.
def Cleanup():
    os.remove("master.zip")
    os.remove("sites-using-cloudflare-master/sorted_unique_cf.txt")
    os.rmdir("sites-using-cloudflare-master")
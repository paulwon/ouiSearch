import os
import sys
import requests
import time

fileOui = "/Users/zwang/projects/ouiSearch/oui.txt"
fileOuiFormatted  = "/Users/zwang/projects/ouiSearch/ouiFormatted.txt"
downloadUrl = "https://standards-oui.ieee.org/"

def printMsgAndExit(msg):
    print("---", msg)
    exit(1)

def formatFile():
    os.remove(fileOuiFormatted)
    fileWrite = open(fileOuiFormatted, "a")
    with open(fileOui, 'r') as f:
        for line in f.readlines():
            if '(base 16)' in line:
                fileWrite.write(line)
    fileWrite.close()
    
def formatSearchString(searchString):
    searchStringFormatted = searchString.replace("-", "").replace(":", "")
    if len(searchStringFormatted) != 6:
        searchStringFormatted = searchStringFormatted[0:6]
    print("--- OUI will be searched:", searchStringFormatted)
    return searchStringFormatted

def search(searchStringFormatted):
    print("--- Search result:")
    with open(fileOuiFormatted, 'r') as f:
        for line in f.readlines():
            if searchStringFormatted.upper() in line.upper():
                print(line)

def formatTime(timeStamp):
    m_ti = time.ctime(timeStamp)
    t_obj = time.strptime(m_ti)
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return T_stamp


def downloadFile():
    if os.path.exists(fileOui):
        print("--- File before the update:", formatTime(os.path.getmtime(fileOui)))
        count = len(open(fileOui).readlines( ))
        print("Number of lines of the oui file before the update:",count)
    print("--- Downloading the latest oui file from {}".format(downloadUrl))
    r = requests.get(downloadUrl, allow_redirects=True)
    open(fileOui, 'wb').write(r.content)
    print("--- File after the update:", formatTime(os.path.getmtime(fileOui)))
    count = len(open(fileOui).readlines( ))
    print("Number of lines of the oui file after the update:",count)
    formatFile()
    printMsgAndExit("OUI file has been downloaded and formated. Existing.")

def printUsageAndExit():
    usage = """Usage examples:
    {0} --update // Download or update the oui file 
    {0} 1111:2222:3333
    {0} 111122223333
    {0} 111122
    """.format(sys.argv[0])
    print(usage)
    print("Exiting ...")
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        printUsageAndExit()
    if not os.path.exists(fileOui):
        printMsgAndExit("File does not exit. Please download the oui file by using the '--update' option first. Exiting ...")
    if sys.argv[1] == "--update":
        downloadFile()
    searchStringFormatted = formatSearchString(sys.argv[1].strip())
    search(searchStringFormatted)
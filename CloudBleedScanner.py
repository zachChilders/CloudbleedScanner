#! /bin/python

import sys
import HistoryConnector
import FileManager

def main():
    #Retrieve your chosen browser history, potentially will retrieve all browser histories
    historyConn = HistoryConnector.HistoryConnector()#str(sys.argv[1]).lower())
    historylist = historyConn.RetrieveHistoryList()

    #Obtain the latest list from github
    print("Fetching vulnerable site list.  (It's pretty big)")
    FileManager.DownloadZipFile()
    FileManager.ExtractList()
    print("Vulnerable site list unpacked.")

    #Load Leak list into a dictionary
    print("Searching browser history for vulnerable sites.")
    leakcache = FileManager.LoadLeakList()

    #Test dictionary for every hostname in browser history
    vulnerabilityList = []
    for history in historylist:
        if history in leakcache:
            vulnerabilityList.append(history)

    #Try to do something useful with this information
    print(str(len(vulnerabilityList)) + " vulnerable sites found.")
    FileManager.WriteLeakList(vulnerabilityList)
    FileManager.Cleanup()

if __name__ == "__main__":
    main()
    
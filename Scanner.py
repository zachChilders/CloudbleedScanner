#! /bin/python
import sys
import HistoryConnector
import FileManager

def main():
    h = HistoryConnector.HistoryConnector(str(sys.argv[1]))
    historylist = h.retrieveHistoryList()
    print("Building vulnerable site cache")
    FileManager.DownloadZipFile()
    FileManager.ExtractList()
    print("List unpacked")
    leakcache = FileManager.LoadLeakList()
    print("Cache built")

    vulnerabilityList = []
    for history in historylist:
        if history in leakcache:
            vulnerabilityList.append(history)

    print(str(len(vulnerabilityList)) + " vulnerable sites found.")

if __name__ == "__main__":
    main()
    
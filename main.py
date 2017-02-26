#! /bin/python
import HistoryConnector

def main():
    h = HistoryConnector.HistoryConnector("firefox")
    historylist = h.retrieveHistoryList()
    print("Building vulnerable site cache")
    leakcache = {}
    leaklist = open(".\sorted_unique_cf.txt")
    for host in leaklist:
        leakcache[host[:-1]] = ""
    print("Cache built")

    vulnerabilityList = []
    for history in historylist:
        if history in leakcache:
            vulnerabilityList.append(history)

    print(str(len(vulnerabilityList)) + " vulnerable sites found.")

if __name__ == "__main__":
    main()
    
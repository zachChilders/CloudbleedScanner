import sys
import os
import re
import sqlite3




'''
This class is used to connect to the history of various browsers.  More will be added shortly.
'''
class HistoryConnector():

    def __init__(self):
        #Build location list 
        #Firefox is a pain
        ffbasePath = os.getenv('APPDATA') + r"\Mozilla\Firefox\Profiles"
        for filename in os.listdir(ffbasePath):
            if re.match("[a-zA-z0-9]{1,12}.default", filename):
                self.FIREFOX_LOCATION = ffbasePath + "\\" + filename + r"\places.sqlite"
        #Google made it easy on us        
        self.CHROME_LOCATION = os.getenv('LOCALAPPDATA') + r"\Google\Chrome\User Data\Default\History"

    def __del__(self):
        self.conn.close()

    def RetrieveHistoryList(self):
        
        firefox = self.retrieveFirefox()
        chrome = self.retrieveChrome()
        historylist = firefox + chrome

        return {h[0] for h in historylist}
    
    def retrieveFirefox(self):
        historylocation = self.FIREFOX_LOCATION
        self.conn = sqlite3.connect(historylocation)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT host FROM moz_hosts")
        historylist = self.cursor.fetchall()
        self.conn.close()
        return historylist


    def retrieveChrome(self):
        historylocation = self.CHROME_LOCATION
        self.conn = sqlite3.connect(historylocation)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT url FROM urls")
        historylist = self.cursor.fetchall()
        self.conn.close()
        return historylist
        
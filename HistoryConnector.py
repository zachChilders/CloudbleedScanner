import sys
import os
import re
import sqlite3

#Build location list 
#Firefox is a pain
ffbasePath = os.getenv('APPDATA') + r"\Mozilla\Firefox\Profiles"
for filename in os.listdir(ffbasePath):
    if re.match("[a-zA-z0-9]{1,12}.default", filename):
        FIREFOX_LOCATION = ffbasePath + "\\" + filename + r"\places.sqlite"
#Google made it easy on us        
CHROME_LOCATION = os.getenv('LOCALAPPDATA') + r"Google\Chrome\User Data\Default\History"

'''
This class is used to connect to the history of various browsers.  More will be added shortly.
'''
class HistoryConnector():

    def __init__(self, browser):
        self.browser = browser
        if browser == "firefox":
            historylocation = FIREFOX_LOCATION
        elif browser == "chrome":
            historylocation = CHROME_LOCATION

        self.conn = sqlite3.connect(historylocation)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def RetrieveHistoryList(self):
        # Make trigger for chrome as well
        if self.browser == "firefox":
            self.cursor.execute("SELECT host FROM moz_hosts")
        elif self.browser == "chrome":
            self.cursor.execute("SELECT url FROM urls")
        historylist = self.cursor.fetchall()
        return {h[0] for h in historylist}
        

import sqlite3

FIREFOX_LOCATION = r"C:\Users\zwc10\AppData\Roaming\Mozilla\Firefox\Profiles\60786wyw.default\places.sqlite"
CHROME_LOCATION = r"C:\Users\zwc10\AppData\Local\Google\Chrome\User Data\Default\History"

class HistoryConnector():

    def __init__(self, browser):
        self.browser = browser
        if browser == "chrome":
            historylocation = CHROME_LOCATION
        elif browser == "firefox":
            historylocation = FIREFOX_LOCATION

        self.conn = sqlite3.connect(historylocation)
        self.cursor = self.conn.cursor()



    def __del__(self):
        self.conn.close()

    def retrieveHistoryList(self):
        # Make trigger for chrome as well
        if self.browser == "firefox":
            self.cursor.execute("SELECT host FROM moz_hosts")
        elif self.browser == "chrome":
            self.cursor.execute("SELECT url FROM urls")
        historylist = self.cursor.fetchall()
        return {h[0] for h in historylist}
        
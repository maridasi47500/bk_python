global addcard
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from directory import directory
class addcardpage(directory):
    def __init__(self):
        self.set_path("./mespages")
        j=open(self.get_filename_path("addcard.html"),'rb')
        self.set_path("./css")
        self.add_css("signin.css")
        self.add_css("addcard.css")
        self.add_js("addcard.js")
        text=force_to_unicode(j.read())
        self.set_content(text)
        self.set_path("./mespages")
        k=open(self.get_filename_path("headeroverlay.html"),'rb')
        headertext=k.read()
        self.set_header(headertext)
        crsr.execute("SELECT * FROM cards")
        connection
        ans = crsr.fetchall()


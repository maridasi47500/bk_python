# coding=utf-8
global code
import codecs
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()

from directory import directory
class codepage(directory):
    def __init__(self,title,params):
        self.redirect=""
        self.set_title(title)
        print("code")
        self.set_path("./mespages")
        f=open(self.get_filename_path("userconnecte.js"),'r')
        js=f.read()
        ff=open(self.get_filename_path("code.html"),'r')
        text=ff.read()
        self.set_path("./js")
        self.add_js("userconnecte.js")
        self.set_header(self.get_header())
        self.set_footer(self.get_footer())
        self.set_path("./redeem")
        try:
          print(params["userid"][0])
          userid=params["userid"][0]
          print("user connecté")
          #select l'utilisateur et voir si il a une address et un restaurant
          sql="select * from users where user_number = ?"
          user=crsr.execute(sql,(userid,)).fetchall()[0]
          if int(user[-2]) <= 0 and int(user[-3]) <= 0:
            self.set_redirect("/store-locator/service-mode")


        except:
          print("user non connecté")
        self.set_content(unicode(text,'utf-8'))

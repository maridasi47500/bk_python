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

        self.set_path("./code")
        ff=open(self.get_filename_path("code.html"),'r')
        text=ff.read()
        self.add_js("userconnecte.js")
        self.set_header(self.get_header())
        self.set_footer(self.get_footer())

        try:
          print(params["userid"][0])
          userid=params["userid"][0]
          print("user connecté")
          #select l'utilisateur et voir si il a une address et un restaurant
          sql="select * from users where user_number = ?"
          user=crsr.execute(sql,(userid,)).fetchall()[0]
          print("tous les utilisateur selectionnees",user)
          #print(int(user[-2]) <= 0, "restaurant choisi",int(user[-2]))
          #print(int(user[-3]) <= 0, "adresse de liraison choisie",int(user[-3]))
          if user[-2] is None and user[-3] is None:
            self.set_redirect("/store-locator/service-mode")


        except Exception as e:
          print("user non connecté ERREUR??:",e)
        self.set_content(unicode(text,'utf-8'))
        print("fin de cod #code #codebk #redeem")


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
from erreur import erreur

from directory import directory
class codepage(directory):
    def __init__(self,title,params):
        self.set_title(title)
        print("code")

        self.set_path("./code")
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
          restaurant=self.searchattribute(user,"users","restaurant_id")
          address=self.searchattribute(user,"users","address_id")
          print("tous les utilisateur selectionnees",user,"restaurant",restaurant,"address",address)
          if restaurant is None and address is None:
            self.set_redirect("/store-locator/service-mode")


          self.content_from_file("code.html")
        except Exception as e:
          print("user non connecté ERREUR??:",e)

        print("fin de cod #code #codebk #redeem")


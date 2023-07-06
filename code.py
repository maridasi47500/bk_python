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
import traceback
import sys

from directory import directory
class codepage(directory):
    def __init__(self,title,params):
      try:
        self.set_title(title)
        print("code")

        self.set_path("./code")
        self.add_js("userconnecte.js")
        self.add_css("mycode.css")
        self.set_header_with_path("header.html")
        print("footer")
        self.set_footer_with_path("footer.html")
        try:
          print(params["userid"][0])
          userid=params["userid"][0]
          print("user connecté")
          #select l'utilisateur et voir si il a une address et un restaurant
          sql="select * from users where user_number = ?"
          try:
            user=crsr.execute(sql,(userid,)).fetchall()[0]
          except:
            user=None
          try:
            restaurant=self.searchattribute(user,"users","restaurant_id")
          except:
            restaurant=None
          try:
            address=self.searchattribute(user,"users","address_id")
          except:
            address=None
          print(" CHERCHER ICI tous les utilisateur selectionnees",user,"restaurant",restaurant,"address",address)
          if user is not None and restaurant is None and address is None:
            self.set_redirect("/store-locator/service-mode")
          if restaurant is not None:
            self.set_header_with_path_and_address("headersignedin.html",userid)

          


          self.content_from_file("codesignedin.html")
        except Exception as e:
          print("user non connecté ERREUR??:",e)
          self.content_from_file("code.html")
          userid=None
        print("currentuer")
        self.set_current_user_id(userid)
        print("heder")



        print("fin de cod #code #codebk #redeem")

      except Exception as e:
        self.__class__ = erreur
        #self.set_erreur(str(e))

        print(traceback.format_exc())
        self.set_erreur(str(traceback.format_exc()))
        # or
        #print(sys.exc_info()[2])
        self.set_title("Erreur route redeem: "+str(e))



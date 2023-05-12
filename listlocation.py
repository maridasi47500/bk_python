from directory import directory
import re
import sqlite3
from redirect import redirectaction
connection = sqlite3.connect("mesburgers1.db")
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
class listlocationpage(directory):
    def __init__(self,params):
        print("listthislocation")
        self.path=".\store-locator"
        self.current_order=[]
        self.layout=False
        self.header=""
        self.footer=""
        param=params["mylist"][0]
        userid=params["userid"][0]
        #voulez vous me partager lon/lat?
        #favorite recents or nearby?
        #à proximité , favoris puis recents
        if param == "nearby":
          sql_command = "select * from bks"
          tablename="bks"
          message_else=""
          collectionstr= self.display_collection(sql_command, (), "_combosize", message_else, tablename)
        elif param == "favorite":
          sql_command = "select * from bks left join favs on favs.bk_id = bks.id group by bks.id having bk.user_id in (?)"
          tablename="bks"
          message_else=""
          collectionstr= self.display_collection(sql_command, (), "_combosize", message_else, tablename)
        self.set_content("")


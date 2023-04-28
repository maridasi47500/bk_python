from directory import directory
import re
import sqlite3
from redirect import redirectaction
connection = sqlite3.connect("mesburgers1.db")
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
class addburgeraction(redirectaction):
    def __init__(self,params):
        print("add this burger to order")
        self.current_order=[]
        self.layout=""
        self.header=""
        self.footer=""
        self.content=""
        self.set_path("./")
        self.css=""
        self.js=""
        print("show menu",params)
        self.set_title("Burger King")
        self.set_redirect("/")
        try:
            id=params["id"][0]
        except:
            id=None
        try:
            userid=params["userid"][0]
        except:
            userid=None
        try:
            nb=params["id"][0]
        except:
            nb=None
        try:
            print(params["mydata[]"][0])
            order=params["mydata[]"]
        except:
            order=[]
        sql="insert into preorders (burger_id,user_id,qty,data,display) values (?,?,?,?,?);"
        print("data")
        data=(id,userid,nb,"",0)
        print(data)
        try:
          if len(order) == 0 and userid is not None:
              crsr.execute(sql,(id,userid,nb,"","0"))
              connection.commit()
          else:
              for x in order:
                  crsr.execute(sql,(id,userid,nb,x,"0"))
                  connection.commit()
        except Exception as e:
          print(e)
        order.insert(0,nb)
        order.insert(0,id)
        print(order)
        self.current_user=()

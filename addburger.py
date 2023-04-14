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
            order=params["mydata"][0]
        except:
            order=[]
        sql="insert into preorders (burger_id,user_id,qty,data) values (?,?,?,?);"
        print("data")
        data=(id,userid,nb,"")
        print(data)
        if len(order) == 0 and userid is not None:
            crsr.execute(sql,(id,userid,nb,""))
            connection.commit()
        else:
            for x in order:
                crsr.execute(sql,(id,userid,nb,x))
                connection.commit()
        order.insert(0,nb)
        order.insert(0,id)
        print(order)
        self.current_user=()

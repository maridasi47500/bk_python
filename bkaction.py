from directory import directory
import re
import sqlite3
from jsoncontent import jsoncontent
from redirect import redirectaction
connection = sqlite3.connect("mesburgers1.db")
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
class bkactionjson(jsoncontent):
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
            print(params[""][0])
            order=params["action"]
        except:
            order=[]

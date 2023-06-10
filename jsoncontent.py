from directory import directory
import os
import json
global path1
import sqlite3  
global codecs
import codecs
from multipledispatch import dispatch
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
class jsoncontent(directory):
    mimetype="json"
    layout=""
    redirect=None

    def __init__(self,title):
        global path1
        self.htmlpath="/"
        path1=os.getcwd()
        self.path1=os.getcwd()
        self.title = title
        self.mytitle = title
        self.js=""
        self.url=""
        self.html=""
        self.current_order=[]
        self.mime=None
        self.content=""
        self.response=200
        self.json=None
        self.userid=""
        self.redirect=None
        self.email=""
        self.css=""
        self.menu=""
        self.path=os.getcwd()+"/mespages"
        print(self.get_file_with_path("header.html"))
        header1=self.get_file_with_path("header.html")
        footer1=self.get_file_with_path("footer.html")
        self.header=header1.read()
        self.path=""
        self.footer=footer1.read()
        self.parameters={}
        self.current_user=None

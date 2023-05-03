from directory import directory 
import os
class redirectaction(directory):
    def __init__(self,redirect):
        global path1
        self.htmlpath="/"
        path1=os.getcwd()
        self.path1=os.getcwd()
        self.title = "title"
        self.layout = "ok"
        self.mytitle = redirect
        self.js=""
        self.url=""
        self.html=""
        self.current_user=()
        self.current_order=[]
        self.mime=None
        self.content=""
        self.response=200
        self.json=None
        self.userid=""
        self.redirect=redirect
        self.email=""
        self.css=""
        self.menu=""
        self.path=os.getcwd()+"/mespages"
        self.header=""
        self.path=""
        self.footer=""
        self.parameters={}
        self.current_user=None

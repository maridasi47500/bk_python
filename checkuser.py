import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from directory import directory
from jsoncontent import jsoncontent
class checkuserpage(jsoncontent):
    def __init__(self,title,query_components):
        self.layout=""
        self.current_user=""
        self.redirect=None
        print(query_components)
        print("validate code",query_components.get("email"))
        if query_components.get("email"):
            email=query_components.get("email")[0]
            crsr.execute("SELECT * FROM users where email = '"+str(email)+"'")
            connection.commit()
            users=crsr.fetchall()
            mytype="json"
            if len(users) == 0:
                self.set_json({"usernotexist":"1"})
            else:
                self.set_json({"usernotexist":"0"})

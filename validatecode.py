global validatecode
from directory import directory
import sqlite3

connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class validatecodepage(directory):
    def __init__(self,title,query_components):
        print(query_components)
        self.title=title
        print("validate code",query_components.get("code"))
        if query_components.get("code"):
            code=query_components.get("code")[0]
            userid=query_components.get("userid")[0]
            crsr.execute("SELECT * FROM users where code = '"+str(code)+"' and user_number = '"+str(userid)+"'")
            connection.commit()
            users=crsr.fetchall()
            if len(users) > 0:
                session.current_user=users[0]
                Program.set_json({"id":users[0][0],"correcturl":"1","url": "/store-locator"})
                print(Program.get_json())
            else:
                Program.set_json({"correcturl":"0","url": "/signin/codeincorrect"})
                print(Program.get_json())
            Program.set_mimetype("json")

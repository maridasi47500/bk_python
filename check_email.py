from directory import directory
global checkemail
class checkemailpage(directory):
    def __init__(self,title,query_components):
        print(query_components)
        print("validate code",query_components.get("email"))
        if query_components.get("email"):
            email=query_components.get("email")[0]
            crsr.execute("SELECT * FROM users where email = '"+str(email)+"'")
            connection.commit()
            users=crsr.fetchall()
            if len(users) > 0:
                self.set_json({"correctemail":"1"})
                print(self.get_json())
            else:
                self.set_json({"correctemail":"0"})
                print(self.get_json())
            self.set_mimetype("json")

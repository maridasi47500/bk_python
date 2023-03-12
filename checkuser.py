from directory import directory
class checkuserpage(directory):
    def __init__(self,title,query_components):
        print(query_components)
        print("validate code",query_components.get("email"))
        if query_components.get("email"):
            email=query_components.get("email")[0]
            crsr.execute("SELECT * FROM users where email = '"+str(email)+"'")
            connection.commit()
            users=crsr.fetchall()
            mytype="json"
            if len(users) == 0:
                Program.set_json({"usernotexist":"1"})
            else:
                Program.set_json({"usernotexist":"0"})

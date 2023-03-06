import directory
global checkemail

def checkemail(query_components):
    try:
        Program=directory('burger king') 

        print(query_components)
        print("validate code",query_components.get("email"))
        if query_components.get("email"):
            email=query_components.get("email")[0]
            crsr.execute("SELECT * FROM users where email = '"+str(email)+"'")
            connection.commit()
            users=crsr.fetchall()
            if len(users) > 0:
                Program.set_json({"correctemail":"1"})
                print(Program.get_json())
            else:
                Program.set_json({"correctemail":"0"})
                print(Program.get_json())
            Program.set_mimetype("json")
            return Program
    except Exception as e:
        print("erreur validate code",e)

global validatecode
def validatecode(query_components):
    try:
        print(query_components)
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
            return Program
    except Exception as e:
        print("erreur validate code",e)
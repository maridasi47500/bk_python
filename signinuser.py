from directory import directory
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
class pagesigninuser(directory):
    def __init__(self,title,params):
        print("")
        self.title=title
        if params.get("user_number"):


            user_number=params.get("user_number")[0]
            code=params.get("bkcode")[0]
            sql="select * from users where user_number = "+str(user_number)+" and code = '"+code+"';"
            print(sql)
            crsr.execute(sql)
            connection.commit()
            users=crsr.fetchall()

            print(users)
            if len(users) > 0:
                #bkcode=rand.randint(100000,999999)
                #sql="UPDATE users SET code = '" + str(bkcode) + "' WHERE user_number = "+user_number+""
                #print(sql)
                #crsr.execute(sql)
                #connection.commit()
                #users=crsr.fetchall()
                #print(users)
                #sql="select * from users where user_number = "+str(user_number)+";"
                #print(sql)
                #crsr.execute(sql)
                #connection.commit()
                sql1="delete from preorders where user_id = ?"
                data1=(user_number,)
                crsr.execute(sql1,data1)
                connection.commit()
                user=users[0]
                self.set_current_user(user)
                crsr.execute("update users set signedin = ? where user_number = ?",(1,user[0]))
                connection.commit()

                self.set_redirect("/confirm-otp")


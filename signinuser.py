import directory

global signinuser
def signinuser(params):
    try:
        Program=directory('burger king') 

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
                user=users[0]
                session.current_user=user
                print(session.current_user)
                Program.set_current_user(user)
                Program.set_redirect("/confirm-otp")
            return Program
    except Exception as e:
        print("erreur: sign in user ",e)
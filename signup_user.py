global signup_user
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
global crsr
crsr = connection.cursor()

from directory import directory
class signup_user_page(directory):
    def __init__(self,title,query_components):
        self.title="inscription"
        
        print("sign sign up",query_components["email"])
        if query_components.get("email"):
            print("data_string = query_components[\"email\"][0]")
            data_string = query_components["email"][0]

            print("crsr.execute(\"SELECT * FROM users where email = '\"+data_string+\"'\")")
            mycontent=""
            # store all the fetched data in the ans variable
            date=""
            try:
                print("date de naisance===")
                annee=int(query_components.get("yy")[0])
                print(annee)
                mois=int(query_components.get("mm")[0])
                print(mois)
                jour=int(query_components.get("dd")[0])
                print(jour)
                w=datetime.datetime(annee,mois,jour)
                print(w)
                date=str(w)
            except:
                print("erreur champ date de naissance")
            prenom = query_components.get("prenom")[0]
            email = query_components.get("email")[0]
            offreparam=query_components.get("offres")
            offres = offreparam[0] if offreparam == ["1"] else "0"
            #user = crsr.fetchall()
            print("envoyer le code bk")
            bkcode=rand.randint(100000,999999)
            token=binascii.b2a_hex(os.urandom(159))

            crsr.execute("insert into users (prenom,email,code,token,dateofbirth) values ('" + str(prenom) + "','" + str(email) + "','"+str(bkcode)+"','" + str(token) + "','" + str(date) + "')")
            connection.commit()
            crsr.execute("select * from users where email = '"+email+"'")
            connection.commit()
            ant=crsr.fetchall()
            session.current_user = ant[0]
            urlconfirmjwt="/confirm-jwt?token="+str(token)
            self.set_url(urlconfirmjwt)

            #confirmotp(data_string)
            print("set redirect ICI")
            self.set_redirect("/confirm-jwt?token="+str(token))

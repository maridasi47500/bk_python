from directory import directory
import sqlite3
global crsr
connection = sqlite3.connect("mesburgers1.db")

crsr = connection.cursor()
from jsoncontent import jsoncontent

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()

class savemyinfopage(jsoncontent):
    def __init__(self,title,query_components):
        print("save my info",query_components["user_number"])
        if query_components.get("user_number"):
            try:
                id=query_components.get("user_number")[0]
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
                    date=""
                print(date)
                print(query_components)
                try:
                    tel=query_components.get("tel")[0]
                except:
                    tel=""
                print(tel)
                try:
                    zip=query_components.get("zip")[0]
                except:
                    zip=""
                try:
                    prenom=query_components.get("prenom")[0]
                except:
                    prenom=""
                offres="0"
                print(offres)
                try:
                    offres=query_components.get("offres")[0]
                except:
                    print("erreur recevoir offres")
                sql="update users set dateofbirth = '"+date+"', prenom = '"+prenom+"',offres='"+offres+"', zip = '"+zip+"', tel = '"+tel+"' where user_number = " + str(id) + ""
                print(sql)
                crsr.execute(sql)
                connection.commit()
                crsr.execute("select * from users where user_number = " + str(id) + "")
                connection.commit()
                ant=crsr.fetchall()
                self.set_current_user(ant[0])
                print("hello")
                self.set_json({"sauve":"1"})
            except Exception as e:
                print("erreur save data",e)
                self.set_json({"sauve":"0"})
            self.set_mimetype("json")

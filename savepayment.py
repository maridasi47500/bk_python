import directory
def savepayment(query_components):
    try:
        Program=directory("")
        print("save payment method",query_components["nom"])
        if query_components.get("nom"):
            print("save payment method")
            nom=query_components.get("nom")[0]
            zip=query_components.get("zip")[0]
            creditcard=query_components.get("creditcard")[0]
            cvv=query_components.get("cvv")[0]
            mmyy=query_components.get("date")[0]
            try:
                j=mmyy.split("/")
                annee=int("20"+str(j[1]))
                mois=int(j[0])
                jour=1
                date=datetime.datetime(annee,mois,jour)
            except:
                print("erreur cvv")
            sql="insert into creditcards (nom,zip,creditcard,cvv,datecard,user_id) values (?, ?, ?, ?, ?,?)"  
            values=(nom,zip,creditcard,cvv,mmyy,session.current_user[0])
            
            crsr.execute(sql,values)
            connection.commit()
            Program.set_json({"ok":"1"})
        else:
            Program.set_json({"ok":"0"})
        Program.set_mimetype("json")
        return Program
    except Exception as e:
        print("erreur save payment method",e)

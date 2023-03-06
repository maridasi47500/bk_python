global afficher_modepaiement
def afficher_modepaiement(text,usernumber):
    sql="select * from payments where user_id = "+str(usernumber)
    print(sql)
    crsr.execute(sql)
    connection.commit()
    res=crsr.fetchall()
    if len(res) > 0:
        html=""
        return html
    else:
        return text.replace('ici le mode de paiement',"<p>Vous n'avez actuellement aucun mode de paiement enregistré</p>"),

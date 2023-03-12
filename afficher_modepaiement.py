# -*- coding: utf-8 -*-
global afficher_modepaiement
from directory import directory
import sqlite3
connection = sqlite3.connect("desburgers.db")

global crsr
crsr = connection.cursor()

class afficher_modepaiementpage(directory):
    def __init__(self,text,usernumber):
        sql="select * from payments where user_id = "+str(usernumber)
        print(sql)  
        crsr.execute(sql)
        connection.commit()
        res=crsr.fetchall()
        if len(res) > 0:
            html=""
            return html
        else:
            return text.replace('ici le mode de paiement',"<p>Vous n'avez actuellement aucun mode de paiement enregistré</p>") 



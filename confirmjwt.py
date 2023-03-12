# -*- coding: utf-8 -*-
global confirmjwt
import sqlite3
connection = sqlite3.connect("desburgers.db")
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# cursor
global crsr
crsr = connection.cursor()

from directory import directory
class confirmjwtpage(directory):
    def __init__(self,title):
        self.title=title
        print("sign sign up",query_components["token"])
        if query_components.get("token"):
            token=query_components.get("token")[0]

            crsr.execute("select * from users where token = '" + str(token) + "'")
            connection.commit()
            user=crsr.fetchall()[0]
            self.set_current_user(user)
            user_number=user[0]
            prenom = user[1]
            email = user[2]
            offres = user[5]
            #user = crsr.fetchall()
            print("envoyer le code bk")
            bkcode=user[3]

            # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
            host_smtp = "smtp.gmail.com"
            port_smtp = 587
            email_smtp = "mary.goudon@gmail.com" # Mon email Gmail
            mdp_smtp = "eljlkuznppklsquw"  # Mon mot de passe

            # Configuration du mail
            self.set_path("./mespages")
            m=get_file("inscription.txt")
            n=m.read()
            print("mail")
            mail_content = n
            print("mail")
            mail_content+="\n http://localhost:8000/confirm-jwt?token="+str()
            print("dest")
            email_destinataire = "cleo.ordioni@gmail.com"
            formule_p = "Inscription à Burger King"
            msg = MIMEMultipart()
            msg['From'] = email_smtp
            msg['To'] = email_destinataire
            msg['Subject'] = formule_p
            print("message")
            msg.attach(MIMEText(str(mail_content)))
            # Création de l'objet mail
            mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
            mail.ehlo() # protocole pour SMTP étendu
            mail.starttls() # email crypté
            mail.login(email_smtp, mdp_smtp)
            print("envoyer message")
            mail.sendmail(email_smtp, email_destinataire, msg.as_string())
            mail.close()
            self.set_path("./")

            self.set_url("/")
            self.set_redirect("/")
            #self.set_redirect("/signinuser?user_number=" + str(user_number))
            self.set_mimetype(None)

# -*- coding: utf-8 -*-
from directory import directory
global signmein
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
global crsr

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
crsr = connection.cursor()
class signmeinpage(directory):
    def __init__(self,query_components):
        print("sign me in",query_components["email"])
        if query_components.get("email"):
            print("data_string = query_components[\"email\"][0]")
            data_string = query_components["email"][0]
            print("crsr.execute(\"SELECT * FROM users where email = '\"+data_string+\"'\")")
            crsr.execute("SELECT * FROM users where email = '"+data_string+"'")
            mycontent=""
            # store all the fetched data in the ans variable
            connection.commit()
            ans = crsr.fetchall()
            if len(ans) == 0:
                print("no user")
            else:
                crsr.execute("SELECT * FROM users where email = '"+data_string+"'")
                connection.commit()
                user = crsr.fetchall()
                user_number=user[0][0]
                print("envoyer le code bk")
                print(user[0])
                print(user[0][0])
                self.set_userid(user[0][0])
                bkcode=rand.randint(100000,999999)
                crsr.execute("UPDATE users SET code = '" + str(bkcode) + "' WHERE email = '"+data_string+"'")
                connection.commit()


                # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
                host_smtp = "smtp.gmail.com"
                port_smtp = 587
                email_smtp = "mary.goudon@gmail.com" # Mon email Gmail
                mdp_smtp = "eljlkuznppklsquw"  # Mon mot de passe

                # Configuration du mail
                prenom = "cleo jeanne"
                print(prenom)
                print("prenom")
                mail_content = force_to_unicode("Prêt pour les hamburgers ? !\nVous trouverez ci-dessous le code de connexion sécurisé que vous avez demandé pour vous connecter à Burger King. Entrez simplement ceci dans l'application et nous vous connecterons immédiatement.\n ") + force_to_unicode(str(bkcode))
                print("mail_content")
                email_destinataire = "cleo.ordioni@gmail.com"
                print(email_destinataire)
                formule_p = force_to_unicode(str(bkcode))+" est votre code de connexion de burger king"
                print(formule_p)
                msg = MIMEMultipart()
                print("from")
                msg['From'] = email_smtp
                print("to")
                msg['To'] = email_destinataire
                print("subject")
                msg['Subject'] = formule_p
                print("formule")
                try:
                    msg.attach(MIMEText(mail_content.decode('utf-8')))
                except UnicodeEncodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    msg.attach(MIMEText(mail_content.encode('utf-8')))
                except UnicodeDecodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    msg.attach(MIMEText(mail_content))
                print("creation mail")
                # Création de l'objet mail
                mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
                mail.ehlo() # protocole pour SMTP étendu
                mail.starttls() # email crypté
                mail.login(email_smtp, mdp_smtp)
                mail.sendmail(email_smtp, email_destinataire, msg.as_string())
                mail.close()

                #confirmotp(force_to_unicode(data_string))
                self.set_redirect("/signinuser?user_number=" + str(user_number)+"&bkcode="+str(bkcode))

                self.set_json(None)
                self.set_mimetype(None)

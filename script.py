# -*- coding: utf-8 -*-
import json
import binascii
import random as rand
import smtplib
import datetime
import sys
import requests
global session
import sqlite3
global copy
global render_pages
global connection
global get_file
global switcher

switcher={
'html':'text/html',
'css':'text/css',
'json':'application/json',
'js':'text/javascript',
'png':"image/png",
'ico':'image/vnd.microsoft.icon'
}


connection = sqlite3.connect("db_burger090ERYYTHYYY7.db")

# cursor
global crsr
crsr = connection.cursor()

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()
global force_to_unicode
global decode_any_string
def decode_any_string(text):
    try:
        print(text)
        return force_to_unicode(text)
    except UnicodeEncodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text.encode('utf-8')
    except UnicodeDecodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text

def force_to_unicode(text):
    "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
    return text if isinstance(text, unicode) else text.decode('utf-8')
session = requests.Session()
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from os.path import exists
from urlparse import urlparse, parse_qs
import os
global path1
path1=os.getcwd()
sys.path.append(os.path.abspath(os.getcwd()+"/pythonfile"))
from myfunc import *
from pagehtml import *
import codecs
import re


global Program
global get_file
global get_file_dir
def get_file(file):
    print("get file:")
    print(Program.get_filename_path(file))
    return open(Program.get_filename_path(file),'r')
def get_file_dir(file,dir):
    print("get file:"+dir)
    Program.set_path(dir)
    return open(Program.get_path()+"/"+file,'r')

global mycard
global myparams


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import random

# connecting to the database
global infotable
def infotable(tablename):
    crsr.execute("PRAGMA table_info(["+tablename+"])")
    connection.commit()
    matable=crsr.fetchall()
    return matable
def display_collection(sql,sqlargs,templatename,errormessage,tablename,sortby = False,templatesortby = False):
    idprecedent=0
    print(sqlargs)
    print(len(sqlargs))
    print(sql,sqlargs,templatename,errormessage,tablename)
    crsr.execute("PRAGMA table_info(["+tablename+"])")
    connection.commit()
    matable=crsr.fetchall()
    Program.set_path("./mespages")
    h=get_file(templatename+".html")
    template=force_to_unicode(h.read())
    mysql=sql % sqlargs
    print(mysql)
    crsr.execute(mysql)
    connection.commit()
    res=crsr.fetchall()
    myfigure=""
    x=0
    mytemplate=""
    if len(res) > 0:
        print("plusieurs "+tablename)

        for re in res:
            paspremier = False
            mytemplate=force_to_unicode(template)
            for x in range(len(re)):
                print(x)
                print(re[x])
                z=re[x]
                strrep=force_to_unicode("(%s)" % (matable[x][1]))
                print(strrep)
                if type(z) == int or type(z) == float:
                    z=str(z)
                if z is not None:
                    mytemplate=mytemplate.replace(strrep, force_to_unicode(z))
                if matable[x][1] == sortby:
                    if idprecedent != 0:
                        if re[x] != idprecedent:
                            if paspremier:
                                myfigure+="</div>"
                                paspremier = True
                            Program.set_path("./mespages")
                            kk=get_file(templatesortby)
                            kk=kk.read()
                            y=0
                            for y in range(len(re)):
                                mystrrep="(%s)" % (matable[y][1])
                                kk=kk.replace(mystrrep, force_to_unicode(str(re[y])))
                            myfigure += kk
                    idprecedent=re[x]

            myfigure+=mytemplate
            myfigure+="</div>"
        return myfigure
    else:
        return force_to_unicode("<p>"+errormessage+"</p>")
global searchmyparams
def searchmyparams(query_components,myurlpath):
    print("search for my params")
    mysql="select * from burgercats"
    crsr.execute(mysql)
    connection.commit()
    res=crsr.fetchall()
    mysql="select * from burgers order by burger_number desc"
    crsr.execute(mysql)
    connection.commit()
    res2=crsr.fetchall()


    dic={"/menu/recents":"recents","/menu/favorites":"favorites","/menu":"fullmenu"}
    print(myurlpath,";;this url path ::",dic)
    mytab1=dic.get(myurlpath)
    if mytab1 is not None:

        myurlpath = "/menu"
        query_components["mytab"]=[mytab1]
        print("url",myurlpath,"my tab",query_components.get("mytab"))

    else:
        spliturl=myurlpath.split("/")
        if spliturl[-1] == "menu" or spliturl [-2] == "menu":
            print("url: ",myurlpath)

            for r in res:
                print(r[0],r[1],r[2])
                if "/"+r[2] in myurlpath:
                    myurlpath=myurlpath.replace("/"+r[2], "")
                    query_components["catid"]=[r[0]]
                    print("category",r[1])
            for r in res2:
                print(r[0],r[1],r[2])
                if "/menu/"+str(r[0]) in myurlpath:
                    myurlpath=myurlpath.replace("/menu/"+str(r[0]), "/burger")
                    query_components["burgerid"]=[r[0]]
            print(myurlpath)
    return [myurlpath,query_components]
global __words__
__words__ = ""
def render_figure(pathname):
    try:
        global path1
        path1=os.getcwd()
        Program.set_filename(pathname)
        print("render figure")
        print('ok')
        p1=Program.get_path
        p2=Program.get_filename
        print("okdac")
        print(p1())
        print("okokdac")
        print(p2())
        print(p1()+p2())
        print('dac')
        title=Program.get_title
        try:
            print(session.current_user)
            Program.set_path("./mespages")
            h=get_file("mynavsignedin.html")
            Program.set_menu(h.read())
        except:
            h=open("./mespages/mynav.html",'r')
            Program.set_menu(h.read())
        header=Program.get_header
        content=Program.get_content
        footer=Program.get_footer
        layout=Program.get_layout()
        if layout == False:
            print("content")
            try:
                html=decode_any_string(myparams(content()))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=myparams(content()).encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=myparams(content())
        else:
            html="<!doctype html>"
            html+="<html>"
            html+="<head>"
            html+="<meta charset=\"UTF-8\">"
            html+="<title>"
            print("title")
            html+=title()
            html+="</title>"
            html+="<link rel=\"icon\" href=\"/images/logo.png\">"
            html+="<link rel=\"stylesheet\" href=\"/css/css.css\"/>"
            html+=Program.get_css()
            html+="</head>"
            html+="<body>"
            print("header")
            try:
                html+=decode_any_string(header())
            except UnicodeEncodeError as e:
                print(type(e))
                print('header gerer cette erreur')
                html+=header().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=header()
            html+="<main>"
            print("content")
            try:
                html+=decode_any_string(myparams(content()))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=myparams(content()).encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=myparams(content())
            print("footer")
            print("type footer")

            print(type(force_to_unicode(footer())))

            try:
                html+=decode_any_string(footer())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=footer().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=footer()
            print("footer ajouté")
            html+="</main>"
            print("type menu")
            print(type(Program.get_menu()))
            try:
                html+=force_to_unicode(Program.get_menu())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=Program.get_menu().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=Program.get_menu()
            print("meu ajouté")
            html+="<script src=\"/js/jquery.js\"></script>"
            html+="<script src=\"/js/js.js\"></script>"
            html+=Program.get_js()
            html+="</body>"
            html+="</html>"
            #print(html)
            print("fin balise")
        result = re.search('<li class=\"mycat\">(.*?)</li>', html)
        #print(result.group(1))
        __words__ = result.group(1) if result is not None else ''
        print("===words")
        #print(__words__)
        mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        print(mychemin)
        #try:
        #    s1=(html)
        #except Exception as e:
        #    print(e)
        #    s1=(html)
        #    print(type(s1))
        #s1=(html).encode("ascii", "ignore")
        print(type(html))
        if isinstance(html,str):
            s1=html
        else:
            s1=html.encode('utf-8')
        return s1
        #f=codecs.open(mychemin,'w')

        #print(type(s1))
        #f.write(s1)
        #f.close()
        #if (__words__).rstrip() == "Full Menu":
        #print(Program.get_path())
    except Exception as e:
        print(e,'erreru')
menuburger=[
{'url':'fullmenu', 'title': "Full Menu",'myurl':"pages/menu/fullmenu.html"},
{'url':'recents', 'title': "Recents",'myurl':"pages/menu/recents.html"},
{'url':'favorite', 'title': "Favorite",'myurl':"pages/menu/favorite.html"},
{'url':'featured', 'title': "Featured",'myurl':"pages/menu/favorite1.html"},
{'url':'family', 'title': "Family bundles",'myurl':"pages/menu/favorite2.html"},
{'url':'flame', 'title': "Flame grilled burgers",'myurl':"pages/menu/favorite3.html"},
{'url':'chicken', 'title': "Chicken & more",'myurl':"pages/menu/favorite4.html"},
{'url':'sides', 'title': "Sides",'myurl':"pages/menu/favorite5.html"},
{'url':'drinks', 'title': "Drinks & coffee",'myurl':"pages/menu/favorite6.html"},
{'url':'sweets', 'title': "Sweets",'myurl':"pages/menu/favorite7.html"},
{'url':'king', 'title': "King Jr.",'myurl':"pages/menu/favorite8.html"}
]

# SQL command to create a table in the database
f=codecs.open(path1+"/mespages/dump.sql")
sql_command = f.read()
global myroutes

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


def myparams(x):
    myvar={
    'monemailici': Program.get_email(),
    'monuseridici': Program.get_userid()
    }
    for y in myvar:
        x=x.replace(y,myvar[y])
    return x
global accountinfo
def accountinfo(query_components):
    try:

        myaccountinfo()
    except Exception as e:
        print("erreur account info",e)
global signinuser
def signinuser(params):
    try:
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
global savegiftcard
def savegiftcard(query_components):
    try:
        print("save gift card",query_components["numero"])
        if query_components.get("numero"):
            numero=query_components.get("numero")[0]
            sql="select * from giftcards where numero = '%s'" % (numero)
            crsr.execute(sql)
            connection.commit()
            data=crsr.fetchall()
            if len(data) > 0:
                card=data[0]
                cardid=card[0]
                userid=session.current_user[0]
                sql="update giftcards set user_id = '%s' where id = %s" % (userid,cardid)
                crsr.execute(sql)
                connection.commit()
                Program.set_json({"ok":"1"})
            else:
                card=None
                Program.set_json({"ok":"0"})
            print("save giftcard")
            Program.set_mimetype("json")
            return Program
    except Exeption as e:
        print("erreur save gift card",e)
def savepayment(query_components):
    try:
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
            sql="insert into creditcards (nom,zip,creditcard,cvv,datecard,user_id) values ('%s', '%s', '%s', '%s', '%s','%s')" % (nom,zip,creditcard,cvv,mmyy,session.current_user[0])
            crsr.execute(sql)
            connection.commit()
            Program.set_json({"ok":"1"})
        else:
            Program.set_json({"ok":"0"})
        Program.set_mimetype("json")
        return Program
    except Exception as e:
        print("erreur save payment method",e)
global savemyinfo
def savemyinfo(query_components):
    try:
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
                session.current_user=ant[0]
                Program.set_current_user(ant[0])
                print("hello")
                Program.set_json({"sauve":"1"})
            except Exception as e:
                print("erreur save data",e)
                Program.set_json({"sauve":"0"})
            Program.set_mimetype("json")
            return Program
    except Exception as e:
        print("erreur save data",e)
global setcookie
def setcookie(query_components):
    try:
        print("set cookie",query_components["user"])
        if query_components.get("user"):
            token=query_components.get("user")[0]

            crsr.execute("select * from users where user_number = '" + str(token) + "'")
            connection.commit()
            user=crsr.fetchall()[0]

            return "<html></html>"

    except:
        print("erreur set cookie")

global confirmjwt
def confirmjwt(query_components):
    try:
        print("sign sign up",query_components["token"])
        if query_components.get("token"):
            token=query_components.get("token")[0]

            crsr.execute("select * from users where token = '" + str(token) + "'")
            connection.commit()
            user=crsr.fetchall()[0]
            session.current_user=user
            Program.set_current_user(user)
            user_number=user[0]
            prenom = user[1]
            email = user[2]
            offres = user[5]
            #user = crsr.fetchall()
            print("envoyer le code bk")
            bkcode=user[3]
            session.current_user=user

            # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
            host_smtp = "smtp.gmail.com"
            port_smtp = 587
            email_smtp = "mary.goudon@gmail.com" # Mon email Gmail
            mdp_smtp = "eljlkuznppklsquw"  # Mon mot de passe

            # Configuration du mail
            Program.set_path("./mespages")
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
            Program.set_path("./")

            Program.set_url("/")
            Program.set_redirect("/")
            #Program.set_redirect("/signinuser?user_number=" + str(user_number))
            Program.set_mimetype(None)
            return Program
            #return confirmotp(email)

    except Exception as e:
        print("erreur confirm jwt",e)
global signup_user
def signup_user(query_components):
    global Program
    try:
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
            Program.set_url(urlconfirmjwt)

            #confirmotp(data_string)
            print("set redirect ICI")
            Program.set_redirect("/confirm-jwt?token="+str(token))
            return Program
    except Exception as e:
        print("erreur sign up",e)
global aftersignup
def aftersignup(query_components):
    try:
        print(query_components)
        print("validate code",query_components.get("email"))
        Program.set_js("")

        fff=open(path1+"/mespages/header.html")
        myheader=fff.read()

        Program.set_header(myheader)

        Program.set_json({"ok":"1"})
    except Exception as e:
        print("erreur after signup",e)

global checkuser
def checkuser(query_components):
    try:
        print(query_components)
        print("validate code",query_components.get("email"))
        if query_components.get("email"):
            email=query_components.get("email")[0]
            crsr.execute("SELECT * FROM users where email = '"+str(email)+"'")
            connection.commit()
            users=crsr.fetchall()
            mytype="json"
            if len(users) == 0:
                Program.set_json({"usernotexist":"1"})
            else:
                Program.set_json({"usernotexist":"0"})
            return Program
    except Exception as e:
        print("erreur validate code",e)

global checkemail

def checkemail(query_components):
    try:
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
global signmein
def signmein(query_components):
    try:
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
                Program.set_userid(user[0][0])
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
                Program.set_redirect("/signinuser?user_number=" + str(user_number)+"&bkcode="+str(bkcode))

                Program.set_json(None)
                Program.set_mimetype(None)
                return Program
    except Exception as e:
        print("erreur sign me in",e)
global refreshmyorders
def refreshmyorders(query_components):
    sql_command = "select  orders.user_id as userid, burgers.name as itemname, orders.id as orderno, burgers.image as burgerimage, burgers.prix as burgerprice, (o.qty*burgers.prix) as price, o.qty as qte, orders.dateorder as dateorder from orders left join orderitems o on o.order_id = orders.id left join burgers on o.burger_id = burgers.burger_number where orders.user_id = %s"
    message_else="Commencez une nouvelle commande maintenant !"
    tablename="orders"
    mystr="okokokokok"
    mystr="<div id=\"mydiv\">"+display_collection(sql_command, (str(session.current_user[0])), "_order", message_else, tablename,"orderid","_orderid.html")+"</div>"
    try:
        Program.set_content(force_to_unicode(mystr))
        Program.set_mimetype("html")
        Program.set_layout(False)
        return Program
    except Exception as e:

        print("erreur",e)
    print("okokokok")
global showburger
def showburger(query_components):
    print("show menu",query_components)
    dataparams={"1":"burger1=sandwich&burger2=sandwich&drink1=small&drink2=small&side1=small&side2=small","2":"burger=burger","3":"burger=burger","4":"burger=side","5":"burger=drink","6":"burger=sweet","7":"burger=burger&jrsides=jrsides&jrdrinks=jrdrinks&jrtreats=toy"}
    Program.set_title("Burger King")
    print("burger king")
    Program.add_css("burger.css")
    Program.add_js("burger.js")
    Program.set_path("./mespages")

    print('hi')
    Program.set_header_with_path("headersignin.html")
    Program.set_header(Program.get_header().replace("\"/\"","\"/menu\""))
    Program.set_footer_with_path("footer.html")
    burgerid=str(query_components.get("burgerid")[0])
    sql_command = "select * from burgers where burger_number = %s" % (burgerid)
    crsr.execute(sql_command)
    connection.commit()
    res=crsr.fetchall()
    message_else=""
    tablename="burgers"
    Program.set_path("./mespages")
    matable=infotable(tablename)
    contentpage=force_to_unicode(get_file("burger.html").read())
    contentpage=contentpage.replace("<!-- myparams -->",dataparams[res[0][7]]+"&burgerid="+str(res[0][0]))
    sql_command = "select * from nutinfos where burger_id = %s" % (burgerid)
    tablename="nutinfos"
    message_else="Aucune information n'est disponible."
    collectionstr= display_collection(sql_command, (), "_infonutrition", message_else, tablename)

    contentpage=contentpage.replace("info nutritionnelle ici",collectionstr)
    sql_command = "select * from burgers where burgercat_id in (%s,%s) and burger_number = %s" % ("2","3",burgerid)
    tablename="burgers"
    message_else=""
    collectionstr= display_collection(sql_command, (), "_combosize", message_else, tablename)
    contentpage=contentpage.replace("<!-- size combo here -->",collectionstr)

    sql_command = "select * from burgers where burgercat_id in (%s,%s) and burger_number = %s" % ("4","5",burgerid)
    collectionstr= display_collection(sql_command, (), "_valuesize", message_else, tablename)
    contentpage=contentpage.replace("<!-- size item here -->",collectionstr)
    sql_command = "select burgers.* from burgers where burger_number = %s and burgers.burgercat_id = %s" % (burgerid,1)
    collectionstr= display_collection(sql_command, (), "_customizeburger", message_else, tablename)
    contentpage=contentpage.replace("<!-- personnaliser votre burger -->",collectionstr)


    if len(res) > 0:
        for re in res:
            paspremier = False
            contentpage=force_to_unicode(contentpage)
            for x in range(len(re)):
                print(x)
                print(re[x])
                z=re[x]
                strrep=force_to_unicode("(%s)" % (matable[x][1]))
                print(strrep)
                if type(z) == int or type(z) == float:
                    z=str(z)
                if z is not None:
                    contentpage=contentpage.replace(strrep, force_to_unicode(z))
    Program.set_content(contentpage)
    #=======
    return Program

    #connection.commit()
global showmenu
def showmenu(query_components):
    print("show menu",query_components)
    Program.set_title("Burger King")
    print("burger king")
    Program.set_path("./mespages")
    print('hi')
    Program.set_header_with_path("header.html")
    Program.set_footer_with_path("footer.html")
    sql_command = "select * from burgercats"
    message_else=""
    tablename="burgercats"
    Program.set_path("./mespages")

    contentpage=force_to_unicode(get_file("menu.html").read())
    mytabs=display_collection(sql_command, (), "_burgercat", message_else, tablename)
    #=======
    if query_components.get("mytab") is not None:
        x=query_components.get("mytab")[0]
    else:
        x=""
    print("")
    print("my tab name:",x)
    if x == "fullmenu":
        sql_command = "select * from burgercats"
        message_else="Il n'y a aucune catégorie"
        tablename="burgercats"
        myitems=display_collection(sql_command, (), "_myburgercat", message_else, tablename)
        contentpage=contentpage.replace("my items here",myitems)
    elif x == "recents" and query_components.get("userid") is not None:
        sql_command = "select * from burgers left join user_recents u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
        message_else="commencez une commande pour voir les items ici<a href=\"/store-locator\">commencez à commander</a>"
        tablename="burgers"
        myarguments=(str(query_components.get("userid")[0]))
        myitems=display_collection(sql_command, myarguments, "_burger", message_else, tablename)
        contentpage=contentpage.replace("my items here",myitems)
    elif x == "recents":
        myitems="<h2>Sign In to Save Recents</h2><h3>Sign up or sign in to save your recents.</h3><a href=\"/signin\">Sign in</a>"
        contentpage=contentpage.replace("my items here",myitems)
    elif x == "favorites" and query_components.get("userid") is not None:
        sql_command = "select * from burgers left join user_favs u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
        message_else="Favorisez un article de votre panier ou des articles récents pour l'enregistrer en tant que favori."
        tablename="burgers"
        myarguments=(str(query_components.get("userid")[0]))
        myitems=display_collection(sql_command, myarguments, "_burger", message_else, tablename)
        contentpage=contentpage.replace("my items here",myitems)
    elif x == "favorites":
        myitems="<h2>Sign In to Save Favorites</h2><h3>Sign up or sign in to save your favorites.</h3><a href=\"/signin\">Sign in</a>"
        contentpage=contentpage.replace("my items here",myitems)

    elif query_components.get("catid") is not None:
        sql_command = "select * from burgers where burgercat_id = %s"
        message_else="Il n'y a aucun item < a href=\"/menu\">Retour au menu</a>"
        tablename="burgers"
        myitems=display_collection(sql_command, (str(query_components.get("catid")[0])), "_burger", message_else, tablename)
        contentpage=contentpage.replace("my items here",myitems)

    #=======

    contentpage=contentpage.replace("my tabs here",mytabs)

    try:
        Program.set_content(force_to_unicode(contentpage))
        Program.set_mimetype("html")
        Program.set_footer("")
        Program.add_css("mymenu.css")
        return Program
    except Exception as e:

        print("erreur",e)
    print("okokokok")
    #connection.commit()
global myorders
def myorders(query_components):
    sql_command = "select orders.user_id as userid, burgers.name as itemname, orders.id as orderno, burgers.image as burgerimage, burgers.prix as burgerprice, (o.qty*burgers.prix) as price, o.qty as qte, orders.dateorder as dateorder from orders left join orderitems o on o.order_id = orders.id left join burgers on o.burger_id = burgers.burger_number where orders.user_id = %s"
    message_else="Commencez une nouvelle commande maintenant !"
    tablename="orders"

    mystr="<div id=\"mydiv\">"+display_collection(sql_command, (str(session.current_user[0])), "_order", message_else, tablename,"orderid","_orderid")+"</div>"
    try:
        Program.add_js("orders.js")
        Program.add_css("orders.css")
        Program.set_path("./mespages")
        k=get_file("orders.html")
        text=force_to_unicode(k.read())
        text=text.replace("les commandes apparaissent ici",mystr)

        Program.set_content(text)
        return Program
    except Exception as e:

        print("erreur",e)
    print("okokokok")
    #connection.commit()
global insertburger
def insertburger(query_components):
    if query_components.get("burgername"):
        data_string = query_components["burgername"][0]
        sql_command = """INSERT INTO burgers (name) VALUES ('""" + data_string + """');"""
        print("ok ok")
        crsr.execute(sql_command)
        connection.commit()
        try:
            print("jom")
            crsr.execute("SELECT * FROM burgers")
            mycontent="<main><ul>"
            # store all the fetched data in the ans variable
            ans = crsr.fetchall()

            for myburger,name1,image1,description1,prix1 in ans:
                mycontent+= "<li>"+name1+"</li>"
            mycontent+="</ul></main>"
            #print(mycontent)
            #Program.path("./")
            print("ok")
            print("yeah")
            Program.set_content(mycontent)
            return render_figure("index.html")
        except Exception as e:
            print("erreur",e)
        print("okokokok")
        #connection.commit()

global listburger
def listburger(burger):
    try:
        print(" list brger")
        print(type(burger[0]))
        print(type(burger[1]))
        print(type(burger[1].encode("utf-8")))
        s= "<li><a href=\"/burgers/"+str(burger[0])+"\">"+(burger[1].encode('utf-8'))+"</a></li>"
        print(type(s))
        return s
    except Exception as e:
        print("erreur list brger",e)


def ajoutlistburger(burger):
    try:
        print("ajout list brger")
        print(type(burger[1]))
        return "<li>"+burger[1]+"</li>"
    except Exception as e:
        print("erreur ajout burger",e)

# execute the statement
for sql in sql_command.split(";"):
    print(sql)
    try:
        crsr.execute(sql)
    except Exception as e:
        print(e)

connection.commit()
for cat in menuburger:
    crsr.execute(""" insert or ignore into cats (name,url) values ('"""+cat['title']+ """','"""+cat['url']+ """');""")
    connection.commit()
# close the connection
#connection.close()
#s = 'asdf=5;iwantthis123jasd'
#result = re.search('asdf=5;(.*)123jasd', s)
#print(result.group(1))
global displaythisburger
def displaythisburger(burger,catname,catid):
    try:
        print("display this burger")
        print(type(catid))
        print(type(catname))
        print(type(burger[0]))
        print(type(burger[1]))
        print(type(burger[2]))
        print(type(burger[3]))
        print(type(burger[4]))
        print(type(burger[5]))
        text="<a href=\"/menu/"+repr(catid)+"\">retour au menu "+catname+"</a>"
        text+=mycard(burger[1],str(burger[4])+"€","min "+str(burger[5])+" cal")
        Program.set_path("./burgers")
        Program.set_content(text)
        return render_figure(str(burger[0])+".html")
    except Exception as e:
        print('erreur display burger',e)
def card(title,description,button):
    try:
        f=codecs.open(path1+"/mespages/card.html")
        s=f.read()
        result = re.search('<h3 class="title">(.*)</h3>', s)
        montitre=(result.group(1) if result is not None else "")
        result = re.search('<p class="subtitle">(.*)</p>', s)
        mysubtitle=(result.group(1) if result is not None else "")
        result = re.search('<a href="">(.*)</a>', s)
        mylink=result.group(1) if result is not None else ""

        html=s.replace(montitre,title).replace(mysubtitle,description).replace(mylink,button)
        return html
    except Exception as e:
        print("erreur card",e)
        return ""
def mycard(title,description,content):
    try:
        f=codecs.open(path1+"/mespages/card.html")
        s=f.read()
        result = re.search('<h3 class="title">(.*)</h3>', s)
        montitre=(result.group(1) if result is not None else "")
        result = re.search('<p class="subtitle">(.*)</p>', s)
        mysubtitle=(result.group(1) if result is not None else "")
        result = re.search('<p class="text">(.*)</p>', s)
        mylink=result.group(1) if result is not None else ""
        print(montitre+" "+mysubtitle+" "+mylink)
        print(title)
        print(description)
        print(content)
        #print(title+" "+description+" "+content)
        html=(s).replace(montitre,(title))
        #html=(s).replace(montitre,(title)).replace(mysubtitle,(description)).replace(mylink,(content))
        print(type(html))
        return html
    except Exception as e:
        print("erreur card",e)
        return ""

def bootstrapjs(params = None):
    h="""  """
    return h

def bootstrapcss(params = None):
    h="""  """
    return h

def render_pages(params = None):
    home()
    menu()
    signup()
    signin()
    erreur404()
    myaccountinfo()
def copy(params = None):
    os.system("cp "+path1+"/mespages/js.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/css/css.css "+path1+"/css/css.css")
    os.system("cp "+path1+"/mespages/css/signin.css "+path1+"/css/signin.css")
    os.system("cp "+path1+"/mespages/css/*.css "+path1+"/css")
    os.system("cp "+path1+"/mespages/*.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/userconnecte.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/signin.js "+path1+"/js")

Program=directory("Burger King")
#Program.path("./")
class Header:
    global set_my_header
    global set_my_footer

    def set_my_header(headername):
        try:
            Program.set_path("./mespages")
            fff=get_file(headername+".html")
            myheader=fff.read()
            Program.set_header(myheader)
        except IOError:
            Program.set_header("")

    def set_my_footer(headername):
        try:
            Program.set_path("./mespages")
            fff=get_file(headername+".html")
            myfooter=fff.read()
            Program.set_footer(myfooter)
        except IOError:
            Program.set_footer("")

class Page:
    global erreur404
    def erreur404(params = None):
        try:
            print("erreur 202")
            Program.set_path("./mespages")
            j=get_file("404.html")
            print("my file")
            text=j.read()
            Program.set_path("./css")
            Program.add_css("404.css")

            Program.edit_title("Page non trouvée")
            Program.set_content(text)
            print("my path")
            set_my_header("")
            print("my footer")
            set_my_footer("")
            print("my path1")
            Program.set_path("./erreur")
            print("my path")
            return render_figure("404.html")

        except Exception as e:
            print("errur my 404",e)
    global addgiftcard
    def addgiftcard(params = None):
        Program.set_path("./mespages")
        j=codecs.open(Program.get_filename_path("addgiftcard.html"))
        Program.add_css("signin.css")
        Program.add_js("addcard.js")
        Program.add_css("addgiftcard.css")
        text=j.read()
        Program.set_content(force_to_unicode(text))
        Program.set_path("./mespages")
        k=codecs.open(Program.get_filename_path("headeroverlay.html"))
        headertext=k.read()
        Program.set_header(headertext)

        return render_figure("ma page.html")
    global addcard
    def addcard(params = None):
        try:
            Program.set_path("./mespages")
            j=codecs.open(Program.get_filename_path("addcard.html"))
            Program.set_path("./css")
            Program.add_css("signin.css")
            Program.add_css("addcard.css")
            Program.add_js("addcard.js")
            text=force_to_unicode(j.read())
            Program.set_content(text)
            Program.set_path("./mespages")
            k=codecs.open(Program.get_filename_path("headeroverlay.html"))
            headertext=k.read()
            Program.set_header(headertext)

            return render_figure("ma page.html")
        except:
            print("erreur add card")
    global accountpayment
    def accountpayment(params = None):
        try:
            print("account payment: current user")
            print(session.current_user)
            Program.set_path("./mespages")
            j=codecs.open(Program.get_filename_path("accountpayment.html"))
            Program.set_path("./css")
            Program.set_css("")
            Program.add_css("accountpaiement.css")
            text=force_to_unicode(j.read())
            #sql,templatename,errormessage,tablename
            mysql="select * from creditcards where orders.user_id = %s" % (session.current_user[0])
            str=display_collection(mysql,(),"_modedepaiement","Aucun mode de paiement n'a été ajouté","creditcards")
            text=text.replace("ici le mode de paiement",str)
            Program.set_content(text)
            Program.set_path("./mespages")
            k=codecs.open(Program.get_filename_path("headersignin.html"))
            headertext=k.read()
            Program.set_header(headertext)

            return render_figure("my page.html")
        except Exception as e:
            print("account payment erreur",e)
    global myaccountinfo
    def myaccountinfo(params = None):
        try:
            print("account info: current user")
            print(session.current_user)
            Program.set_path("./mespages")
            j=codecs.open(Program.get_filename_path("accountinfo.html"))
            text=j.read()
            Program.set_css("")
            Program.set_path("./css")
            Program.add_css("account.css")
            Program.add_css("signin.css")
            Program.set_path("./js")
            Program.add_js("saveinfo.js")
            Program.edit_title("Account Details")
            try:
                if session.current_user is not None:
                    for a in range(len(session.current_user)):
                        try:
                            if session.current_user[a] is not None:
                                idstring="id=\""+force_to_unicode(table_users[a][1])+"\""
                                print(idstring)
                                idvaluestring=(idstring+" value=\""+str(session.current_user[a])+"\" ")
                                if force_to_unicode(table_users[a][1]) == u'offres':
                                    text=text.replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=force_to_unicode(text).replace(idstring,idvaluestring)

                                if force_to_unicode(table_users[a][1]) == u'dateofbirth':
                                    date=session.current_user[a].split(" ")[0]
                                    print("date : "+date)
                                    idstring="id=\""+"yy"+"\""
                                    idvaluestring=(idstring+" value=\""+date.split("-")[0]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                    text=force_to_unicode(text).replace(idstring,idvaluestring)
                                    idstring="id=\""+"mm"+"\""
                                    idvaluestring=(idstring+" value=\""+date.split("-")[1]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                    text=force_to_unicode(text).replace(idstring,idvaluestring)
                                    idstring="id=\""+"dd"+"\""
                                    idvaluestring=(idstring+" value=\""+date.split("-")[2]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                    text=force_to_unicode(text).replace(idstring,idvaluestring)

                        except Exception as e:
                            print("mon texte erreur",e)
            except:
                print("erreur afficher le formulaire")
            Program.set_content(text)
            Program.set_path("./accountinfo")
            set_my_header("headersignin")
            set_my_footer("footer")
            return render_figure("index.html")

        except Exception as e:
            print("erreur my account info page",e)
    global home
    def home(params = None):
        try:
            Program.set_path("./")
            print("home")
            Program.set_title("Burger King")
            print("burger ing")
            Program.set_path("./mespages")
            print('hi')
            Program.set_header_with_path("header.html")
            Program.set_footer_with_path("footer.html")

            j=codecs.open(Program.get_filename_path("index.html"))
            text=j.read()
            print("my text")
            result = re.search("<div class=\"burgers-list\">(.*)</div>",text)
            #print(result.group(1))
            crsr.execute("SELECT * FROM burgers")
            mycontent="<ul>"
            # store all the fetched data in the ans variable
            print("burgersok")
            ans = crsr.fetchall()
            print("burgers")
            for myburger in ans:
                mycontent+= ajoutlistburger(myburger)
            print("burgervalue")
            mycontent+="</ul>"
            print(mycontent)
            if result is not None and len(result.group(1)) > 0:
                text=text.replace(result.group(1),mycontent)
            print("cards1")
            crsr.execute("SELECT * FROM cards")
            print("cards")
            mycontent=""
            # store all the fetched data in the ans variable
            ans = crsr.fetchall()
            print("allcards")
            print("cads")
            for x in ans:
                mycontent+= card(x[1],x[2],x[3])
            #print(mycontent)
            result = re.search("<div class=\"mycards\">(.*)</div>",text)
            if result is not None:
                print(result)
                print(result.group(1))
                if len(result.group(1)) > 0:
                    text=text.replace(result.group(1),mycontent)
            Program.set_path("./")
            Program.set_content(text)

            text=(text)
            print("render figure home")
            return render_figure("index.html")
        except Exception as e:
            print("erreur 1",e)
    global menu
    def menu(params = None):
        try:
            Program.set_title("Burger King")
            Program.set_path("./mespages")
            j=codecs.open(Program.get_filename_path("menu.html"))
            text=j.read()
            result = re.search("<nav class=\"mytabs\"><ul>(.*)</ul></nav>",text)
            #print(result.group(1))
            crsr.execute("SELECT * FROM cats")
            mycontent=""
            # store all the fetched data in the ans variable
            print("burgersok")
            ans = crsr.fetchall()
            print("burgers")
            for myburger in ans:
                #print("burger",myburger[1],mycontent)
                mycontent+= "<li class=\"mycat\"><a href=\"/menu/"+repr(myburger[0] if myburger[0] > 1 else '')+"\">"+(myburger[1]).encode('utf-8')+"</a></li>"
            if result is not None and len(result.group(1)) > 0:
                text=text.replace(result.group(1),mycontent)
            for myburger in ans:
                mesburgers=""
                print("burger?!%*#")
                crsr.execute("SELECT * FROM burgers where cat_id = '"+repr(myburger[0])+"'")
                res=re.search("<div class=\"myitems\"><ul>(.*?)</ul></div>",text)
                ans1 = crsr.fetchall()
                for burger in ans1:
                    #print("burger",burger[1])
                    print("erreur ici")
                    displaythisburger(burger,myburger[1],myburger[0])
                    print("myerreur")
                    mesburgers+= listburger(burger)
                    print("erreur")
                if mesburgers == "":
                    mesburgers = "mes items ici"
                if res is not None and len(res.group(1)) > 0:
                    text=text.replace(res.group(1),mesburgers)
                print("burgervalue")
                #print(myburger[1])

                Program.set_path("./menu")
                Program.set_content(text)
                page=str(myburger[0] if myburger[0] > 1 else 'index')
                return render_figure(page+".html")
        except Exception as e:
            print("erreur menu",e)
    global confirmotp
    def confirmotp(params=None):
        try:
            print("confirm otp func")
            print(params)
            print(session.current_user)
            email=session.current_user[2]
            print(email)
            if email is not None:
                Program.set_title("Burger King")
                Program.set_path("./mespages")
                print("confirm otp")
                f=open(Program.get_filename_path("userconnecte.js"))
                js=f.read()
                print("user connectes")
                Program.set_email(email)
                print("email")
                ff=open(Program.get_filename_path("confirmotp.html"))
                text=ff.read()
                print("text length : "+str(len(text)))
                Program.set_js("")
                fff=open(Program.get_filename_path("headersignin.html"))
                myheader=fff.read()
                print("header")
                Program.set_header(myheader)
                Program.set_path("./css")
                Program.add_css("signin.css")
                Program.set_path("./js")
                Program.add_js("signin.js")
                Program.set_footer("")
                Program.set_path("./signup")
                Program.set_mimetype("html")
                print("confirm otp return program")
                Program.set_content(unicode(text,'utf-8'))
                return Program
        except Exception as e:
            print("erreur confirm otp",e)
    global signup
    def signup(params = None):
        try:
            print("sign up")
            Program.set_path("./mespages")

            f=open(Program.get_filename_path("userconnecte.js"))
            js=f.read()
            fff=open(Program.get_filename_path("headersignin.html"))
            myheader=fff.read()

            ff=open(Program.get_filename_path("/signup.html"))
            text=ff.read()
            Program.set_title("Burger King")
            Program.set_js("")
            Program.set_header(myheader)
            Program.set_path("./css")
            Program.add_css("signin.css")
            Program.set_path("./js")
            Program.add_js("signin.js")
            Program.set_footer("")
            Program.set_path("./signup")
            Program.set_content(unicode(text,'utf-8'))
            return render_figure("index.html")
        except Exception as e:
            print("erreur sign in",e)
    global signin
    def signin(params = None):
        try:
            print("sign in")
            Program.set_path("./mespages")
            f=open(Program.get_filename_path("userconnecte.js"))
            js=f.read()
            fff=open(Program.get_filename_path("headersignin.html"))
            myheader=fff.read()
            Program.set_title("Burger King")

            ff=open(Program.get_filename_path("signin.html"))
            text=ff.read()
            Program.set_js("")
            Program.set_header(myheader)
            Program.set_path("./css")
            Program.add_css("signin.css")
            Program.set_path("./js")
            Program.add_js("signin.js")
            Program.set_footer("")
            Program.set_path("./signin")
            Program.set_content(text)
            return render_figure("index.html")
            Program.set_css("")
            Program.set_js("")
        except Exception as e:
            print("erreur sign in",e)
    global code
    def code(params = None):
        try:
            print("code")
            Program.set_path("./mespages")
            f=open(Program.get_filename_path("userconnecte.js"),'r')
            js=f.read()
            Program.set_title("Burger King")

            ff=open(Program.get_filename_path("code.html"),'r')
            text=ff.read()
            Program.set_path("./js")
            Program.add_js("userconnecte.js")
            Program.set_header(Program.get_header())
            Program.set_footer(Program.get_footer())
            Program.set_path("./code")
            Program.set_content(unicode(text,'utf-8'))
            return render_figure("index.html")
        except Exception as e:
            print("erreur 3",e)
    global offers
    def offers(params = None):
        try:
            print("offers")
            Program.set_header(Program.get_header())
            Program.set_footer(Program.get_footer())
            Program.set_path("./offers")
            Program.set_content("")
            return render_figure("index.html")
        except:
            print("erreur 4")
    global rewards
    def rewards(params = None):
        try:
            Program.set_title("Burger King")

            print("rewards")
            Program.set_path("./rewards")
            Program.set_content("")
            return render_figure("index.html")
        except:
            print("erreur 5")
class S(BaseHTTPRequestHandler):
    def _set_headers(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()

    def do_GET(self):
        print("=========new route GET====================")

        try:
            Program=directory("Burger King")
            #Program.path("./")
            Program.set_url(self.path)
            urlpath=self.path
            myurlpath=urlpath.split("?")[0]

            #f = open("index.html", "r")
            query_components = parse_qs(urlparse(urlpath).query)
            print(query_components,"what params")
            x=searchmyparams(query_components,myurlpath)
            if x:
                print(x)
                query_components=x[1]
                myurlpath=x[0]

            try:
                query_components["userid"]=[session.current_user[0]]
            except:
                print("aucun user connecté")
            #print(query_components)
            try:
                insertburger(query_components)
            except KeyError:
                print("erreur 6")
            print(myurlpath)
            try:
                print(" route_post={")
                print('my path')
                print(myurlpath)
                if myroutes.get(myurlpath) is not None:
                    codehtml=myroutes.get(myurlpath)(query_components)

            except KeyError:
                print("erreur 6")
            #try:
                #x=myroutes.get(urlpath.split("?")[0])
                #if x is not None:
                #    Program.set_url(x)
            #except:
            #    print("pas d'autre route")
            print(urlpath)
            print('my url get')
            #self.data_string = params
            #os.system("echo \""+urlpath+"\"")
            copy()
            #render_pages()
            #myaccountinfo()
            #home()

            print("rendere")

            if myroutes.get(myurlpath) is not None:
                print("code html pour"+urlpath)
                res=myroutes.get(myurlpath)(query_components)
                if isinstance(res,str):
                    print('is code html')
                    codehtml=decode_any_string(force_to_unicode(codehtml))
                elif isinstance(res,object):
                    print("is object")
                    print(res)
                    Program=res
                    if Program.get_current_user() is not None:
                        print("current_user")
                        print(Program.get_current_user())
                        session.current_user=Program.get_current_user()
                    html=render_figure("my file.html")
                    print(html)
                    codehtml=decode_any_string(force_to_unicode(html))
                    print(len(codehtml))
                try:
                    code=(codehtml.decode("utf-8"))
                except UnicodeEncodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    code=(codehtml.encode('utf-8'))
                except UnicodeDecodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    code=(codehtml)
            if Program.get_mimetype() is not None:
                mytype=Program.get_mimetype()
            else:
                mytype=urlpath.split(".")[-1]
            print(mytype)



            print("Program.get json")
            print(Program.get_json() is None)
            print("mytype")
            print(mytype)
            print(switcher.get(mytype))


            print(myroutes.get(urlpath))
            if switcher.get(mytype) is None:
                mytype="html"
            print("get redirect "+str(Program.get_redirect()))
            if str(Program.get_redirect()) == 'None':
                if mytype != "html":
                    if switcher.get(mytype) is not None:
                        print("trouver fichier")
                        self._set_headers(switcher.get(mytype))
                        self.wfile.write(Program.trouver_fichier(urlpath,myroutes).read())
                elif route_post.get(urlpath) and Program.get_json() != "null":
                    print("return json")
                    x=Program.get_json()
                    Program.set_json(None)

                    self._set_headers(switcher.get("json"))
                    self.wfile.write(x)
                else:
                    print("my html page")
                    print(mytype)


                    self._set_headers(switcher.get(mytype))
                    self.wfile.write(code)
            else:
                print("reirect is not none")
                self.send_response(301)
                myred=Program.get_redirect()
                self.send_header('Location',myred)
                Program.set_redirect(None)
            self.end_headers()

            Program.set_js("")
        except UnboundLocalError as e:
            print("erreur get",e)
            k=get_file_dir("404.html","./erreur")
            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read())
    def do_HEAD(self):
        self._set_headers()
    def do_POST(self):
        print("=========new route POST====================")

        try:
            Program=directory("Burger King")
            Program.set_url(self.path)
            urlpath=Program.get_url()

            query_components = parse_qs(urlparse(urlpath).query)
            x=searchmyparams(query_components,urlpath)
            if x:
                print(x)
                query_components=x[1]
                urlpath=x[0]
            try:
                query_components["userid"]=[session.current_user[0]]
            except:
                print("aucun user connecté")
            print "in post method"
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            fields = parse_qs(self.data_string)
            myurlpath=urlpath.split("?")[0]
            try:
                print('my path')
                print(myurlpath)
                print(route_post.get(myurlpath))
                if route_post.get(myurlpath) is not None:
                    print("route trouve")
                    print(fields)
                    res=route_post.get(myurlpath)(fields)
                    if isinstance(res,str):
                        codehtml = res
                        print("is code HTML")
                        #print(codehtml)
                    elif isinstance(res,object):
                        print("is object")
                        print(res)
                        Program=res
                        if Program.get_current_user() is not None:
                            print("current_user")
                            print(Program.get_current_user())
                            session.current_user=Program.get_current_user()
                        #.dict2class(res.__dict__)
            except KeyError:
                print("erreur 6")


        #self.data_string = params
            urlpath=self.path
            print("redirect post:")
            print(Program.get_redirect())
            copy()
            #render_pages()
            #myaccountinfo()
            #home()
            mytype=Program.get_mimetype() or self.path.split(".")[-1]
            print(urlpath)
            print("my type")
            print(mytype)
            print("Program.get json")
            print(Program.get_json() is not None)
            print(Program.get_json())
            print(route_post.get(myurlpath))
            print("redirect")
            print(Program.get_redirect())
            print(str(Program.get_redirect()) != 'None')
            if str(Program.get_redirect()) != 'None':
                self.send_response(301)
                myred=Program.get_redirect()
                self.send_header('Location',myred)
                Program.set_redirect(None)


            elif mytype == "json":
                print("return json")
                data=Program.get_json()
                Program.set_json(None)

                self._set_headers(switcher.get("json"))
                self.wfile.write(str(data).replace("'",'"'))
            elif mytype is not None:
                if mytype != "html":
                    if switcher.get(mytype) is not None:


                        if myroutes.get(urlpath) is not None:
                            self._set_headers(switcher.get(mytype))
                            self.wfile.write(codehtml)
            else:
                print(mytype)
                self._set_headers(switcher.get(mytype))
                self.wfile.write(codehtml)
            self.end_headers()
        except UnboundLocalError:
            print("erreur post")
            k=get_file_dir("404.html","./erreur")
            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read())

        return


def run(server_class=HTTPServer, handler_class=S, port=8000,host="localhost"):
    server_address = ('', port)
    print("run erver")
    httpd = server_class(server_address, handler_class)
    #print 'http://localhost:8000'
    if len(argv) == 2:
        print 'http://'+host+':'+argv[1]
    else:
        print 'http://'+host+':'+str(port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
render_pages()
#rewards()
#offers()
print((__words__).rstrip())

myroutes = {"/customizemenu":customizemymenu,"/burger": showburger,"/menu": showmenu,
"/orders/refresh":refreshmyorders,
"/account/orders":myorders,
"/account/payment":accountpayment,
"/account/payment/add-card":addcard,
"/account/payment/add-gift-card":addgiftcard,
"/signinuser": signinuser,
"/":home,
"/":home,"/signin":signin,
            "/signup": signup,
            "/rewards": rewards,
'/account/info': myaccountinfo,
'/confirm-otp': confirmotp,
"/confirm-jwt": confirmjwt,
"/setcookie": setcookie,

'/confirm-jwt': confirmjwt
}
global route_post
route_post={
    "/savegiftcard": savegiftcard,
    "/savepayment": savepayment,
    "/signup": signup_user,
    "/signin": signmein,
    "/saveinfo": savemyinfo,
    "/aftersignup": aftersignup,
    "/confirm-otp": confirmotp,
    "/checkemail": checkemail,
    "/checkuser.json": checkuser,
    "/validatecode": validatecode
}
if len(argv) == 3:
    run(port=int(argv[1]),host=argv[2])
elif len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()

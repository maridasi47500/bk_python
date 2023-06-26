# coding: utf-8 -*-
from searchrestaurant import searchrestaurantpage
import searchrestaurant
global searchrestaurant
global findaddress
import findaddress
import address
global address
from findaddress import findaddresspage


import json
import psutil
import traceback
import logging
from erreur import erreur
import binascii
import random as rand
import smtplib
import datetime
import sys
import requests
from jsoncontent import jsoncontent
from infolocation import infolocationpage
from orderlocation import orderlocationpage
from offerslocation import offerslocationpage
from favlocation import favlocationpage
from bkaction import bkactionjson
from redirect import redirectaction
from setuser import setuserpage
global session
import sqlite3
from home import pagehome
from changeitem import changeitempage
from ingredients import ingredientpage
from servicemode import servicemodepage
from address import addresspage
from listlocation import listlocationpage
global copy
global reloadmymodules
global render_pages
global connection
global get_file
global switcher
__mots__={"/favlocation":{"partiedemesmots":"favlocation"},
    "/searchrestaurant":{"partiedemesmots":"searchrestaurant"},
"/findaddress":{"partiedemesmots":"findaddress"},
"/offerslocation":{"partiedemesmots":"offerslocation"},"/orderlocation":{"partiedemesmots":"orderlocation"},"/infolocation":{"partiedemesmots":"infolocation"},"/bkaction":{"partiedemesmots":"id"},"/listlocation":{"partiedemesmots":"listlocation"},"/redeem":{"partiedemesmots":"royalprk"},r"^/store-locator/service-mode$":{"partiedemesmots":"Emplacements"},r"^/store-locator/address$":{"partiedemesmots":"Entrez votre adresse"},r"^/store-locator$":{"partiedemesmots":"Emplacements"},"/account/info":{"partiedemesmots":"Account"},"/confirm-jwt":{"partiedemesmots":""},"/updateitem/changeitem":{"partiedemesmots":"burger"},"/updateitem/customize":{"partiedemesmots":"bacon"},"/customizemenu":{"partiedemesmots":"burger"},r"\/menu\/[0-9]*$(\/)?": {"partiedemesmots":"Personnaliser votre commande"}, r"/menu(/)([a-z]+)(/)?": {"partiedemesmots":"Hamburgers grillés à la flamme"}, r"/menu(/)?([a-z]+)?(/)?": {"partiedemesmots":"Hamburgers grillés à la flamme"},"/menu(/)?":{"partiedemesmots":"Hamburgers grillés à la flamme"},"^\/$":{"partiedemesmots":"Get rewarded like Royalty"},"/signin":{"partiedemesmots":"sign-in-form\""},"/signup":{"partiedemesmots":"J'accepte ce qui suit : Politique de confidentialité Conditions d'utilisation des récompenses Conditions d'utilisation"}}
from customizemymenu import customizemymenupage

from accountpayment import pageaccountpayment
from directory import directory
from signup_user import signup_user_page
from afficher_modepaiement import afficher_modepaiementpage
from check_email import checkemailpage
from code import codepage
from signin import signinpage
import addcard
from signup import signuppage
import signup_user
from addcard import addcardpage
from refreshmyorders import refreshmyorderspage
from myaccountinfo import myaccountinfopage
from validatecode import validatecodepage
import home
from confirmotp import confirmotppage
from menu import menupage
from confirmjwt import confirmjwtpage
import signup
print("==BK : BIENVNUE!===$$$$$$ùùù^^^")

from showmenu import showmenupage
from insertburger import insertburgerpage
from checkuser import checkuserpage
from myorders import myorderspage
from displaythisburger import pagedisplaythisburger
from showburger import showburgerpage
from signmein import signmeinpage
from signinuser import pagesigninuser
import accountpayment
from addburger import addburgeraction
from savemyinfo import savemyinfopage
from savegiftcard import savegiftcardpage
from savepayment import savepaymentpage
myredirect=["codepage"]
switcher={
'html':'text/html',
'css':'text/css',
'json':'application/json',
'js':'text/javascript',
'png':"image/png",
'gif':"image/gif",
'ico':'image/vnd.microsoft.icon'
}


connection = sqlite3.connect("mesburgers1.db")

# cursor
global crsr
crsr = connection.cursor()

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()
global force_to_unicode
global decode_any_string
def decode_any_string(text):
    try:
        print("..."+text[0:60]+"...")
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
try:
    if len(sys.argv) == 4: 
        session.current_user=[sys.argv[3]]
except:
    print("no arg")
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from os.path import exists
from urlparse import urlparse, parse_qs
import os

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception, e:
        logging.error(e)

    python = sys.executable
    os.system("kill -9 $(lsof -ti tcp:8000) && python script.py 8000 localhost 1")
    #os.execl(python, python, *sys.argv)


global path1
path1=os.getcwd()
#sys.path.append(os.path.abspath(os.getcwd()+"/pythonfile"))
#from myfunc import *
#from pagehtml import *
import codecs
import re

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


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import random
def showburger(query_components):
    Program=showburgerpage("./showburger","burger",query_components)
    #=======
    return render_figure("burger.html",Program)
# connecting to the database
def savegiftcard(query_components):
    try:
        Program=savegiftcardpage("enregistrer des cartes cadeaux")
        return Program
    except Exeption as e:
        print("erreur save gift card",e)

def myorders(query_components):
    Program=myorderspage("mes commandes")

    return Program
    #connection.commit()
def afficher_modepaiement(text,usernumber):
    return afficher_modepaiementpage(text,usernumber)
def listlocation(params):
    try:
        Program=listlocationpage(params)
        
        return render_figure("listlocation.html",Program)
    except:
        print("erreur add burger")
def bkaction(params):
    try:
        Program=bkactionjson(params)
        
        return render_figure("bk.html",Program)
    except:
        print("erreur add burger")
def addburger(params):
    try:
        Program=addburgeraction(params)
        
        return render_figure("burger.html",Program)
    except:
        print("erreur add burger")
def addcard(params = None):
    try:
        Program=addcardpage("ajouter une carte")


        return render_figure("ma page.html")
    except:
        print("erreur add card")
global home
def infolocation(params = None):
    try:
        print("render figure home")    
        Program = infolocationpage("bk",params)
        print("render figure home finish")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 1 INFO LOCAtION",e)
def orderlocation(params = None):
    try:
        print("render figure home")    
        Program = orderlocationpage("bk",params)
        Program.set_path("./")
        print("render figure home finish")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 1",e)
def offerslocation(params = None):
    try:
        print("render figure home")    
        Program = offerslocationpage("bk",params)
        Program.set_path("./")
        print("render figure home finish")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 1",e)
def favlocation(params = None):
    try:
        print("render figure home")    
        Program = favlocationpage("bk",params)
        Program.set_path("./")
        print("render figure home finish")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 1",e)
def homefunc(params = None):
    try:
        print("render figure home")    
        Program = pagehome("bk",params)
        Program.set_path("./")
        print("render figure home finish")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 1",e)
def refreshmyorders(query_components):
    Program=refreshmyorderspage("commencez une nouvelle commande")

    return Program

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
def savemyinfo(query_components):
    try:
        Program=savemyinfopage("sauvegarde des infos",query_components)
        return Program
    except Exception as e:
        print("erreur save data",e)
def render_figure(pathname,Program):
    try:
        global path1
        s1=Program
        path1=os.getcwd()
        print(pathname,Program,"<== pathname, pgrm")
        Program.set_filename(pathname)
        print("render figure")
        print('ok')
        p1=Program.get_path
        p2=Program.get_filename
        print("okdac")
        #print(p1())
        print("okokdac")
        #print(p2())
        #print(p1()+p2())
        #print('dac')
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
        print(Program.__class__.__name__, "my html page action name")
        print((Program.__class__.__name__ in myredirect), "my redirect is like codepage")
        print(Program.get_redirect(), "my html redirect url link")
        print(Program.get_redirect() != "", "my redirect is not ''")

        if isinstance(Program,jsoncontent):
            html=Program
        elif Program.__class__.__name__ in myredirect and Program.get_redirect() != "":
            html=redirectaction(Program.get_redirect())
        elif isinstance(Program,redirectaction):
            html=Program
        elif layout == False:
            print("content")
            try:
                html=decode_any_string(content())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=content().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=content()
        else:
            title=title()
            css=Program.get_css()
            body=""
            js=""
            header1=""
            main1=""
            footer1=""
            print("header render_figure")
            try:
                header1+=decode_any_string(header().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e)[0:50])
                print('header gerer cette erreur')
                header1=header().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e)[0:50])
                print('gerer cette erreur')
                header1=header()
            print("content rnder figure")
            try:
                main1=decode_any_string(content().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e),"render figure")
                print('gerer cette erreur')
                main1=content().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e),"render figure")
                print('gerer cette erreur')
                main1=content()
            print("footer render figure")
            print("type footer")

            print(type(force_to_unicode(footer())))

            try:
                footer1=decode_any_string(footer().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                footer1=footer().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                footer1=footer()
            print("footer ajouté")
            print("type menu")
            try:
                body+=force_to_unicode(Program.get_menu())
            except UnicodeEncodeError as e:
                print(type(e) )
                print('gerer cette erreur')
                body+=Program.get_menu().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                body+=Program.get_menu()
            print("meu ajouté")
            j=open(path1+"/mespages/jstag.html").read()    
            js+=j % ("/js/jquery.js",)
            #print(js)
            js+=j % ("/js/js.js",)
            #print(js)
            print(Program.get_js(),"=js")
            js+=Program.get_js().decode('utf-8')

            j=open(path1+"/myapppage.html","r").read().decode('utf-8')
            #print(j)
            #print(title.decode('utf-8'),"=title")
            #print(css.decode('utf-8'),"=css")
            #print(js.decode('utf-8'),"=js")
            #print(header1.decode('utf-8'),"header1")
            #print(main1,"=main1")
            print("erreur")
            print(footer1[0:30],"=footer")
            print(js.decode('utf-8')[0:30],"==js")
            print(js.decode('utf-8')[-30:-1],"==fin js")
            print(main1.decode('utf-8')[0:30],"==main1")
            print(header1[0:30],"==js")
            print("erreur")
            html=j % (title.decode('utf-8'),css.decode('utf-8'),header1,main1.decode('utf-8'),footer1,js)
            #print(html)
            print("fin balise")
        #mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        #print(mychemin)
        #print(type(html))
        if isinstance(html,str):
            s1=html
        elif isinstance(html,directory):
            s1=html
        else:
            s1=html.encode('utf-8')
        #Program.sethtml(s1)    
        return s1
    except Exception as e:
        print(e,'erreru')
        print(traceback.format_exc())
        ##s1.set_erreur(str(traceback.format_exc()))


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
f=open(path1+"/mespages/dump.sql",'rb')
sql_command = f.read().decode('utf-8')
global myroutes
kk=0
mysqlcom= sql_command.split(";")
for sql in mysqlcom:
    if kk==0:
      print("Chargement du sql,patientez. ")
    elif kk == (len(mysqlcom) - 1): 
      print(" sql chargé.")
    #print(sql)
    kk+=1
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



def bootstrapjs(params = None):
    h="""  """
    return h

def bootstrapcss(params = None):
    h="""  """
    return h

def reloadmymodules(params = None):
    reload(searchrestaurant)
    reload(findaddress)
    reload(home)
    reload(address)
def copy(params = None):
    #restart_program()
    #os.execv(sys.argv[0], sys.argv)
    #os.execv(sys.executable, ['python'] + sys.argv)
    os.system("cp "+path1+"/mespages/js.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/css/css.css "+path1+"/css/css.css")
    os.system("cp "+path1+"/mespages/css/signin.css "+path1+"/css/signin.css")
    os.system("cp "+path1+"/mespages/css/*.css "+path1+"/css")
    os.system("cp "+path1+"/mespages/*.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/userconnecte.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/signin.js "+path1+"/js")

#Program.path("./")


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
    j=open(Program.get_filename_path("addgiftcard.html"),'rb')
    Program.add_css("signin.css")
    Program.add_js("addcard.js")
    Program.add_css("addgiftcard.css")
    text=j.read().decode('utf-8')
    Program.set_content(force_to_unicode(text))
    Program.set_path("./mespages")
    k=open(Program.get_filename_path("headeroverlay.html"),'rb')
    headertext=k.read().decode('utf-8')
    Program.set_header(headertext)

    return render_figure("ma page.html")







def signmein(query_components):
    try:
        Program=signmeinpage("bk")

        return Program
    except Exception as e:
        print("erreur sign me in",e)

def showmenu(query_components):
    Program=showmenupage("menu de burger king",query_components)
    

    return render_figure("index.html",Program)  

def signup_user(query_components):
    try:
        Program=signup_user_page("inscription",query_components)

        return Program
    except Exception as e:
        print("erreur sign up",e)
global splitparams
def splitparams(x):
    return x.split("=")
global accountinfo
def accountinfo(query_components):
    try:

        Program=myaccountinfo(query_components)
        return render_figure("index.html",Program)  
    except Exception as e:
        print("erreur account info",e)

def displaythisburger(burger,catname,catid):
    try:
        Program=pagedisplaythisburger('burger king',burger,catname,catid) 
        Program.set_path("./burgers")
        code=render_figure(str(burger[0])+".html")
        Program.file("html","/burger/"+str(burger[0]),code)
        return Program
    except Exception as e:
        print('erreur display burger',e)
def savepayment(query_components):
    try:
        Program=savepaymentpage("save payment",query_components)
        return Program
    except Exception as e:
        print("erreur save payment method",e)
global setcookie
def setcookie(query_components):
    try:
        print("set cookie",query_components["user"])
        if query_components.get("user"):
            token=query_components.get("user")[0]

            crsr.execute("select * from users where user_number = '" + str(token) + "'")
            connection.commit()
            user=crsr.fetchall()[0]

            return ""

    except:
        print("erreur set cookie")
def confirmotp(params=None):
    try:
        Program=confirmotppage("bk")
        return Program
    except Exception as e:
        print("erreur confirm otp",e)
def code(params = None):
    try:
        Program=codepage("code du coupon",params)
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur 3",e)
def signup(params = None):
    try:
        Program=signuppage("inscription")
        return render_figure("index.html",Program)
    except Exception as e:
        print("erreur sign in",e)
def accountpayment(params = None):
    try:
        Program=pageaccountpayment("account payment")
        print("account payment: current user")
        print(session.current_user)
        Program.set_path("./mespages")

        return render_figure("my page.html")
    except Exception as e:
        print("account payment erreur",e)
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


def validatecode(query_components):
    try:
        Program=validatecodepage("valider le code",query_components)
        return Program
    except Exception as e:
        print("erreur validate code",e)
def servicemode(query_components):
    Program=servicemodepage('entrer votre adresse',query_components) 
    try:
        return render_figure("servicemode.html",Program)
    except Exception as e:
        print("my errooor (=) service mode",e)
def addressfunc(query_components):
    Program=addresspage('choisir un restaurant',query_components) 
    try:
        return render_figure("address.html",Program)
    except Exception as e:
        print("my errooor (=) adress page",e)
def customizemymenu(query_components):
    Program=customizemymenupage('personnaliser mon menu',query_components) 
    try:


        return render_figure("custo.html",Program)
    except Exception as e:
        print("my errooor (=)",e)
def checkuser(query_components):
    try:
        Program=checkuserpage("vérifier l'utilisateur",query_components)
        return render_figure("check.html",Program)
    except Exception as e:
        print("erreur validate code",e)
def checkemail(query_components):
    try:
        Program=checkemailpage("vérification de l'email") 
        return Program
    except Exception as e:
        print("erreur validate code",e)


def insertburger(query_components):
    Program=insertburgerpage("ajouter des burgers",query_components)

    return render_figure("index.html")
def menu(params = None):
    try:
        Program=menupage("menu",params)
        return render_figure(page+".html")
    except Exception as e:
        print("erreur menu",e)
def accountpayment(params = None):
    try:
        try:
            userid=params["userid"]
        except:
            userid=None
        Program=pageaccountpayment("account payment", userid)
        print("account payment: current user")
        #print(session.current_user)
        Program.set_path("./mespages")

        return render_figure("my page.html")
    except Exception as e:
        print("account payment erreur",e)






global listburger
def listburger(burger):
    try:
        print(" list brger")
        print(type(burger[0]))
        print(type(burger[1]))
        print(type(burger[1].encode("utf-8")))
        j=open(path1+"/listburger/_modelburger.html")
        s= j % (str(burger[0]),(burger[1].encode('utf-8')))
        print(type(s))
        return s
    except Exception as e:
        print("erreur list brger",e)

def ingredients(burger):
    try:
        Program=ingredientpage("./showburger","customize your item",burger)
        return render_figure("ingredients.html",Program)
    except Exception as e:
        print("erreur ajout burger",e)
def changeitem(burger):
    try:
        Program=changeitempage("./showburger","customize your item",burger)
        return render_figure("changeitem.html",Program)
    except Exception as e:
        print("erreur ajout burger",e)
def ajoutlistburger(burger):
    try:
        print("ajout list brger")
        print(type(burger[1]))
        return "<li>"+burger[1]+"</li>"
    except Exception as e:
        print("erreur ajout burger",e)

# execute the statement


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
def myaccountinfo(params = None):
    try:
        Program=myaccountinfopage("infos de mon compte",params)

        return render_figure("index.html",Program)

    except Exception as e:
        print("erreur my account info page",e)

def signin(params = None):
    try:
        Program=signinpage("connexion")

        return render_figure("index.html",Program)

    except Exception as e:
        print("erreur sign in",e)
global signinuser
def signinuser(params):
    try:
        Program=pagesigninuser('burger king',params) 
        return Program
    except Exception as e:
        print("erreur: sign in user ",e)

def confirmjwt(query_components):
    try:
        Program=confirmjwtpage("bk",query_components)
        return Program


    except Exception as e:
        print("erreur confirm jwt",e)

def findaddressfunc(params):
  Program=findaddresspage("./myfindaddressdirectory","super website",params)
  return render_figure("myhtml.html",Program)


def searchrestaurantfunc(params):
  Program=searchrestaurantpage("./mysearchrestaurantdirectory","super website",params)
  return render_figure("mysearchrestauranthtml.html",Program)

class S(BaseHTTPRequestHandler):
    def _mon_erreur(self,e):
        print("erreur get",e)
        file="404.html"
        dir="./erreur"
        Program.set_path(dir)
        k= open(Program.get_path()+"/"+file,'rb').read()
        print(k)
        self._set_headers(switcher.get("html"))
        self.wfile.write(force_to_unicode(k.decode('utf-8')))
    def _mon_erreur_text(self,e):
        print("erreur get",e)
        file="404.html"
        dir="./erreur"
        Program.set_path(dir)
        k= "mon erreur"
        print(k)
        self._set_headers(switcher.get("html"))
        self.wfile.write(force_to_unicode(k.decode('utf-8')))
    def _set_headers(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()
    def set_header(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()
    def do_GET(self):
        print("=========new route GET=========["+self.path+"]===========")
        try:
            copy()
            reloadmymodules()
            urlpath=self.path
            myurlpath=urlpath.split("?")[0]
            routetrouve=None
            #f = open("index.html", "r")
            query_components = parse_qs(urlparse(urlpath).query)
            try:
                query_components["userid"]=[session.current_user[0]]
                print("-- user connecté --")
            except:
                print("aucun user connecté")
            print('path',myurlpath , query_components,"what params")
            #x=searchmyparams(query_components,myurlpath)
            for path in myroutes:
                #simple=path.split("?")[0]
                #print("le chemin est %s et la route %s" % (myurlpath,path))
                #print("la route a été trouvée ?%r" % (re.match(path, myurlpath) != None))
                mysimplefunc=myroutes[path]
                kk=re.match(path, myurlpath)
                if kk:
                    for x in range(len(kk.groups())):
                        print(kk.group(0),x,kk.group(x))
                        query_components["param"+str(x)] = kk.group(x)
                    routetrouve=path
                    code=mysimplefunc(query_components)
                    #code=Program.gethtml()
                    print("le code récupéré")    
                    break

            if routetrouve:
                print("La route a été trouvée ? %r, c'est %s" % (routetrouve is not None, routetrouve))
            else:
                print("La route n'a pas été trouvée ?  %r" % (routetrouve is None,))
            try:
              if code is None:
                print("code in none")
                code=""
            except:
                code=""
            
            if isinstance(code,redirectaction):
                self.send_response(301)
                myred=code.get_redirect()
                print("vous serez redirigée à %s " % myred)
                self.send_header('Location',myred)
            elif isinstance(code,jsoncontent):
                print("return json")
                data=code.get_json()
                code.set_json(None)

                self._set_headers(switcher.get("json"))
                self.wfile.write(str(data).replace("'",'"'))
            elif myurlpath.split(".")[-1] in ["css","scss"]:
                print("le mimetype est %s et la réponse est %s" % ("css",200))
                self._set_headers(switcher["css"])

                code=open(os.getcwd()+myurlpath, "rb").read().decode('utf-8')
                self.wfile.write(code)
            elif myurlpath.split(".")[-1] in ["png","gif"]:
                print("le mimetype est %s et la réponse est %s" % ("png",200))
                self._set_headers(switcher[myurlpath.split(".")[-1]])

                code=open(os.getcwd()+myurlpath, "rb").read()
                self.wfile.write(code)
            elif myurlpath.split(".")[-1] in ["js"]:
                print("le mimetype est %s et la réponse est %s" % ("js",200))
                self._set_headers(switcher["js"])

                code=open(os.getcwd()+myurlpath, "rb").read()
                self.wfile.write(code)
            elif routetrouve:
                
                try:
                    dic=__mots__[routetrouve]
                    if dic["partiedemesmots"]:
                        print("partie de mes mots cherches : "+dic["partiedemesmots"])
                        print("une partie de mes mots a été cherchée?vrai")
                        try:
                            if code.index(dic["partiedemesmots"]):
                                print("la route est html")

                                print("le mimetype est %s et la réponse est %s" % ("html",200))
                                self._set_headers(switcher["html"])


                                self.wfile.write(code)
                                print("les mots ed la page ont été reconnus?vrai")
                        except Exception as e:
                            print("retrouver l'output dans myoutput.html ")
                            k=open("myoutput.html","w")
                            k.write(code)
                            k.close()
                            print("une partie de mes mots n'a ps été trouvee")
                            print("la route nest pas html")
                            print(str(e)+str(traceback.format_exc()))
                            mycode=erreur("erreur:: ")


                            mycode.set_erreur(str(traceback.format_exc()))
                            mycode.set_title("Erreur "+dic["partiedemesmots"]+": mot non trouves")
                            self._set_headers(switcher["html"])

                            self.wfile.write(render_figure("hhh.html",mycode))



                        #try:
                        #    if code.index("Traceback"):
                        #        print("une erreur a été trouvée dans le code html")

                        #        self._set_headers(switcher["html"])


                        #        self.wfile.write(code)
                        #except Exception as e:
                        #    print("aucune erreur n'a été trouvée dans le code html")
                        #    print(str(e)+str(traceback.format_exc()))
                        #    print("retrouver l'output dans myoutput.html ")
                        #    k=open("myoutput.html","w")
                        #    k.write(code)
                        #    k.close()
                except Exception as e:
                        print("les mots ed la page ont été reconnu?faux",code)
                        self._mon_erreur_text(e)
                        print(str(e)+str(traceback.format_exc()))
            else:
                self._mon_erreur("ni une erreur ni css js ou image")
        except UnboundLocalError as e:


          self._set_headers(switcher["html"])
          self.wfile.write(str(e)+str(traceback.format_exc()))

        return

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
                print("-- user connecté --")
            except:
                print("aucun user connecté")
            try:
                query_components["neworder"]=[session.neworder]
            except:
                print("aucune nouvelle commande")
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
                    elif isinstance(res,erreur):
                        Program=res
                    elif isinstance(res,jsoncontent):
                        Program=res
                    elif isinstance(res,directory):
                        print("is object")
                        print(res)
                        Program=res
                        try:
                            if isinstance(Program,setuserpage):
                                session.current_user=Program.get_session()
                        except:
                            print("pas de session")
                        if Program.get_current_user() is not None and Program.get_current_user() != ():
                            print("current_user")
                            print(Program.get_current_user())
                            session.current_user=Program.get_current_user()
            except KeyError:
                print("erreur 6")


        #self.data_string = params
            urlpath=self.path
            print("redirect post:")
            print(Program.get_redirect())
            copy()
            reloadmymodules()
            #myaccountinfo()
            #home()
            try:
                mytype=Program.get_mimetype() or self.path.split(".")[-1]
                print(urlpath)
                print("my type")
                print(mytype)
                print("Program.get json")
                print(Program.get_json() is not None)
                print(Program.get_json())
                print(route_post.get(myurlpath))
            except:
                print("no mimetype(redirect)")
            print("redirect")
            print(Program.get_redirect())
            print(str(Program.get_redirect()) != 'None')
            if Program and isinstance(Program,redirectaction):
                myred=Program.get_redirect()
                print("vous serez redirigée à %s " % myred)

                self.send_response(301)
                self.send_header('Location',myred)
            elif isinstance(Program,jsoncontent):
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
            session.neworder=None
            self.end_headers()
        except UnboundLocalError:
            print("erreur post")
            file="404.html"
            dir="./erreur"
            Program.set_path(dir)
            k= open(Program.get_path()+"/"+file,'r')

            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read().decode('utf-8'))

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
#rewards()
#offers()


global route_post
myroutes = {"/customizemenu":customizemymenu,
"/searchrestaurant":searchrestaurantfunc,
"/findaddress":findaddressfunc,
    "/infolocation":infolocation,

r"^/store-locator/address$":addressfunc,
r"^/store-locator/service-mode$":servicemode,
r"^/store-locator$":servicemode,

"/listlocation":listlocation,
"/updateitem/customize":ingredients,
"/updateitem/changeitem":changeitem,

r"\/menu\/[0-9]*$(\/)?": showburger,
r"/menu(/)([a-z]+)(/)?": showmenu,
r"/menu(/)?([a-z]+)?(/)?": showmenu,
"/orders/refresh":refreshmyorders,
"/account/orders":myorders,
"/redeem":code,
"/account/payment":accountpayment,
"/account/payment/add-card":addcard,
"/account/payment/add-gift-card":addgiftcard,
"/signinuser": signinuser,
r"^\/$":homefunc,
"/signin":signin,
            "/signup": signup,
            "/rewards": rewards,
'/account/info': myaccountinfo,
'/confirm-otp': confirmotp,
"/confirm-jwt": confirmjwt,
"/setcookie": setcookie,

'/confirm-jwt': confirmjwt
}
global menu
# POST routes
route_post={

    "/orderlocation":orderlocation,
    "/offerslocation":offerslocation,
    "/favlocation":favlocation,
    "/bkaction":bkaction,
    "/addburger":addburger,
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

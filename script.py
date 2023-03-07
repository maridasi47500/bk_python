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
import customizemymenu
import showburger
from accountpayment import pageaccountpayment
import directory
from signup_user import signup_user_page
import afficher_modepaiement
import check_email
import code
from signin import signinpage
import addcard
from signup import signuppage
import signup_user
import refreshmyorders
import myaccountinfo
import home
import confirmotp
import menu
import signup
from showmenu import showmenupage
import insertburger
import checkuser
import myorders
from displaythisburger import pagedisplaythisburger
from showburger import showburger
from signmein import signmeinpage
from signinuser import pagesigninuser
import accountpayment
import savemyinfo
import savegiftcard
import savepayment
switcher={
'html':'text/html',
'css':'text/css',
'json':'application/json',
'js':'text/javascript',
'png':"image/png",
'ico':'image/vnd.microsoft.icon'
}


connection = sqlite3.connect("desburgers.db")

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
def showburger(query_components):
    Program=showburger("burger",query_components)
    Program.set_path(".\showburger")
    #=======
    return Program
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
global home
def home(params = None):
    try:
            
        Program = pagehome("bk")
        Program.set_path("./")
        
        code=render_figure("index.html")
        Program.run("html","/",code)
        print("render figure home")
        return Program
    except Exception as e:
        print("erreur 1",e)
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
            title=title()
            css=Program.get_css()
            body=""
            js=""
            header1=""
            main1=""
            footer1=""
            print("header")
            try:
                body+=decode_any_string(header1())
            except UnicodeEncodeError as e:
                print(type(e))
                print('header gerer cette erreur')
                header1=header().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                header1=header()
            print("content")
            try:
                main1=decode_any_string(myparams(content()))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                main1=myparams(content()).encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                main1=myparams(content())
            print("footer")
            print("type footer")

            print(type(force_to_unicode(footer())))

            try:
                footer1=decode_any_string(footer())
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
            print(type(Program.get_menu()))
            try:
                body+=force_to_unicode(Program.get_menu())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                body+=Program.get_menu().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                body+=Program.get_menu()
            print("meu ajouté")
            j=open(path1+"/mespages/jstag.html").read()    
            js+=j % ("/js/jquery.js",)
            js+=j % ("/js/js.js",)
            js+=Program.get_js()

            j=open(path1+"/myapppage.html","r").read()
            html=j % (title,css,header,main,footer,js)
            #print(html)
            print("fin balise")
        mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        print(mychemin)
        print(type(html))
        if isinstance(html,str):
            s1=html
        else:
            s1=html.encode('utf-8')
        return s1
    except Exception as e:
        print(e,'erreru')
def accountpayment(params = None):
    try:
        Program=pageaccountpayment("account payment")
        print("account payment: current user")
        print(session.current_user)
        Program.set_path("./mespages")

        return render_figure("my page.html")
    except Exception as e:
        print("account payment erreur",e)
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
def signmein(query_components):
    try:
        Program=signmeinpage("bk")

        return Program
    except Exception as e:
        print("erreur sign me in",e)
global myroutes
def showmenu(query_components):
    Program=showmenupage("menu de burger king",query_components)
    Program.set_path("./mespages")

    return Program  

def signup_user(query_components):
    try:
        Program=signup_user_page("inscription",query_components)

        return Program
    except Exception as e:
        print("erreur sign up",e)
global splitparams
def splitparams(x):
    return x.split("=")
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

def displaythisburger(burger,catname,catid):
    try:
        Program=pagedisplaythisburger('burger king',burger,catname,catid) 
        Program.set_path("./burgers")
        code=render_figure(str(burger[0])+".html")
        Program.file("html","/burger/"+str(burger[0]),code)
        return Program
    except Exception as e:
        print('erreur display burger',e)

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

def signup(params = None):
    try:
        Program=signuppage("inscription")
        return render_figure("index.html")
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

def card(title,description,button):
    try:
        f=codecs.open(path1+"/mespages/card.html")
        s=f.read()

        html=s % (title,description,button)
        return html
    except Exception as e:
        print("erreur card",e)
        return ""
def mycard(title,description,content):
    try:
        f=codecs.open(path1+"/mespages/card.html")
        s=f.read()
        html = s % (title,description,content)
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
def signin(params = None):
    try:
        Program=signinpage("connexion")

        return render_figure("index.html")

    except Exception as e:
        print("erreur sign in",e)
global signinuser
def signinuser(params):
    try:
        Program=pagesigninuser('burger king',params) 
        return Program
    except Exception as e:
        print("erreur: sign in user ",e)
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
                    if Program is not None and Program.get_current_user() is not None:
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

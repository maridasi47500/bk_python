# -*- coding: utf-8 -*-
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from os.path import exists
from urlparse import urlparse, parse_qs
import os
import codecs
import re
import sqlite3
global path1
global Program
global mycard
global myparams
path1 = "/home/mary/ionicsite"

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import random
global copy

global connection
# connecting to the database
connection = sqlite3.connect("data_base_1burker.db")
 
# cursor
global crsr
crsr = connection.cursor()
global __words__
__words__ = ""
 
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
myroutes = {
'/confirm-otp': '/signup/confirm-otp'
}
global signmein
def myparams(x):
    myvar={
    'monemailici': Program.get_email()
    }
    for y in myvar:
        x=x.replace(y,myvar[y])
    return x

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

                import random as rand
                bkcode=rand.randint(1,999999)
                crsr.execute("UPDATE users SET code = '" + str(bkcode) + "' WHERE email = '"+data_string+"'")
                connection.commit()
                import smtplib

                # Configuration SMTP | Ici ajusté pour fonctionné avec Gmail
                host_smtp = "smtp.gmail.com"
                port_smtp = 587
                email_smtp = "mary.goudon@gmail.com" # Mon email Gmail
                mdp_smtp = "eljlkuznppklsquw"  # Mon mot de passe

                # Configuration du mail
                prenom = "cleo jeanne"
                formule_p = "code de burger king"
                email_destinataire = "cleo.ordioni@gmail.com"
                mail_content = str(bkcode)+" est votre code de connexion de burger king"
                msg = MIMEMultipart()
                msg['From'] = email_smtp
                msg['To'] = email_destinataire
                msg['Subject'] = formule_p
                msg.attach(MIMEText(mail_content))
                # Création de l'objet mail
                mail = smtplib.SMTP(host_smtp, port_smtp) # cette configuration fonctionne pour gmail
                mail.ehlo() # protocole pour SMTP étendu
                mail.starttls() # email crypté
                mail.login(email_smtp, mdp_smtp)
                mail.sendmail(email_smtp, email_destinataire, msg.as_string())
                mail.close()
                Program.set_url("/confirm-otp")
                confirmotp(data_string)
                Program.set_redirect("/confirm-otp")
    except Exception as e:
        print("erreur sign me in",e)
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
            render_figure("index.html")
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
    crsr.execute(sql)
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
        render_figure(str(burger[0])+".html")
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

def bootstrapjs():
    h="""  """
    return h

def bootstrapcss():
    h="""  """
    return h
def header():
    h=open(path1+"/mespages/header.html","r")
    return h.read()
def footer():
    h=open(path1+"/mespages/footer.html","r")
    return h.read()    
def copy():
    os.system("cp "+path1+"/mespages/css/css.css "+path1+"/css/css.css")
    os.system("cp "+path1+"/mespages/css/signin.css "+path1+"/css/signin.css")
    os.system("cp "+path1+"/mespages/userconnecte.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/signin.js "+path1+"/js")
class directory(object):
    def __init__(self,title):
        self.title = title
        self.js=""
        self.url=""
        self.redirect=False
        self.email=""
        self.css=""
        h=header
        i=footer
        self.header=h()
        self.path=""
        self.footer=i()
    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email=email
    def get_redirect(self):
        return self.redirect
    def set_redirect(self,redirect):
        self.redirect=redirect
    def get_url(self):
        return self.url
    def set_url(self,url):
        self.url=url
    def get_content(self):
        return self.content
    def set_content(self,content):
        self.content=content
    def get_header(self):
        return self.header
    def set_header(self,myheader):
        self.header=myheader
    def get_footer(self):
        return self.footer
    def set_footer(self,myfooter):
        self.footer=myfooter
    def set_filename(self,name):  
        self.filename=name
    def title(self,title):
        self.title = title
    def get_title(self):
        return self.title
    def get_js(self):
        return self.js
    def set_js(self,js):
        self.js=js
    def add_js(self,js):
        self.js+="<script type=\"text/javascript\" src=\""+js+"\"></script>"
    def add_css(self,css):
        self.css+="<link rel=\"stylesheet\" href=\""+css+"\"/>"
    def get_css(self):
        return self.css
    def set_css(self,css):
        self.css=css
    def get_path(self):
        return self.path
    def get_filename(self):
        return self.filename
    def set_path(self,mypath):
        self.path=path1+mypath.replace("./","/")
    def path(self,path):
        self.path = path1+path.replace("./","/")

def render_figure(pathname):
    try:
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
        header=Program.get_header
        content=Program.get_content
        footer=Program.get_footer
        html="<!doctype html>"
        html+="<html>"
        html+="<head>"
        html+="<meta charset=\"UTF-8\">"
        html+="<title>"
        print("title")
        html+=title()
        html+="</title>"
        html+="<link rel=\"stylesheet\" href=\"/css/css.css\"/>"
        html+=Program.get_css()
        html+="</head>"
        html+="<body>"
        print("header")
        html+=header()
        print("content")
        html+=myparams(content())
        print("footer")
        print("type footer")
        print(type(footer()))
        html+=unicode(footer(),'utf-8')
        html+=Program.get_js()
        html+="</body>"
        html+="</html>"
        #print(html)

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
        
        f=codecs.open(mychemin,'w')
        print(type(s1))
        f.write(s1)
        f.close()
        #if (__words__).rstrip() == "Full Menu":
        print(Program.get_path())
        if Program.get_path()+"/"+Program.get_filename() == path1+"/code/index.html":
            if len(argv) == 2:
                run(port=int(argv[1]))
            else:
                run()    
    except Exception as e:
        print(e,'erreru')
Program=directory("Burger King")
#Program.path("./")
class Page:
    global home
    def home():
        try:
            print("home")
            j=codecs.open(path1+"/mespages/index.html")
            text=j.read()
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
                if result.group(1):
                    print(result.group(1))
                    if len(result.group(1)) > 0:
                        text=text.replace(result.group(1),mycontent)
            Program.set_path("./")
            Program.set_content(text)
            
            text=(text)
            render_figure("index.html")
        except Exception as e:
            print("erreur 1",e)
    global menu        
    def menu():
        try:
            j=codecs.open(path1+"/mespages/menu.html")
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
                render_figure(page+".html")
        except Exception as e:
            print("erreur menu",e)
    global confirmotp        
    def confirmotp(email):
        try:
            print("confirm otp")
            f=open(path1+"/mespages/userconnecte.js")
            js=f.read()
            fff=open(path1+"/mespages/headersignin.html")
            myheader=fff.read()
            Program.set_email(email)
            ff=open(path1+"/mespages/confirmotp.html")
            text=ff.read()
            Program.set_js("")
            Program.set_header(myheader)
            Program.add_css("/css/signin.css")
            Program.add_js("/js/signin.js")
            Program.set_footer("")
            Program.set_path("./signup")
            Program.set_content(unicode(text,'utf-8'))
            render_figure("confirm-otp.html")
        except Exception as e:
            print("erreur confirm otp",e)
    global signup        
    def signup():
        try:
            print("sign up")
            f=open(path1+"/mespages/userconnecte.js")
            js=f.read()
            fff=open(path1+"/mespages/headersignin.html")
            myheader=fff.read()

            ff=open(path1+"/mespages/signup.html")
            text=ff.read()
            Program.set_js("")
            Program.set_header(myheader)
            Program.add_css("/css/signin.css")
            Program.add_js("/js/signin.js")
            Program.set_footer("")
            Program.set_path("./signup")
            Program.set_content(unicode(text,'utf-8'))
            render_figure("index.html")
        except Exception as e:
            print("erreur sign in",e)
    global signin        
    def signin():
        try:
            print("sign in")
            f=open(path1+"/mespages/userconnecte.js")
            js=f.read()
            fff=open(path1+"/mespages/headersignin.html")
            myheader=fff.read()

            ff=open(path1+"/mespages/signin.html")
            text=ff.read()
            Program.set_js("")
            Program.set_header(myheader)
            Program.add_css("/css/signin.css")
            Program.add_js("/js/signin.js")
            Program.set_footer("")
            Program.set_path("./signin")
            Program.set_content(text)
            render_figure("index.html")
            Program.set_css("")
            Program.set_js("")
        except Exception as e:
            print("erreur sign in",e)
    global code        
    def code():
        try:
            print("code")
            f=open(path1+"/mespages/userconnecte.js",'r')
            js=f.read()

            ff=open(path1+"/mespages/code.html",'r')
            text=ff.read()
            Program.add_js("/js/userconnecte.js")
            Program.set_header(header())
            Program.set_footer(footer())
            Program.set_path("./code")
            Program.set_content(text)
            render_figure("index.html")
        except Exception as e:
            print("erreur 3",e)
    global offers        
    def offers():
        try:
            print("offers")
            Program.set_header(header())
            Program.set_footer(footer())
            Program.set_path("./offers")
            Program.set_content("")
            render_figure("index.html")
        except:
            print("erreur 4")
    global rewards        
    def rewards():
        try:
            print("rewards")
            Program.set_path("./rewards")
            Program.set_content("")
            render_figure("index.html")
        except:
            print("erreur 5")
class S(BaseHTTPRequestHandler):
    def _set_headers(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()

    def do_GET(self):
        
        #Program.path("./")
        Program.set_url(self.path)
        urlpath=Program.get_url()

        #f = open("index.html", "r")
        query_components = parse_qs(urlparse(urlpath).query)
        #print(query_components)
        try:
            insertburger(query_components)
        except KeyError:
            print("erreur 6")
        urlpath=Program.get_url()
        #self.data_string = params
        #os.system("echo \""+urlpath+"\"")
        patha=path1+urlpath.split("?")[0].replace(".html","")+".html"
        pathd=path1+urlpath.split("?")[0].replace(".html","")
        pathb=path1+urlpath.split("?")[0]+"index.html"
        pathc=path1+urlpath.split("?")[0]+"/index.html"
        pathe=path1+str(myroutes.get(urlpath.split("?")[0]))+".html"
        copy()
        if exists(patha):
            f=codecs.open(patha,'r')
            mytype=patha.split(".")[-1]
        elif exists(pathb):
            f=codecs.open(pathb,'r')
            mytype=pathb.split(".")[-1]
        elif exists(pathc):
            f=codecs.open(pathc,'r')
            mytype=pathc.split(".")[-1]
        elif exists(pathd):
            f=codecs.open(pathd,'r')
            mytype=pathd.split(".")[-1]
        elif exists(pathe):
            f=codecs.open(pathe,'r')
            mytype=pathe.split(".")[-1]
        switcher={
        'html':'text/html',
        'css':'text/css',
        'js':'text/javascript'
        }
        print(mytype)
        self._set_headers(switcher.get(mytype))    
        self.wfile.write(f.read())
            
    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        Program.set_url(self.path)
        urlpath=Program.get_url()

        query_components = parse_qs(urlparse(urlpath).query)

        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        fields = parse_qs(self.data_string)
        try:
            signmein(fields)
        except KeyError:
            print("erreur 6")


        query_components = parse_qs(urlparse(urlpath).query)
        #self.data_string = params
        urlpath=Program.get_url()
        patha=path1+urlpath.split("?")[0].replace(".html","")+".html"
        pathb=path1+urlpath.split("?")[0]+"index.html"
        pathc=path1+urlpath.split("?")[0]+"/index.html"
        pathd=path1+urlpath.split("?")[0].replace(".html","")
        pathe=path1+str(myroutes.get(urlpath.split("?")[0]))+".html"

        copy()
        if exists(patha):
            f=codecs.open(patha,'r')
            mytype=patha.split(".")[-1]
        elif exists(pathb):
            f=codecs.open(pathb,'r')
            mytype=pathb.split(".")[-1]
        elif exists(pathc):
            f=codecs.open(pathc,'r')
            mytype=pathc.split(".")[-1]
        elif exists(pathd):
            f=codecs.open(pathd,'r')
            mytype=pathd.split(".")[-1]
        elif exists(pathe):
            f=codecs.open(pathe,'r')
            mytype=pathe.split(".")[-1]
        switcher={
        'html':'text/html',
        'css':'text/css',
        'js':'text/javascript'
        }
        
        if Program.get_redirect():
            Program.set_redirect(False)
            self.send_response(301)
            self.send_header('Location',Program.get_url())
            self.end_headers()
        else:
            print(mytype)
            self._set_headers(switcher.get(mytype))    
            self.send_response(200)
            self.end_headers()
        
            self.wfile.write(f.read())

        return


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    print("run erver")
    httpd = server_class(server_address, handler_class)
    #print 'http://localhost:8000'
    if len(argv) == 2:
        print 'http://localhost:'+argv[1]
    else:
        print 'http://localhost:8000'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
home()
menu()
signup()
signin()

code()
#rewards()
#offers()
print((__words__).rstrip())



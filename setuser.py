import os
import json
global path1
import sqlite3  
global codecs
import codecs
from multipledispatch import dispatch
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
import requests
from directory import directory
class setuserpage(directory):
    redirect=""
    current_user=()
    session=None
    path1=os.getcwd()
    def __init__(self,title):
        global path1
        self.session=None
        self.htmlpath="/"
        path1=os.getcwd()
        self.path1=os.getcwd()
        self.title = title
        self.layout = "ok"
        self.mytitle = title
        self.js=""
        self.url=""
        self.html=""
        self.current_user=()
        self.current_order=[]
        self.mime=None
        self.content=""
        self.response=200
        self.json=None
        self.userid=""
        self.redirect=None
        self.email=""
        self.css=""
        self.menu=""
        self.path=os.getcwd()+"/mespages"
        print(self.get_file_with_path("header.html"))
        header1=self.get_file_with_path("header.html")
        footer1=self.get_file_with_path("footer.html")
        self.header=header1.read()
        self.path=""
        self.footer=footer1.read()
        self.parameters={}
        self.current_user=None
    def switcher(self,extension):
        return {
        'html':'text/html',
        'css':'text/css',
        'json':'application/json',
        'js':'text/javascript',
        'png':"image/png",
        'ico':'image/vnd.microsoft.icon'
        }[extension]
    def infotable(self,tablename):
        crsr.execute("PRAGMA table_info(["+tablename+"])")
        connection.commit()
        matable=crsr.fetchall()
        return matable

    def parameters(self):
        return self.parameters
    def work(self,code):
        self.response=code 
    def pageok(self):
        self.response=200        
    def run(self,redirect):
        self.parameters={"codereponse":301,"location":redirect}
    def file(self,mime,location):
        self.parameters={"mime":self.switcher(mime),"codereponse":200,"location":location}
    def sethtml(self,html):
        self.html=html
    def gethtml(self):
        return self.html
    def dict2class(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
    def set_header_with_path(self,header):
        header1=self.get_file_with_path(header)
        self.header=header1.read()
    def set_current_user(self,user):
        self.current_user=user
    def get_current_order(self):
        return self.current_order
    def set_current_order(self,user):
        self.current_order.append(user)
    def append_current_order(self,user):
        self.current_order.append(user)
    def get_current_user(self):
        return self.current_user
    def set_footer_with_path(self,footer):
        footer1=self.get_file_with_path(footer)
        self.footer=footer1.read()
    def set_layout(self,type):
        self.layout=type
    def get_layout(self):
        return self.layout
    def set_response(self,type):
        self.response=type
    def get_response(self):
        return self.response
    def set_mimetype(self,type):
        self.mime=type
    def get_mimetype(self):
        return self.switcher(self.mime)
    def edit_title(self,str):
        self.title = str+ " - "+self.mytitle
    def set_title(self,str):
        self.title = str
    def get_title(self):
        return self.title
    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email=email
    def get_json(self):
        return json.dumps(self.json, ensure_ascii=False).replace("'",'"')

    def set_json(self,json):
        self.json=json
    def get_redirect(self):
        return self.redirect
    def set_redirect(self,redirect):
        self.redirect=redirect
    def get_userid(self):
        return str(self.userid)
    def set_userid(self,userid):
        self.userid=userid
    def get_menu(self):
        return self.menu
    def set_menu(self,menu):
        self.menu=menu
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
        self.set_path("./js")
        self.js+="<script type=\"text/javascript\" src=\""+self.get_htmlpath()+"/"+js+"\"></script>"
    def get_htmlpath(self):
        return self.htmlpath
    def trouver_fichier(self,urlpath,myroutes):
        file=None
        paths=[]
        paths.append(self.path1+urlpath.split("?")[0].replace(".html","")+".html")
        paths.append(self.path1+urlpath.split("?")[0]+"index.html")
        paths.append(path1+urlpath.split("?")[0]+"/index.html")
        paths.append(self.path1+urlpath.split("?")[0].replace(".html",""))
        paths.append(self.path1+str(myroutes.get(urlpath.split("?")[0]))+".html")
        for i in paths:
            try:
                print(i)
                if self.get_file(i) is not None:
                    file=self.get_file(i)
            except:
                print("erreur")
        return file
    def get_file(self,file):

        return open(file,'r')
    def get_file_with_path(self,file):

        return open(self.path+"/"+file,'r')
    def add_css(self,css):
        self.set_path("./css")
        self.css+="<link rel=\"stylesheet\" href=\""+self.get_htmlpath()+"/"+css+"\"/>"
    def get_css(self):
        return self.css
    def set_css(self,css):
        self.css=css
    def get_path(self):
        return self.path
    def get_filename(self):
        return self.filename
    def set_path(self,mypath):
        self.htmlpath=mypath.replace("./","/")
        self.path=self.path1+mypath.replace("./","/")
    def get_filename_path(self,file):
        return self.path+"/"+file
    def get_css_dir_path(self):
        return "./css/"
    def get_js_dir_path(self):
        return "./js/"
    def get_image_dir_path(self):
        return "./images/"
    def path(self,path):
        try:
            self.path = self.path1+path.replace("./","/")
        except Exception as e:
            print(e,"erreur  1111")
    def set_my_header(self,headername):
        try:
            #self.set_path("./mespages")
            fff=self.get_file(headername+".html")
            myheader=fff.read()
            self.set_header(myheader)
        except IOError:
            self.set_header("")
    def force_to_unicode(self,text):
        "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
        return text if isinstance(text, unicode) else text.decode('utf-8')
    def get_file(self,file):
        print("get file:")
        print(self.get_filename_path(file))
        return open(self.get_filename_path(file),'r')
    def get_file_dir(self,file,dir):
        print("get file:"+dir)
        self.set_path(dir)
        return open(self.get_path()+"/"+file,'r')

    def set_my_footer(self,headername):
        try:
            #self.set_path("./mespages")
            fff=self.get_file(headername+".html")
            myfooter=fff.read()
            self.set_footer(myfooter)
        except IOError:
            self.set_footer("")
    def display_collection(self,sql,sqlargs,templatename,errormessage,tablename,sortby = False,templatesortby = False):
        idprecedent=0
        print(sqlargs)
        print(len(sqlargs))
        print(sql,sqlargs,templatename,errormessage,tablename)
        crsr.execute("PRAGMA table_info(["+tablename+"])")
        connection.commit()
        matable=crsr.fetchall()
        #self.set_path("./mespages")
        h=self.get_file(templatename+".html")
        template=self.force_to_unicode(h.read())
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
                mytemplate=self.force_to_unicode(template)
                for x in range(len(re)):
                    print(x)
                    print(re[x])
                    z=re[x]
                    strrep=self.force_to_unicode("(%s)" % (matable[x][1]))
                    print(strrep)
                    if type(z) == int or type(z) == float:
                        z=str(z)
                    if z is not None:
                        mytemplate=mytemplate.replace(strrep, self.force_to_unicode(z))
                    if matable[x][1] == sortby:
                        if idprecedent != 0:
                            if re[x] != idprecedent:
                                if paspremier:
                                    myfigure+="</div>"
                                    paspremier = True
                                #self.set_path("./mespages")
                                kk=self.get_file(templatesortby)
                                kk=kk.read()
                                y=0
                                for y in range(len(re)):
                                    mystrrep="(%s)" % (matable[y][1])
                                    kk=kk.replace(mystrrep, self.force_to_unicode(str(re[y])))
                                myfigure += kk
                        idprecedent=re[x]

                myfigure+=mytemplate
                myfigure+="</div>"
            return myfigure
        else:
            return self.force_to_unicode("<p>"+errormessage+"</p>")
    def set_session(self,sess):
        self.session=sess
    def get_session(self):
        return self.session
    def display_collection_sql(self,sql,sqlargs,templatename,errormessage,tablename,sortby = False,templatesortby = False):
        idprecedent=0
        print(sqlargs)
        print(len(sqlargs))
        print(sql,sqlargs,templatename,errormessage,tablename)
        crsr.execute("PRAGMA table_info(["+tablename+"])")
        connection.commit()
        matable=crsr.fetchall()
        #self.set_path("./mespages")
        h=self.get_file(templatename+".html")
        template=self.force_to_unicode(h.read())
        print(sql,sqlargs)
        crsr.execute(sql,sqlargs)
        connection.commit()
        res=crsr.fetchall()
        myfigure=""
        x=0
        mytemplate=""
        if len(res) > 0:
            print("plusieurs ("+str(res)+") "+tablename)

            for re in res:
                paspremier = False
                mytemplate=self.force_to_unicode(template)
                for x in range(len(re)):
                    print(x)
                    print(re[x])
                    z=re[x]
                    strrep=self.force_to_unicode("(%s)" % (matable[x][1]))
                    print(strrep)
                    if type(z) == int or type(z) == float:
                        z=str(z)
                    if z is not None:
                        mytemplate=mytemplate.replace(strrep, self.force_to_unicode(z))
                    if matable[x][1] == sortby:
                        if idprecedent != 0:
                            if re[x] != idprecedent:
                                if paspremier:
                                    myfigure+="</div>"
                                    paspremier = True
                                #self.set_path("./mespages")
                                kk=self.get_file(templatesortby)
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
            return self.force_to_unicode("<p>"+errormessage+"</p>")

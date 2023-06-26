# -*- coding: utf-8 -*-

from erreur import erreur
import sys
import os
print(sys.argv[1])
if sys.argv[1] == "myclass":


  filename=sys.argv[2]
  marouteget="\"/%s\"" % filename
  myhtml="my"+filename+"html"
  myfavdirectory="my%sdirectory" % filename
  mystr="""# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur

class {myclass}page(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content_from_file("{myhtml}.html")
      self.title=title
      self.params=title
      try:
        userid=params["userid"][0]
      except:
        userid=None
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title({marouteget})

"""
  if not os.path.isfile(filename):
    f = open(filename+".py", "w") 
    f.write(mystr.format(myclass=filename,myhtml=myhtml,marouteget=marouteget))
    f.close()


  with open("./script.py", "r") as f:
    contents = f.readlines()


  scriptfunc="""
def {myclass}func(params):
  Program={myclass}page("./{myfavdirectory}","super website",params)
  return render_figure("{myhtml}.html",Program)

"""
  index=[i for i in range(len(contents)) if "class S(BaseHTTPRequestHandler):" in contents[i]][0]
  contents.insert(index, scriptfunc.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
  contents.insert(1, "global {myclass}\n".format(myclass=filename))
  contents.insert(1, "import {myclass}\n".format(myclass=filename))
  contents.insert(1, "from {myclass} import {myclass}page\n".format(myclass=filename))
  myrouteget="\"/{myclass}\":{myclass}func,\n"
  index=[i for i in range(len(contents)) if "myroutes = {" in contents[i]][0]
  contents.insert((index+1), myrouteget.format(myclass=filename))
  index=[i for i in range(len(contents)) if "def reloadmymodules" in contents[i]][0]
  contents.insert((index+1), "    reload({myclass})\n".format(myclass=filename))
  index=[i for i in range(len(contents)) if "__mots__={" in contents[i]][0]
  contents.insert((index+1), "    \"/{myclass}\":{\"partiedemesmots\":\"{myclass}\"},\n".replace("{myclass}",filename))

  with open("./script.py", "w") as f:
      contents = "".join(contents)
      f.write(contents)

  os.system("mkdir %s" % myfavdirectory)
  pathhtml="%s/%s.html" % (myfavdirectory, myhtml)
  os.system("touch %s" % pathhtml)

  if os.path.isfile(pathhtml):
      with open(pathhtml, "w") as f:
          urlayout="""<h1>Layout de la route {myclass}</h1>
<p><a href="{marouteget}">nous sommes ici (essayez ce lien)</a></p>
<p>Entrez du texte sur cette page</p>
"""
          f.write(urlayout.format(marouteget=marouteget,myclass=filename))

  print("ma route get %s a été ajoutée. Maintenant vous pouvez essayer d'y acceder" % marouteget)

# -*- coding: utf-8 -*-

import sys
import os
print(sys.argv[1])
if sys.argv[1] == "myclass":
  filename=sys.argv[2]
  mystr="""# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class {myclass}page(directory):
  def __init__(self,path,params):
    self.set_path(path)
    self.title=title
    self.params=title
    try:
      userid=params["userid"][0]
    else:
      userid=None
"""
  if not os.path.isfile(filename):
    f = open(filename+".py", "w") 
    f.write(mystr.format(myclass=filename))
    f.close()

    myfavdirectory="myfavdirectory"
    myhtml="myhtml"
    with open("./script.py", "r") as f:
      contents = f.readlines()
    scriptfunc="""
def {myclass}(params):
  Program={myclass}page("./{myfavdirectory}","super website",params)
  return render_figure("{myhtml}.html",Program)

"""
    index=[i for i in range(len(contents)) if "class S(BaseHTTPRequestHandler):" in contents[i]][0]
    contents.insert(index, scriptfunc.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
    contents.insert(1, "from {myclass} import {myclass}page\n".format(myclass=filename))
    myrouteget="\"/{myclass}\":{myclass},\n"
    index=[i for i in range(len(contents)) if "myroutes = {" in contents[i]][0]
    contents.insert((index+1), myrouteget.format(myclass=filename))
    index=[i for i in range(len(contents)) if "def reloadmymodules" in contents[i]][0]
    contents.insert((index+1), "  reload({myclass})\n".format(myclass=filename))

    with open("./script.py", "w") as f:
        contents = "".join(contents)
        f.write(contents)
    os.system("mkdir %s" % myfavdirectory)
    os.system("touch %s/%s.html" % (myfavdirectory, myhtml))
    marouteget="\"/%s\"" % filename
    print("ma route get %s a été ajoutée. Maintenant vous pouvez essayer d'y acceder" % marouteget)

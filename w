import os
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/hom/mary/ionicsite')

class directory(object):
  def init(self, words):
    self.title = words
    self.text = ""
  def path(self,path):
    self.path = path
  def file(self):
    self.path = path
  def text(self,text):
    self.text = self.text + text
  def run(self):
    self.path = path
Program = directory("burger king")

def render_figure(self, filename):
  with open(filename, 'w') as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write(Program.text)
    f.write("</body>\n")
    f.write("</html>\n")
  
Program.path("./menu")
def datareach():
  render_figure("datareach.html")
  other = open("./other/form1.html","r+")
  Program.text(other)
  mf = open("datareach.html","r+")
  _words= mf[-2]
  if _words_ == "endofcode":

    result=Program.run() #lancer formulaire
    Program.file(result) #sauver dans un fichier

os.system("python -m SimpleHTTPServer 8000")

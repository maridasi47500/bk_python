from directory import directory 
class erreur(directory):
  css="<link rel=\"stylesheet\" href=\"/css/erreur.css\"/>"
  def __init__(self,message):
    self.path="./"
    self.title="ERREUR "
    self.erreur=message
  def set_title(self,url):
    self.title=url+" : ERREUR"
  def set_erreur(self,err):
    self.erreur=err
  def get_erreur(self,err):
    return self.erreur
  def get_content(self):
    return "<p>%s</p>" % self.erreur

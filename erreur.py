from directory import directory 
class erreur(directory):
  css="<link rel=\"stylesheet\" href=\"/css/erreur.css\"/>"
  mimetype="html"
  erreur=""
  def __init__(self,message):
    self.path="./"
    self.title="ERREUR "
    self.erreur=message
  def set_title(self,url):
    self.title=url+" : ERREUR"
  def set_erreur(self,err):
    if self.erreur == "" or self.erreur is None:
      self.erreur="Erreur"
    if self.content == "" or self.content is None:
      self.content+= "<h6>%s</h6>" % (self.title)
    self.erreur+=str(err)
    self.content+= "<p>%s</p>" % (self.erreur)
  def get_erreur(self,err):
    return self.erreur

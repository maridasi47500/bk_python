from directory import directory
class infolocationpage(directory):
  def __init__(self,title,param):
    self.path="./store-locator"
    self.title=title
    self.param=param
    self.layout=False
    try:
      id=param["id"][0]
    except:
      id=None
    sql="select *, (lat - 0.2) as lata, (lon - 0.2) as lona,(lat - 0.2) as latb,(lon + 0.2) as lonb from bks where id = ?"
    sqlargs=(id,)
    templatename="mytemplate.html"
    errormessage="aucun bk de cet id"
    tablename="bks"
    x=self.display_collection_with_current_path(sql,sqlargs,templatename,errormessage,tablename,False,False,("lata","lona","latb","lonb"))
    self.set_content(x)
    print("INFO LOCATION")


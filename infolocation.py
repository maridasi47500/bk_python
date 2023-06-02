from directory import directory
class infolocationpage(directory):
  def __init__(self,title,param):
    self.path="./store-locator"
    self.title=title
    self.param=param
    self.layout=False
    self.content_from_file("myfile.html")
    print("INFO LOCATION")


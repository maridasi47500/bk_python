from directory import directory
class addresspage(directory): 
  def __init__(self,title,params):
    self.title=title
    self.path="./store-locator"
    self.only_set_header_withthispath("headersignin.html")
    f=self.get_file("address.html").read()
    self.set_content(f)

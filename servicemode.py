from directory import directory
class servicemodepage(directory):
  def __init__(self,title,params):
    self.title=title
    self.path="./store-locator"
    self.only_set_header_withthispath("headersignin.html")
    f=self.get_file("servicemode.html").read()
    self.set_content(f)
    print("fin de cod")


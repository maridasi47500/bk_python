from directory import directory
class servicemodepage(directory):
  def __init__(self,title,params):
    self.title=title
    self.path="./store-locator"
    self.set_css("")
    self.add_css("servicemode.css")
    self.only_set_header_withthispath("headersignin.html")
    f=self.get_file("servicemode.html").read().decode("utf-8")
    self.set_content(f)
    print("fin de cod")


global code

from directory import directory
class codepage(directory):
    def __init__(self,title):
        self.set_title(title)
        print("code")
        self.set_path("./mespages")
        f=open(self.get_filename_path("userconnecte.js"),'r')
        js=f.read()
        ff=open(self.get_filename_path("code.html"),'r')
        text=ff.read()
        self.set_path("./js")
        self.add_js("userconnecte.js")
        self.set_header(self.get_header())
        self.set_footer(self.get_footer())
        self.set_path("./code")
        self.set_content(unicode(text,'utf-8'))

global signin
from directory import directory
class signinpage(directory):
    def __init__(self,title):
        self.title=title
        print("sign in")
        self.set_path("./mespages")
        f=open(self.get_filename_path("userconnecte.js"))
        js=f.read()
        fff=open(self.get_filename_path("headersignin.html"))
        myheader=fff.read()
        self.set_title("Burger King")

        ff=open(self.get_filename_path("signin.html"))
        text=ff.read()
        self.set_js("")
        self.set_header(myheader)
        self.set_path("./css")
        self.add_css("signin.css")
        self.set_path("./js")
        self.add_js("signin.js")
        self.set_footer("")
        self.set_path("./signin")
        self.set_content(text)

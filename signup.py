global signup
from directory import directory
class signuppage(directory):
    def __init__(self,title):
        self.title=title
        print("sign up")
        self.set_path("./mespages")
        self.css=""
        self.js=""
        f=open(self.get_filename_path("userconnecte.js"))
        js=f.read()
        fff=open(self.get_filename_path("headersignin.html"))
        myheader=fff.read()

        ff=open(self.get_filename_path("/signup.html"))
        text=ff.read()
        self.set_title("Burger King")
        self.set_js("")
        self.set_header(myheader)
        self.set_path("./css")
        self.add_css("signin.css")
        self.set_path("./js")
        self.add_js("signin.js")
        self.set_footer("")
        self.set_path("./signup")
        self.set_content(unicode(text,'utf-8'))

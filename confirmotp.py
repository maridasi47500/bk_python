global confirmotp
from directory import directory
class confirmotppage(directory):
    def __init__(self,title):
        self.title=title
        print("confirm otp func")
        print(params)
        print(session.current_user)
        email=session.current_user[2]
        print(email)
        if email is not None:
            self.set_title("Burger King")
            self.set_path("./mespages")
            print("confirm otp")
            f=open(self.get_filename_path("userconnecte.js"))
            js=f.read()
            print("user connectes")
            self.set_email(email)
            print("email")
            ff=open(self.get_filename_path("confirmotp.html"))
            text=ff.read()
            print("text length : "+str(len(text)))
            self.set_js("")
            fff=open(self.get_filename_path("headersignin.html"))
            myheader=fff.read()
            print("header")
            self.set_header(myheader)
            self.set_path("./css")
            self.add_css("signin.css")
            self.set_path("./js")
            self.add_js("signin.js")
            self.set_footer("")
            self.set_path("./signup")
            self.set_mimetype("html")
            print("confirm otp return program")
            self.set_content(unicode(text,'utf-8'))


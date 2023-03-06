global confirmotp
import directory
def confirmotp(params=None):
    try:
        Program=directory("bk")
        print("confirm otp func")
        print(params)
        print(session.current_user)
        email=session.current_user[2]
        print(email)
        if email is not None:
            Program.set_title("Burger King")
            Program.set_path("./mespages")
            print("confirm otp")
            f=open(Program.get_filename_path("userconnecte.js"))
            js=f.read()
            print("user connectes")
            Program.set_email(email)
            print("email")
            ff=open(Program.get_filename_path("confirmotp.html"))
            text=ff.read()
            print("text length : "+str(len(text)))
            Program.set_js("")
            fff=open(Program.get_filename_path("headersignin.html"))
            myheader=fff.read()
            print("header")
            Program.set_header(myheader)
            Program.set_path("./css")
            Program.add_css("signin.css")
            Program.set_path("./js")
            Program.add_js("signin.js")
            Program.set_footer("")
            Program.set_path("./signup")
            Program.set_mimetype("html")
            print("confirm otp return program")
            Program.set_content(unicode(text,'utf-8'))
            return Program
    except Exception as e:
        print("erreur confirm otp",e)

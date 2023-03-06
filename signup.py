global signup
def signup(params = None):
    try:
        print("sign up")
        Program.set_path("./mespages")

        f=open(Program.get_filename_path("userconnecte.js"))
        js=f.read()
        fff=open(Program.get_filename_path("headersignin.html"))
        myheader=fff.read()

        ff=open(Program.get_filename_path("/signup.html"))
        text=ff.read()
        Program.set_title("Burger King")
        Program.set_js("")
        Program.set_header(myheader)
        Program.set_path("./css")
        Program.add_css("signin.css")
        Program.set_path("./js")
        Program.add_js("signin.js")
        Program.set_footer("")
        Program.set_path("./signup")
        Program.set_content(unicode(text,'utf-8'))
        return render_figure("index.html")
    except Exception as e:
        print("erreur sign in",e)
global signin
import directory
def signin(params = None):
    try:
        Program=directory("")
        print("sign in")
        Program.set_path("./mespages")
        f=open(Program.get_filename_path("userconnecte.js"))
        js=f.read()
        fff=open(Program.get_filename_path("headersignin.html"))
        myheader=fff.read()
        Program.set_title("Burger King")

        ff=open(Program.get_filename_path("signin.html"))
        text=ff.read()
        Program.set_js("")
        Program.set_header(myheader)
        Program.set_path("./css")
        Program.add_css("signin.css")
        Program.set_path("./js")
        Program.add_js("signin.js")
        Program.set_footer("")
        Program.set_path("./signin")
        Program.set_content(text)
        return render_figure("index.html")
        Program.set_css("")
        Program.set_js("")
    except Exception as e:
        print("erreur sign in",e)
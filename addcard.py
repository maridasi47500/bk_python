global addcard
import directory
def addcard(params = None):
    try:
        Program=directory("")
        Program.set_path("./mespages")
        j=codecs.open(Program.get_filename_path("addcard.html"))
        Program.set_path("./css")
        Program.add_css("signin.css")
        Program.add_css("addcard.css")
        Program.add_js("addcard.js")
        text=force_to_unicode(j.read())
        Program.set_content(text)
        Program.set_path("./mespages")
        k=codecs.open(Program.get_filename_path("headeroverlay.html"))
        headertext=k.read()
        Program.set_header(headertext)

        return render_figure("ma page.html")
    except:
        print("erreur add card")
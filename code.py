global code
import directory
def code(params = None):
    try:
        Program=directory("")
        print("code")
        Program.set_path("./mespages")
        f=open(Program.get_filename_path("userconnecte.js"),'r')
        js=f.read()
        Program.set_title("Burger King")

        ff=open(Program.get_filename_path("code.html"),'r')
        text=ff.read()
        Program.set_path("./js")
        Program.add_js("userconnecte.js")
        Program.set_header(Program.get_header())
        Program.set_footer(Program.get_footer())
        Program.set_path("./code")
        Program.set_content(unicode(text,'utf-8'))
        return render_figure("index.html")
    except Exception as e:
        print("erreur 3",e)
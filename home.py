global home
import directory
def home(params = None):
    try:
        Program=directory("bk")
        Program.set_path("./")
        print("home")
        Program.set_title("Burger King")
        print("burger ing")
        Program.set_path("./mespages")
        print('hi')
        Program.set_header_with_path("header.html")
        Program.set_footer_with_path("footer.html")

        j=codecs.open(Program.get_filename_path("index.html"))
        text=j.read()
        print("my text")
        result = re.search("<div class=\"burgers-list\">(.*)</div>",text)
        #print(result.group(1))
        crsr.execute("SELECT * FROM burgers")
        mycontent="<ul>"
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")
        for myburger in ans:
            mycontent+= ajoutlistburger(myburger)
        print("burgervalue")
        mycontent+="</ul>"
        print(mycontent)
        if result is not None and len(result.group(1)) > 0:
            text=text.replace(result.group(1),mycontent)
        print("cards1")
        crsr.execute("SELECT * FROM cards")
        print("cards")
        mycontent=""
        # store all the fetched data in the ans variable
        ans = crsr.fetchall()
        print("allcards")
        print("cads")
        for x in ans:
            mycontent+= card(x[1],x[2],x[3])
        #print(mycontent)
        result = re.search("<div class=\"mycards\">(.*)</div>",text)
        if result is not None:
            print(result)
            print(result.group(1))
            if len(result.group(1)) > 0:
                text=text.replace(result.group(1),mycontent)
        Program.set_path("./")
        Program.set_content(text)

        text=(text)
        print("render figure home")
        return render_figure("index.html")
    except Exception as e:
        print("erreur 1",e)
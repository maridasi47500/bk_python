global home
import directory 
class pagehome(directory):
    def __init__(self,title):
        self.title=title
        self.set_path("./")
        self.set_title("Burger King")
        self.set_path("./mespages")
        print('hi')
        self.set_header_with_path("header.html")
        self.set_footer_with_path("footer.html")

        j=codecs.open(self.get_filename_path("index.html"))
        text=j.read()
        print("my text")
        #print(result.group(1))
        crsr.execute("SELECT * FROM burgers")
        mycontent="<ul>"
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")

        print(mycontent)
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
        montitreici="mon titre ici"
        text = text % (mycontent,montitreici)
        Program.set_path("./")
        Program.set_content(text)

        text=(text)


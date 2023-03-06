import directory
global menu
def menu(params = None):
    try:
        Program=directory("bk")
        Program.set_title("Burger King")
        Program.set_path("./mespages")
        j=codecs.open(Program.get_filename_path("menu.html"))
        text=j.read()
        result = re.search("<nav class=\"mytabs\"><ul>(.*)</ul></nav>",text)
        #print(result.group(1))
        crsr.execute("SELECT * FROM cats")
        mycontent=""
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")
        for myburger in ans:
            #print("burger",myburger[1],mycontent)
            mycontent+= "<li class=\"mycat\"><a href=\"/menu/"+repr(myburger[0] if myburger[0] > 1 else '')+"\">"+(myburger[1]).encode('utf-8')+"</a></li>"
        if result is not None and len(result.group(1)) > 0:
            text=text.replace(result.group(1),mycontent)
        for myburger in ans:
            mesburgers=""
            print("burger?!%*#")
            crsr.execute("SELECT * FROM burgers where cat_id = '"+repr(myburger[0])+"'")
            res=re.search("<div class=\"myitems\"><ul>(.*?)</ul></div>",text)
            ans1 = crsr.fetchall()
            for burger in ans1:
                #print("burger",burger[1])
                print("erreur ici")
                displaythisburger(burger,myburger[1],myburger[0])
                print("myerreur")
                mesburgers+= listburger(burger)
                print("erreur")
            if mesburgers == "":
                mesburgers = "mes items ici"
            if res is not None and len(res.group(1)) > 0:
                text=text.replace(res.group(1),mesburgers)
            print("burgervalue")
            #print(myburger[1])

            Program.set_path("./menu")
            Program.set_content(text)
            page=str(myburger[0] if myburger[0] > 1 else 'index')
            return render_figure(page+".html")
    except Exception as e:
        print("erreur menu",e)
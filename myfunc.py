def render_figure(pathname):
    try:
        Program.set_filename(pathname)

        print("render figure")
        print('ok')
        p1=Program.get_path
        p2=Program.get_filename
        print("okdac")
        print(p1())
        print("okokdac")
        print(p2())
        print(p1()+p2())
        print('dac')
        title=Program.get_title
        try:
            print(session.current_user)
            h=open("./mespages/mynavsignedin.html",'r')
            Program.set_menu(unicode(h.read(),"utf-8"))
        except:
            h=open("./mespages/mynav.html",'r')
            Program.set_menu(unicode(h.read(),"utf-8"))
        header=Program.get_header
        content=Program.get_content
        footer=Program.get_footer
        html="<!doctype html>"
        html+="<html>"
        html+="<head>"
        html+="<meta charset=\"UTF-8\">"
        html+="<title>"
        print("title")
        html+=title()
        html+="</title>"
        html+="<link rel=\"icon\" href=\"/images/logo.png\">"
        html+="<link rel=\"stylesheet\" href=\"/css/css.css\"/>"
        html+=Program.get_css()
        html+="</head>"
        html+="<body>"
        print("header")
        html+=header()
        html+="<main>"
        print("content")
        try:
            html+=myparams(content())
        except Exception as e: 
            html+=myparams(content().encode("utf-8"))
        print("footer")
        print("type footer")
        
        print(type(footer()))
        
        try:
            html+=footer()
        except UnicodeEncodeError as e:
            print(type(e))
            print('gerer cette erreur')
            html+=footer().encode('utf-8')
        except UnicodeDecodeError as e:
            print(type(e))
            print('gerer cette erreur')
            html+=footer().encode('utf-8')
        html+="</main>"    
        html+=Program.get_menu()
        html+="<script src=\"/js/jquery.js\"></script>"
        html+="<script src=\"/js/js.js\"></script>"
        html+=Program.get_js()
        html+="</body>"
        html+="</html>"
        #print(html)

        result = re.search('<li class=\"mycat\">(.*?)</li>', html)
        #print(result.group(1))
        __words__ = result.group(1) if result is not None else ''
        print("===words")
        #print(__words__)
        mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        print(mychemin)
        #try:
        #    s1=(html)
        #except Exception as e:
        #    print(e)
        #    s1=(html)
        #    print(type(s1))
        #s1=(html).encode("ascii", "ignore")
        print(type(html))
        if isinstance(html,str):
            s1=html
        else:    
            s1=html.encode('utf-8')
        
        f=codecs.open(mychemin,'w')
        print(type(s1))
        f.write(s1)
        f.close()
        #if (__words__).rstrip() == "Full Menu":
        print(Program.get_path())
        if Program.get_path()+"/"+Program.get_filename() == path1+"/code/index.html":
            if len(argv) == 2:
                run(port=int(argv[1]))
            else:
                run()    
    except Exception as e:
        print(e,'erreru')
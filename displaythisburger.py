import directory
global customizemymenu
global pagedisplaythisburger
class pagedisplaythisburger(directory)
    def __init__(self,title):
        self.title=title
    def __init__(self,title,catid,catname):
        self.title=title
        text="<a href=\"/menu/"+repr(catid)+"\">retour au menu "+catname+"</a>"
        text+=mycard(burger[1],str(burger[4])+"€","min "+str(burger[5])+" cal")


def displaythisburger(burger,catname,catid):
    try:
        Program=pagedisplaythisburger('burger king',atname,catid) 

        print("display this burger")
        print(type(catid))
        print(type(catname))
        print(type(burger[0]))
        print(type(burger[1]))
        print(type(burger[2]))
        print(type(burger[3]))
        print(type(burger[4]))
        print(type(burger[5]))
        Program.set_path("./burgers")
        code=render_figure(str(burger[0])+".html")
        Program.file("html","/burger/"+str(burger[0]),code)
        return Program
    except Exception as e:
        print('erreur display burger',e)
from directory import directory
import os
class servicemodepage(directory):
  def __init__(self,title,params):
    self.title=title
    self.path="./store-locator"
    self.set_css("")
    self.add_css("servicemode.css")
    self.only_set_header_withthispath("headersignin.html")
    f=self.get_file("servicemode.html").read().decode("utf-8")

    self.add_css_link("https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.css")
    self.add_js_link("https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.js")
    print("fin de cod")
    self.add_css_link("https://maps.locationiq.com/v2/libs/leaflet-geocoder/1.9.6/leaflet-geocoder-locationiq.min.css")
    self.add_js_link("https://maps.locationiq.com/v2/libs/leaflet-geocoder/1.9.6/leaflet-geocoder-locationiq.min.js")

    a=self.get_file(".\leaflet_withoutmap.js").read()
    a=a.replace("{GEOCODERAPIKEY}",os.environ['GEOCODERAPIKEY'])
    self.add_css("leaflet_withoumap.css")
    self.add_js("myleaflet.js")
    self.set_content(f+a)

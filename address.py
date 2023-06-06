from directory import directory
import os
class addresspage(directory): 
  def __init__(self,title,params):
    self.title=title
    self.path="./store-locator"
    self.only_set_header_withthispath("headersignin.html")


    self.set_css("")
    self.add_css("servicemode.css")
    self.only_set_header_withthispath("headersignin.html")
    f=self.get_file("address.html").read().decode('utf-8')

    self.add_css_link("https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.css")
    self.add_js_link("https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.3/leaflet.js")
    self.add_css_link("https://maps.locationiq.com/v2/libs/leaflet-geocoder/1.9.6/leaflet-geocoder-locationiq.min.css")
    self.add_js_link("https://maps.locationiq.com/v2/libs/leaflet-geocoder/1.9.6/leaflet-geocoder-locationiq.min.js")
    #add marker
    self.add_css_link("https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/css/ol.css")
    self.add_js_link("https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/build/ol.js")
    self.add_css("servicemode.css")
    self.add_js("address.js")

    #a=self.get_file("./leaflet.js").read().encode('utf-8').replace('{GEOCODERAPIKEY}',os.environ['GEOCODERAPIKEY'])
    self.set_content(f+a)
    print("fin de cod")

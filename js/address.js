var layer,coordinate,closer,content,container,map,overlay,attribution;
function sefairelivrer(){
$.ajax({url:"/findaddress",data:{address:$("#addresstext").val()},success:function(data){
//#mymap.innerHTML="";
console.log(parseFloat(data.lat),parseFloat(data.lon))
//mylongfunc(parseFloat(data.lat),parseFloat(data.lon))
mybtn.dataset.lat=data.lat;
mybtn.dataset.lon=data.lon;
mybtn.click()

}})
}

function mylongfunc(lat = null,lon = null){
console.log("init map")
initmap(lat,lon)
console.log("ajouter un marqueur")
//ajouterunmarqueur(lat,lon)
//console.log("ajouter une popup")
//mymap.outerHTML=mymap.outerHTML+`
// <div id="popup" class="ol-popup">
//     <a href="#" id="popup-closer" class="ol-popup-closer"></a>
//     <div id="popup-content"></div>
// </div>
//
//
//`;
//console.log("init popup")
//init_la_popup();
//console.log("ouvrir popup");
//ouvrirpopupclickmarqueur();
//console.log("text popup");
//ouvrirpopup_quand_crate_chfargee(lat,lon)
}

function initmap(mylat = 4.35247, mylon = 50.84673){
attribution = new ol.control.Attribution({
     collapsible: false
 });

 map = new ol.Map({
     controls: ol.control.defaults({attribution: false}).extend([attribution]),
     layers: [
         new ol.layer.Tile({
             source: new ol.source.OSM({
                 url: 'https://tile.openstreetmap.be/osmbe/{z}/{x}/{y}.png',
                 attributions: [ ol.source.OSM.ATTRIBUTION, 'Tiles courtesy of <a href="https://geo6.be/">GEO-6</a>' ],
                 maxZoom: 18
             })
         })
     ],
     target: 'mymap',
     view: new ol.View({
         center: ol.proj.fromLonLat([mylon,mylat]),
         maxZoom: 18,
         zoom: 12
     })
 });
 overlay = new ol.Overlay({
     element: container,
     autoPan: true,
     autoPanAnimation: {
         duration: 250
     }
 });
 map.addOverlay(overlay);
}
window.onload=function(){ 
initmap();
//mylongfunc();
}
function ajouterunmarqueur(lat= 4.35247, lon = 50.84673){
 layer = new ol.layer.Vector({
     source: new ol.source.Vector({
         features: [
             new ol.Feature({
                 geometry: new ol.geom.Point(ol.proj.fromLonLat([lon,lat]))
             })
         ]
     })
 });
 map.addLayer(layer);
}
function init_la_popup(){
 container = document.getElementById('popup');
 content = document.getElementById('popup-content');
 closer = document.getElementById('popup-closer');



 closer.onclick = function() {
     overlay.setPosition(undefined);
     closer.blur();
     return false;
 };
}
//ouvrir la popup quand on cliue sur le marker
function ouvrirpopupclickmarqueur(){
map.on('singleclick', function (event) {
     if (map.hasFeatureAtPixel(event.pixel) === true) {
         coordinate = event.coordinate;

         content.innerHTML = '<b>Hello!</b><br />la livraison arrivera ici.';
         overlay.setPosition(coordinate);
     } else {
         overlay.setPosition(undefined);
     }
 });
//}
}

function ouvrirpopup_quand_crate_chfargee(lat,lon){
 content.innerHTML = '<b>Hello world!</b><br />I am a popup.';
 overlay.setPosition(ol.proj.fromLonLat([lon,lat]));
}


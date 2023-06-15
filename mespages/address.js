var layer,coordinate,closer,content,container,map,overlay,attribution;
function deliverhere(){
$.ajax({url:"/searchrestaurant",data:{lat:$("#livrerici")[0].dataset.lat,lon:$("#livrerici")[0].dataset.lon},success:function(data){
console.log(data);
if (data.restauranttrouve === "1"){
window.location="/redeem/";
}
}});
return false;
}
function sefairelivrer(){
$.ajax({url:"/findaddress",data:{address:$("#addresstext").val()},success:function(data){
//#var layer,coordinate,closer,content,container,map,overlay,attribution;
if (data.jsonenvoye === "resultat"){
var livrerici=document.querySelector("#livrerici");
livrerici.dataset.lat=data.lat;
livrerici.dataset.lon=data.lon;
var mymap=document.querySelector("#mymap");
mymap.outerHTML="<div id=\"mymap\" class=\"result\"></div>";
var popup=document.querySelector("#popup");
if (popup){
popup.remove()
}
document.body.innerHTML+=" <div id=\"popup\" class=\"ol-popup\">     <a href=\"#\" id=\"popup-closer\" class=\"ol-popup-closer\">x</a>  <div id=\"popup-content\"></div> </div>";
console.log(parseFloat(data.lat),parseFloat(data.lon))
mylongfunc(parseFloat(data.lat),parseFloat(data.lon))
$(".addressnonreconnue").addClass("addressereconnue");
$(".deliver").removeClass("notdeliver");
$("[name=address]").removeClass("myerror");
} else {
$(".addressnonreconnue").removeClass("addressereconnue");

$(".deliver").addClass("notdeliver");
$("[name=address]").addClass("myerror");

}

}})
}

function mylongfunc(lat = null,lon = null){
console.log("init map")
initmap(lat,lon)
console.log(lat,lon,"ajouter un marqueur")
ajouterunmarqueur(lat,lon)
console.log(lat,lon,"ajouter une popup")

console.log(lat,lon,"init popup")
init_la_popup();
console.log(lat,lon,"ouvrir popup");
ouvrirpopupclickmarqueur();
console.log(lat,lon,"text popup");
ouvrirpopup_quand_crate_chfargee(lat,lon)
}

function initmap(mylat = 50.84673, mylon = 4.35247){
//alert(mylat+"+"+mylon+"+"+typeof mylat)
attribution = new ol.control.Attribution({
     collapsible: false
 });

 map = new ol.Map({
     controls: ol.control.defaults({attribution: false}).extend([attribution]),
     layers: [
         new ol.layer.Tile({
             source: new ol.source.OSM({
                 url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
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
}
function ajouterunmarqueur(lat = 50.84673, lon = 4.35247){
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
 console.log(container,content,closer);

 overlay = new ol.Overlay({
     element: container,
     autoPan: true,
     autoPanAnimation: {
         duration: 250
     }
 });
 map.addOverlay(overlay);



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
 content.innerHTML = '<b>Hello world!</b><br />Livraison ici.';
 //overlay.setPosition(ol.proj.fromLonLat([lon,lat]));
}

window.onload=function(){ 
var layer,coordinate,closer,content,container,map,overlay,attribution;
initmap();
//mylongfunc();
}

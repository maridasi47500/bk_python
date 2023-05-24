function clicklocation(ev){
var loc=ev.target;
var id=loc.dataset.id;
var action=loc.dataset.action;
$.ajax({url:"/bkaction",data:{id: id, action:action},success:function(data){
}});

}

function cherchermcdo(){
$.ajax({url: "/listlocation",data: {mylist: "nearby",lat: $('#lat').html(),lon: $('#lon').html(),address:$('#address').val()},
success:function(data){
$('#result').html(data);
}});
return false;
}
window.onload=function(){
$(".tab2").click(function(){
window.location = "/store-locator/address";
});
$(".tabs-list *").click(function(){
$('.tabs-list *').removeClass("selected");
$(this).toggleClass("selected");
$.ajax({url: "/listlocation",data: {mylist: $(this).data('mylist'),lat: $('#lat').html(),lon: $('#lon').html(),address:$('#address').val()},
success:function(data){
$('#result').html(data);
}});
});
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

function success(pos) {
  const crd = pos.coords;

  console.log("Your current position is:");
  console.log(`Latitude : ${crd.latitude}`);
  $('#lat').html(crd.latitude);
  console.log(`Longitude: ${crd.longitude}`);
  $('#lon').html(crd.longitude);
  console.log(`More or less ${crd.accuracy} meters.`);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(success, error, options);
}

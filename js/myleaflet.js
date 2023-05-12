window.onload=function(){
$(".tab2").click(function(){
window.location = "/store-locator/address";
});
$(".tabs-list *").click(function(){
$('.tabs-list *').removeClass("selected");
$(this).toggleClass("selected");
$.ajax({url: "/listlocation",data: {mylist: $(this).data('mylist'),lat: $('#lat').html(),lon: $('#lon').html()},
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

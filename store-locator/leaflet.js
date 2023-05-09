<script>
window.onload=function(){
var map = L.map('map').setView([40.7259, -73.9805], 12);
L.tileLayer('https://{s}-tiles.locationiq.com/v2/obk/r/{z}/{x}/{y}.png?key=<your_access_token>').addTo(map);
L.control.geocoder('{GEOCODERAPIKEY}').addTo(map);
}
</script>

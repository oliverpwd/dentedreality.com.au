---
title: ''
date: '2019-09-02T16:28:12-06:00'
format: image
service: instagram
latitude: '39.4078'
longitude: '-105.171'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/02182455/67753332_222928965339886_5447027396458705186_n.jpg?fit=640%2C640&ssl=1
---

[![EXTREEEME @jetboil -- making some lunch without a lot of riverbank to play with.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/02182455/67753332_222928965339886_5447027396458705186_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/09/02/extreeeme-jetboil-making-some-lunch-without-a-lot-of-riverbank-to-play-with/) 

[![EXTREEEME @jetboil -- making some lunch without a lot of riverbank to play with.](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/02182455/67753332_222928965339886_5447027396458705186_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B17PNOypYQW/)

EXTREEEME @jetboil — making some lunch without a lot of riverbank to play with.

39.4078-105.171




Posted on [Instagram](https://www.instagram.com/p/B17PNOypYQW/) [4:28 pm, September 2, 2019](https://dentedreality.com.au/2019/09/02/extreeeme-jetboil-making-some-lunch-without-a-lot-of-riverbank-to-play-with/ "4:28 pm") 
jQuery(document).ready(function(){
var gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1 = {
positions : {
266 : new google.maps.LatLng( '39.4078', '-105.171' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.positions ) {
gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.bounds.extend( gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.positions[m] );
}
// Render markers
for ( var m in gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.positions ) {
gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.map,
position : gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.map.setCenter( gmap\_mecd88ebd594a5fa0b6653def4a8ab0d1.positions[266] );
});
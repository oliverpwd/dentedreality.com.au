---
title: ''
date: '2017-04-27T00:55:10-06:00'
format: image
service: instagram
tags:
- corn
- grill
- lobster
- peppers
- seafood
- shrimp
- tuna
latitude: '9.7029733'
longitude: '-84.6605084'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2017/04/14182613/18094729_174844066372786_2994507737720684544_n.jpg
---

[![Tonight's grilled dinner was pretty absurd. Also delicious. #tuna #lobster #shrimp #peppers #corn #grill #seafood](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2017/04/14182613/18094729_174844066372786_2994507737720684544_n.jpg)](https://dentedreality.com.au/2017/04/27/tonights-grilled-dinner-was-pretty-absurd-also-delicious-tuna-lobster-shrimp-peppers-corn-grill-seafood/) 

[![Tonight's grilled dinner was pretty absurd. Also delicious. #tuna #lobster #shrimp #peppers #corn #grill #seafood](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2017/04/14182613/18094729_174844066372786_2994507737720684544_n.jpg)](https://www.instagram.com/p/BTYSYvVhTKp/)

Tonight’s grilled dinner was pretty absurd. Also delicious. #tuna #lobster #shrimp #peppers #corn #grill #seafood

9.7029733-84.6605084




* #[corn](https://dentedreality.com.au/tags/corn/)
* #[grill](https://dentedreality.com.au/tags/grill/)
* #[lobster](https://dentedreality.com.au/tags/lobster/)
* #[peppers](https://dentedreality.com.au/tags/peppers/)
* #[seafood](https://dentedreality.com.au/tags/seafood/)
* #[shrimp](https://dentedreality.com.au/tags/shrimp/)
* #[tuna](https://dentedreality.com.au/tags/tuna/)

Posted on [Instagram](https://www.instagram.com/p/BTYSYvVhTKp/) [12:55 am, April 27, 2017](https://dentedreality.com.au/2017/04/27/tonights-grilled-dinner-was-pretty-absurd-also-delicious-tuna-lobster-shrimp-peppers-corn-grill-seafood/ "12:55 am") 
jQuery(document).ready(function(){
var gmap\_m63f270b6679a68766abca9a784de0473 = {
positions : {
539 : new google.maps.LatLng( '9.7029733395391', '-84.660508412921' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m63f270b6679a68766abca9a784de0473' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m63f270b6679a68766abca9a784de0473.positions ) {
gmap\_m63f270b6679a68766abca9a784de0473.bounds.extend( gmap\_m63f270b6679a68766abca9a784de0473.positions[m] );
}
// Render markers
for ( var m in gmap\_m63f270b6679a68766abca9a784de0473.positions ) {
gmap\_m63f270b6679a68766abca9a784de0473.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m63f270b6679a68766abca9a784de0473.map,
position : gmap\_m63f270b6679a68766abca9a784de0473.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m63f270b6679a68766abca9a784de0473.map.setCenter( gmap\_m63f270b6679a68766abca9a784de0473.positions[539] );
});
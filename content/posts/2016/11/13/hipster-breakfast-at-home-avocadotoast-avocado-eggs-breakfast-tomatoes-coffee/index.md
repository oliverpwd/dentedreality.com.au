---
title: ''
date: '2016-11-13T11:47:36-06:00'
format: image
service: instagram
tags:
- avocado
- avocadotoast
- breakfast
- coffee
- eggs
- tomatoes
latitude: '39.7572'
longitude: '-104.967'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/11/15034631_208385996237211_2824659635342934016_n.jpg?fit=640%2C640
---

[![Hipster breakfast at home #avocadotoast #avocado #eggs #breakfast #tomatoes #coffee](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/11/15034631_208385996237211_2824659635342934016_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/11/13/hipster-breakfast-at-home-avocadotoast-avocado-eggs-breakfast-tomatoes-coffee/) 

[![Hipster breakfast at home #avocadotoast #avocado #eggs #breakfast #tomatoes #coffee](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/11/15034631_208385996237211_2824659635342934016_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BMwswTSDSCA/)

Hipster breakfast at home #avocadotoast #avocado #eggs #breakfast #tomatoes #coffee

39.7572-104.967




* #[avocado](https://dentedreality.com.au/tags/avocado/)
* #[avocadotoast](https://dentedreality.com.au/tags/avocadotoast/)
* #[breakfast](https://dentedreality.com.au/tags/breakfast/)
* #[coffee](https://dentedreality.com.au/tags/coffee/)
* #[eggs](https://dentedreality.com.au/tags/eggs/)
* #[tomatoes](https://dentedreality.com.au/tags/tomatoes/)

Posted on [Instagram](https://www.instagram.com/p/BMwswTSDSCA/) [11:47 am, November 13, 2016](https://dentedreality.com.au/2016/11/13/hipster-breakfast-at-home-avocadotoast-avocado-eggs-breakfast-tomatoes-coffee/ "11:47 am") 
jQuery(document).ready(function(){
var gmap\_mfcbd307d2a09c954872ba432b84b96e4 = {
positions : {
771 : new google.maps.LatLng( '39.7572', '-104.967' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfcbd307d2a09c954872ba432b84b96e4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfcbd307d2a09c954872ba432b84b96e4.positions ) {
gmap\_mfcbd307d2a09c954872ba432b84b96e4.bounds.extend( gmap\_mfcbd307d2a09c954872ba432b84b96e4.positions[m] );
}
// Render markers
for ( var m in gmap\_mfcbd307d2a09c954872ba432b84b96e4.positions ) {
gmap\_mfcbd307d2a09c954872ba432b84b96e4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfcbd307d2a09c954872ba432b84b96e4.map,
position : gmap\_mfcbd307d2a09c954872ba432b84b96e4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfcbd307d2a09c954872ba432b84b96e4.map.setCenter( gmap\_mfcbd307d2a09c954872ba432b84b96e4.positions[771] );
});
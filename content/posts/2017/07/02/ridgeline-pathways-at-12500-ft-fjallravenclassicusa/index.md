---
title: ''
date: '2017-07-02T22:16:38-06:00'
format: image
service: instagram
tags:
- fjallravenclassicusa
latitude: '39.4938756'
longitude: '-106.111132'
image: https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19535523_116104502340572_3718270174466408448_n.jpg?fit=640%2C640&ssl=1
---

[![Ridgeline pathways at 12,500 ft #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19535523_116104502340572_3718270174466408448_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/07/02/ridgeline-pathways-at-12500-ft-fjallravenclassicusa/) 

[![Ridgeline pathways at 12,500 ft #fjallravenclassicusa](https://i0.wp.com/dentedreality.com.au/wp-content/uploads/2017/07/19535523_116104502340572_3718270174466408448_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BWEhgNxBt8g/)

Ridgeline pathways at 12,500 ft #fjallravenclassicusa

39.4938756-106.111132




* #[fjallravenclassicusa](https://dentedreality.com.au/tags/fjallravenclassicusa/)

Posted on [Instagram](https://www.instagram.com/p/BWEhgNxBt8g/) [10:16 pm, July 2, 2017](https://dentedreality.com.au/2017/07/02/ridgeline-pathways-at-12500-ft-fjallravenclassicusa/ "10:16 pm") 
jQuery(document).ready(function(){
var gmap\_m5f8e33bf36f76065b2e9d7c96a685910 = {
positions : {
709 : new google.maps.LatLng( '39.4938756', '-106.111132' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5f8e33bf36f76065b2e9d7c96a685910' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5f8e33bf36f76065b2e9d7c96a685910.positions ) {
gmap\_m5f8e33bf36f76065b2e9d7c96a685910.bounds.extend( gmap\_m5f8e33bf36f76065b2e9d7c96a685910.positions[m] );
}
// Render markers
for ( var m in gmap\_m5f8e33bf36f76065b2e9d7c96a685910.positions ) {
gmap\_m5f8e33bf36f76065b2e9d7c96a685910.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5f8e33bf36f76065b2e9d7c96a685910.map,
position : gmap\_m5f8e33bf36f76065b2e9d7c96a685910.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5f8e33bf36f76065b2e9d7c96a685910.map.setCenter( gmap\_m5f8e33bf36f76065b2e9d7c96a685910.positions[709] );
});
---
title: ''
date: '2016-07-30T10:09:02-06:00'
format: image
service: instagram
tags:
- bwca
latitude: '48.1564649'
longitude: '-90.8717844'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827344_875735252556799_1606538604_n.jpg?fit=640%2C640
---

[![Final sunset. #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827344_875735252556799_1606538604_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/30/final-sunset-bwca/) 

[![Final sunset. #bwca](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13827344_875735252556799_1606538604_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BIfeWP4gT-Y/)

Final sunset. #bwca

48.1564649-90.8717844




* #[bwca](https://dentedreality.com.au/tags/bwca/)

Posted on [Instagram](https://www.instagram.com/p/BIfeWP4gT-Y/) [10:09 am, July 30, 2016](https://dentedreality.com.au/2016/07/30/final-sunset-bwca/ "10:09 am") 
jQuery(document).ready(function(){
var gmap\_m4e7594ef2b91a80fa047b8e172c4a28d = {
positions : {
827 : new google.maps.LatLng( '48.15646494', '-90.871784434' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4e7594ef2b91a80fa047b8e172c4a28d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.positions ) {
gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.bounds.extend( gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.positions[m] );
}
// Render markers
for ( var m in gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.positions ) {
gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.map,
position : gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.map.setCenter( gmap\_m4e7594ef2b91a80fa047b8e172c4a28d.positions[827] );
});
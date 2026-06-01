---
title: ''
date: '2014-03-14T11:22:39+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/928210_485916541534395_1877223305_n.jpg?resize=640%2C640
---

[![Jazzing.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/928210_485916541534395_1877223305_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/03/14/jazzing/) 

Jazzing.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/lh5HhrimNd/) [11:22 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/jazzing/ "11:22 am") 
jQuery(document).ready(function(){
var gmap\_mcb0da7677560d72c631a1f0a3504cfa7 = {
positions : {
125 : new google.maps.LatLng( '-31.946388027', '115.864213463' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcb0da7677560d72c631a1f0a3504cfa7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcb0da7677560d72c631a1f0a3504cfa7.positions ) {
gmap\_mcb0da7677560d72c631a1f0a3504cfa7.bounds.extend( gmap\_mcb0da7677560d72c631a1f0a3504cfa7.positions[m] );
}
// Render markers
for ( var m in gmap\_mcb0da7677560d72c631a1f0a3504cfa7.positions ) {
gmap\_mcb0da7677560d72c631a1f0a3504cfa7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcb0da7677560d72c631a1f0a3504cfa7.map,
position : gmap\_mcb0da7677560d72c631a1f0a3504cfa7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcb0da7677560d72c631a1f0a3504cfa7.map.setCenter( gmap\_mcb0da7677560d72c631a1f0a3504cfa7.positions[125] );
});
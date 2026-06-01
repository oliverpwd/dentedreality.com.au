---
title: IMG_0736
date: '2010-12-31T17:17:49+00:00'
format: image
service: flickr
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434096509_3cdb8d9314_o.jpg?resize=607%2C452
---

[![IMG_0736](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/12/5434096509_3cdb8d9314_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/12/31/img_0736/) 
# [IMG\_0736](http://dentedreality.com.au/2010/12/31/img_0736/)





Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434096509/) [5:17 pm, December 31, 2010](http://dentedreality.com.au/2010/12/31/img_0736/ "5:17 pm") 
jQuery(document).ready(function(){
var gmap\_m9fede16519182b81f5aa2e69b27db20e = {
positions : {
895 : new google.maps.LatLng( '-31.9095', '115.831666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9fede16519182b81f5aa2e69b27db20e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9fede16519182b81f5aa2e69b27db20e.positions ) {
gmap\_m9fede16519182b81f5aa2e69b27db20e.bounds.extend( gmap\_m9fede16519182b81f5aa2e69b27db20e.positions[m] );
}
// Render markers
for ( var m in gmap\_m9fede16519182b81f5aa2e69b27db20e.positions ) {
gmap\_m9fede16519182b81f5aa2e69b27db20e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9fede16519182b81f5aa2e69b27db20e.map,
position : gmap\_m9fede16519182b81f5aa2e69b27db20e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9fede16519182b81f5aa2e69b27db20e.map.setCenter( gmap\_m9fede16519182b81f5aa2e69b27db20e.positions[895] );
});
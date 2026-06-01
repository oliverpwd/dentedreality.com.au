---
title: ''
date: '2015-05-23T16:26:59+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11348209_1419807185008715_52608704_n.jpg?resize=640%2C640
---

[![Dome](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2015/05/11348209_1419807185008715_52608704_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/05/23/dome/) 

Dome





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/3Comt_imPZ/) [4:26 pm, May 23, 2015](http://dentedreality.com.au/2015/05/23/dome/ "4:26 pm") 
jQuery(document).ready(function(){
var gmap\_m694704430c6ff138b14d17341f30643f = {
positions : {
624 : new google.maps.LatLng( '37.784287474', '-122.406335453' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m694704430c6ff138b14d17341f30643f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m694704430c6ff138b14d17341f30643f.positions ) {
gmap\_m694704430c6ff138b14d17341f30643f.bounds.extend( gmap\_m694704430c6ff138b14d17341f30643f.positions[m] );
}
// Render markers
for ( var m in gmap\_m694704430c6ff138b14d17341f30643f.positions ) {
gmap\_m694704430c6ff138b14d17341f30643f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m694704430c6ff138b14d17341f30643f.map,
position : gmap\_m694704430c6ff138b14d17341f30643f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m694704430c6ff138b14d17341f30643f.map.setCenter( gmap\_m694704430c6ff138b14d17341f30643f.positions[624] );
});
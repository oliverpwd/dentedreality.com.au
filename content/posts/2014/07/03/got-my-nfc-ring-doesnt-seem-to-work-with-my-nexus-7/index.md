---
title: ''
date: '2014-07-03T11:24:23+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10514052_683266901709045_1381603828_n.jpg?resize=640%2C640
---

[![Got my NFC Ring... doesn't seem to work with my Nexus 7 :(](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2014/07/10514052_683266901709045_1381603828_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/07/03/got-my-nfc-ring-doesnt-seem-to-work-with-my-nexus-7/) 

Got my NFC Ring… doesn’t seem to work with my Nexus 7 ![:(](http://i1.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_sad.gif?w=607)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/p_tjZyimIx/) [11:24 am, July 3, 2014](http://dentedreality.com.au/2014/07/03/got-my-nfc-ring-doesnt-seem-to-work-with-my-nexus-7/ "11:24 am") 
jQuery(document).ready(function(){
var gmap\_mb8b43530234d66fce73696da8412cd88 = {
positions : {
295 : new google.maps.LatLng( '40.669333333', '-73.984908333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb8b43530234d66fce73696da8412cd88' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb8b43530234d66fce73696da8412cd88.positions ) {
gmap\_mb8b43530234d66fce73696da8412cd88.bounds.extend( gmap\_mb8b43530234d66fce73696da8412cd88.positions[m] );
}
// Render markers
for ( var m in gmap\_mb8b43530234d66fce73696da8412cd88.positions ) {
gmap\_mb8b43530234d66fce73696da8412cd88.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb8b43530234d66fce73696da8412cd88.map,
position : gmap\_mb8b43530234d66fce73696da8412cd88.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb8b43530234d66fce73696da8412cd88.map.setCenter( gmap\_mb8b43530234d66fce73696da8412cd88.positions[295] );
});
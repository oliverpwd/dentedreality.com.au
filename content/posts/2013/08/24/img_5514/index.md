---
title: Bear Mountain Bridge
date: '2013-08-24T10:16:28+00:00'
format: image
tags:
- anthony's nose
- bear mountain
- bridge
- hiking
- new york
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767973266_d58387352c_o.jpg?resize=607%2C452
---

[![IMG_5514](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/08/9767973266_d58387352c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/08/24/img_5514/) 
# [Bear Mountain Bridge](http://dentedreality.com.au/2013/08/24/img_5514/)

From Anthony’s Nose





* #[anthony's nose](http://dentedreality.com.au/tags/anthonys-nose/)
* #[bear mountain](http://dentedreality.com.au/tags/bear-mountain/)
* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[hiking](http://dentedreality.com.au/tags/hiking/)
* #[new york](http://dentedreality.com.au/tags/new-york/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9767973266/) [10:16 am, August 24, 2013](http://dentedreality.com.au/2013/08/24/img_5514/ "10:16 am") 
jQuery(document).ready(function(){
var gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0 = {
positions : {
393 : new google.maps.LatLng( '41.3185', '-73.976' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.positions ) {
gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.bounds.extend( gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.positions[m] );
}
// Render markers
for ( var m in gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.positions ) {
gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.map,
position : gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.map.setCenter( gmap\_mfa65ce69cbf78281df8ad15d5e1a0fe0.positions[393] );
});
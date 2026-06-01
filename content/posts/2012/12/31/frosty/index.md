---
title: Frosty
date: '2012-12-31T09:39:01+00:00'
format: image
service: flickr
tags:
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8331054610_962b8a913b_o.jpg?resize=607%2C452
---

[![Frosty](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8331054610_962b8a913b_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/31/frosty/) 
# [Frosty](http://dentedreality.com.au/2012/12/31/frosty/)





* #[flickriosapp:filter=nofilter](http://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](http://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8331054610/) [9:39 am, December 31, 2012](http://dentedreality.com.au/2012/12/31/frosty/ "9:39 am") 
jQuery(document).ready(function(){
var gmap\_meed2093e69d33f8ac3b201724effdebf = {
positions : {
186 : new google.maps.LatLng( '40.669999', '-73.990667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meed2093e69d33f8ac3b201724effdebf' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meed2093e69d33f8ac3b201724effdebf.positions ) {
gmap\_meed2093e69d33f8ac3b201724effdebf.bounds.extend( gmap\_meed2093e69d33f8ac3b201724effdebf.positions[m] );
}
// Render markers
for ( var m in gmap\_meed2093e69d33f8ac3b201724effdebf.positions ) {
gmap\_meed2093e69d33f8ac3b201724effdebf.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meed2093e69d33f8ac3b201724effdebf.map,
position : gmap\_meed2093e69d33f8ac3b201724effdebf.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meed2093e69d33f8ac3b201724effdebf.map.setCenter( gmap\_meed2093e69d33f8ac3b201724effdebf.positions[186] );
});
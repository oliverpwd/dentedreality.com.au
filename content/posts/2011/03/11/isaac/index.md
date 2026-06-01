---
title: Isaac
date: '2011-03-11T16:05:01+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802653238_c744638baf_o.jpg?resize=607%2C813
---

[![Isaac](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802653238_c744638baf_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/11/isaac/) 
# [Isaac](http://dentedreality.com.au/2011/03/11/isaac/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802653238/) [4:05 pm, March 11, 2011](http://dentedreality.com.au/2011/03/11/isaac/ "4:05 pm") 
jQuery(document).ready(function(){
var gmap\_m71136691c7bdf4fc965b53467e4d45ec = {
positions : {
594 : new google.maps.LatLng( '30.269666', '-97.749834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m71136691c7bdf4fc965b53467e4d45ec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m71136691c7bdf4fc965b53467e4d45ec.positions ) {
gmap\_m71136691c7bdf4fc965b53467e4d45ec.bounds.extend( gmap\_m71136691c7bdf4fc965b53467e4d45ec.positions[m] );
}
// Render markers
for ( var m in gmap\_m71136691c7bdf4fc965b53467e4d45ec.positions ) {
gmap\_m71136691c7bdf4fc965b53467e4d45ec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m71136691c7bdf4fc965b53467e4d45ec.map,
position : gmap\_m71136691c7bdf4fc965b53467e4d45ec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m71136691c7bdf4fc965b53467e4d45ec.map.setCenter( gmap\_m71136691c7bdf4fc965b53467e4d45ec.positions[594] );
});
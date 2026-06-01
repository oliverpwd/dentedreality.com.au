---
title: Affligem
date: '2010-06-17T17:27:10+00:00'
format: image
service: flickr
tags:
- affligem
- beer
- belgian
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/06/4748294904_87589676e1_o.jpg?resize=607%2C455
---

[![Affligem](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/06/4748294904_87589676e1_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/06/17/affligem/) 
# [Affligem](http://dentedreality.com.au/2010/06/17/affligem/)





* #[affligem](http://dentedreality.com.au/tags/affligem/)
* #[beer](http://dentedreality.com.au/tags/beer/)
* #[belgian](http://dentedreality.com.au/tags/belgian/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4748294904/) [5:27 pm, June 17, 2010](http://dentedreality.com.au/2010/06/17/affligem/ "5:27 pm") 
jQuery(document).ready(function(){
var gmap\_mb5342052e0cc41c8a5039ca524c52ce3 = {
positions : {
307 : new google.maps.LatLng( '37.796166', '-122.393834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb5342052e0cc41c8a5039ca524c52ce3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb5342052e0cc41c8a5039ca524c52ce3.positions ) {
gmap\_mb5342052e0cc41c8a5039ca524c52ce3.bounds.extend( gmap\_mb5342052e0cc41c8a5039ca524c52ce3.positions[m] );
}
// Render markers
for ( var m in gmap\_mb5342052e0cc41c8a5039ca524c52ce3.positions ) {
gmap\_mb5342052e0cc41c8a5039ca524c52ce3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb5342052e0cc41c8a5039ca524c52ce3.map,
position : gmap\_mb5342052e0cc41c8a5039ca524c52ce3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb5342052e0cc41c8a5039ca524c52ce3.map.setCenter( gmap\_mb5342052e0cc41c8a5039ca524c52ce3.positions[307] );
});
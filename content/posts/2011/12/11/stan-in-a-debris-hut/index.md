---
title: Stan in a debris hut
date: '2011-12-11T08:34:13+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- stan
- survival
- wilderness
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958325187_cd28afec03_o.jpg?resize=607%2C813
---

[![Stan in a debris hut](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958325187_cd28afec03_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut/) 
# [Stan in a debris hut](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut/)





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[stan](http://dentedreality.com.au/tags/stan/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958325187/) [8:34 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/stan-in-a-debris-hut/ "8:34 am") 
jQuery(document).ready(function(){
var gmap\_m09e74ab0505bcdac13b782b76dcc0416 = {
positions : {
40 : new google.maps.LatLng( '38.000833', '-122.611334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m09e74ab0505bcdac13b782b76dcc0416' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m09e74ab0505bcdac13b782b76dcc0416.positions ) {
gmap\_m09e74ab0505bcdac13b782b76dcc0416.bounds.extend( gmap\_m09e74ab0505bcdac13b782b76dcc0416.positions[m] );
}
// Render markers
for ( var m in gmap\_m09e74ab0505bcdac13b782b76dcc0416.positions ) {
gmap\_m09e74ab0505bcdac13b782b76dcc0416.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m09e74ab0505bcdac13b782b76dcc0416.map,
position : gmap\_m09e74ab0505bcdac13b782b76dcc0416.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m09e74ab0505bcdac13b782b76dcc0416.map.setCenter( gmap\_m09e74ab0505bcdac13b782b76dcc0416.positions[40] );
});
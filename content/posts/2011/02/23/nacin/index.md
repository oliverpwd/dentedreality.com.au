---
title: Nacin…
date: '2011-02-23T17:27:21+00:00'
format: image
service: flickr
tags:
- nacin
- newyork
- newyorkcity
- NYC
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802617312_9fc2365cb4_o.jpg?resize=607%2C452
---

[![Nacin...](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/02/5802617312_9fc2365cb4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/02/23/nacin/) 
# [Nacin…](http://dentedreality.com.au/2011/02/23/nacin/)

…is happy about his drinks





* #[nacin](http://dentedreality.com.au/tags/nacin/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)
* #[newyorkcity](http://dentedreality.com.au/tags/newyorkcity/)
* #[NYC](http://dentedreality.com.au/tags/nyc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802617312/) [5:27 pm, February 23, 2011](http://dentedreality.com.au/2011/02/23/nacin/ "5:27 pm") 
jQuery(document).ready(function(){
var gmap\_m78f8f4c359178f82433798fd8e7d4349 = {
positions : {
603 : new google.maps.LatLng( '40.759166', '-73.982667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m78f8f4c359178f82433798fd8e7d4349' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m78f8f4c359178f82433798fd8e7d4349.positions ) {
gmap\_m78f8f4c359178f82433798fd8e7d4349.bounds.extend( gmap\_m78f8f4c359178f82433798fd8e7d4349.positions[m] );
}
// Render markers
for ( var m in gmap\_m78f8f4c359178f82433798fd8e7d4349.positions ) {
gmap\_m78f8f4c359178f82433798fd8e7d4349.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m78f8f4c359178f82433798fd8e7d4349.map,
position : gmap\_m78f8f4c359178f82433798fd8e7d4349.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m78f8f4c359178f82433798fd8e7d4349.map.setCenter( gmap\_m78f8f4c359178f82433798fd8e7d4349.positions[603] );
});
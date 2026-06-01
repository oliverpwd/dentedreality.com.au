---
title: Party’s Over
date: '2012-12-31T20:26:18+00:00'
format: image
service: flickr
tags:
- flickriosapp:filter=iguana
- iguanafilter
- irvingplaza
- uploaded:by=flickrmobile
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8332678322_14912617f9_o.jpg?resize=607%2C452
---

[![Party's Over](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8332678322_14912617f9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/31/partys-over/) 
# [Party’s Over](http://dentedreality.com.au/2012/12/31/partys-over/)





* #[flickriosapp:filter=iguana](http://dentedreality.com.au/tags/flickriosappfilteriguana/)
* #[iguanafilter](http://dentedreality.com.au/tags/iguanafilter/)
* #[irvingplaza](http://dentedreality.com.au/tags/irvingplaza/)
* #[uploaded:by=flickrmobile](http://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8332678322/) [8:26 pm, December 31, 2012](http://dentedreality.com.au/2012/12/31/partys-over/ "8:26 pm") 
jQuery(document).ready(function(){
var gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb = {
positions : {
620 : new google.maps.LatLng( '40.73492', '-73.988297' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.positions ) {
gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.bounds.extend( gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.positions[m] );
}
// Render markers
for ( var m in gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.positions ) {
gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.map,
position : gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.map.setCenter( gmap\_m90a606b7ac87caaa4b3df85a3b4a66bb.positions[620] );
});
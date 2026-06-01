---
title: BAR
date: '2013-06-01T18:16:12+00:00'
format: image
service: flickr
tags:
- bar
- neon
- red
- sign
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439716228_0a5bd5c113_o.jpg?resize=607%2C813
---

[![BAR](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439716228_0a5bd5c113_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/01/bar/) 
# [BAR](http://dentedreality.com.au/2013/06/01/bar/)





* #[bar](http://dentedreality.com.au/tags/bar/)
* #[neon](http://dentedreality.com.au/tags/neon/)
* #[red](http://dentedreality.com.au/tags/red/)
* #[sign](http://dentedreality.com.au/tags/sign/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439716228/) [6:16 pm, June 1, 2013](http://dentedreality.com.au/2013/06/01/bar/ "6:16 pm") 
jQuery(document).ready(function(){
var gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b = {
positions : {
739 : new google.maps.LatLng( '40.659666', '-73.987667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.positions ) {
gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.bounds.extend( gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.positions[m] );
}
// Render markers
for ( var m in gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.positions ) {
gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.map,
position : gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.map.setCenter( gmap\_m1ca6144e7dc6b9f8c5339a8b612c7c3b.positions[739] );
});
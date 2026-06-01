---
title: Bangla Road
date: '2006-12-31T07:21:31+00:00'
format: image
service: flickr
tags:
- bangla
- banglaroad
- newyearseve2006
- nye2006
- people
- phuket
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349545666_3c14849934_o.jpg?resize=607%2C455
---

[![Bangla Road](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349545666_3c14849934_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/bangla-road/) 
# [Bangla Road](http://dentedreality.com.au/2006/12/31/bangla-road/)

The main party-street in Patong was totally packed with people going from bar to bar (and just drinking in the street)





* #[bangla](http://dentedreality.com.au/tags/bangla/)
* #[banglaroad](http://dentedreality.com.au/tags/banglaroad/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[people](http://dentedreality.com.au/tags/people/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349545666/) [7:21 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/bangla-road/ "7:21 am") 
jQuery(document).ready(function(){
var gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13 = {
positions : {
297 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.positions ) {
gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.bounds.extend( gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.positions[m] );
}
// Render markers
for ( var m in gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.positions ) {
gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.map,
position : gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.map.setCenter( gmap\_m7b8e7564a690a17eaaaf4dcb08f0db13.positions[297] );
});
---
title: Crackers On The Street
date: '2006-12-31T07:48:06+00:00'
format: image
service: flickr
tags:
- crackers
- firecrackers
- newyearseve2006
- nye2006
- phuket
- thailand
- thailand06
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349544964_94a2c406b9_o.jpg?resize=607%2C455
---

[![Crackers On The Street](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349544964_94a2c406b9_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/31/crackers-on-the-street/) 
# [Crackers On The Street](http://dentedreality.com.au/2006/12/31/crackers-on-the-street/)

People kept setting off rolls of 10,000 fire crackers in the middle of the street (and all the people passing). They were so loud that our ears were ringing by the time we made it to the end of the street.





* #[crackers](http://dentedreality.com.au/tags/crackers/)
* #[firecrackers](http://dentedreality.com.au/tags/firecrackers/)
* #[newyearseve2006](http://dentedreality.com.au/tags/newyearseve2006/)
* #[nye2006](http://dentedreality.com.au/tags/nye2006/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349544964/) [7:48 am, December 31, 2006](http://dentedreality.com.au/2006/12/31/crackers-on-the-street/ "7:48 am") 
jQuery(document).ready(function(){
var gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c = {
positions : {
333 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.positions ) {
gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.bounds.extend( gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.positions[m] );
}
// Render markers
for ( var m in gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.positions ) {
gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.map,
position : gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.map.setCenter( gmap\_m4c85e9e0d83d5b2bf1c2578a66e2946c.positions[333] );
});
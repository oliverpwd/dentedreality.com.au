---
title: Up They Go!
date: '2011-05-21T10:30:22+00:00'
format: image
service: flickr
tags:
- bridge
- meetup
- PDX
- Portland
- teamsocial
- willamette
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802736944_a2d41c415c_o.jpg?resize=607%2C452
---

[![Up They Go!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802736944_a2d41c415c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/21/up-they-go-2/) 
# [Up They Go!](http://dentedreality.com.au/2011/05/21/up-they-go-2/)

Bridges going up on the Willamette River to let a boat through





* #[bridge](http://dentedreality.com.au/tags/bridge/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[willamette](http://dentedreality.com.au/tags/willamette/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802736944/) [10:30 am, May 21, 2011](http://dentedreality.com.au/2011/05/21/up-they-go-2/ "10:30 am") 
jQuery(document).ready(function(){
var gmap\_m13e560477136b6bcd8c3c829f289f93e = {
positions : {
327 : new google.maps.LatLng( '45.523333', '-122.669834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m13e560477136b6bcd8c3c829f289f93e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m13e560477136b6bcd8c3c829f289f93e.positions ) {
gmap\_m13e560477136b6bcd8c3c829f289f93e.bounds.extend( gmap\_m13e560477136b6bcd8c3c829f289f93e.positions[m] );
}
// Render markers
for ( var m in gmap\_m13e560477136b6bcd8c3c829f289f93e.positions ) {
gmap\_m13e560477136b6bcd8c3c829f289f93e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m13e560477136b6bcd8c3c829f289f93e.map,
position : gmap\_m13e560477136b6bcd8c3c829f289f93e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m13e560477136b6bcd8c3c829f289f93e.map.setCenter( gmap\_m13e560477136b6bcd8c3c829f289f93e.positions[327] );
});
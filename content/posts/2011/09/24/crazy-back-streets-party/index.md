---
title: Crazy back-streets party
date: '2011-09-24T22:59:36+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- party
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812112418_f5a445dfa8_o.jpg?resize=607%2C813
---

[![Crazy back-streets party](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812112418_f5a445dfa8_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/24/crazy-back-streets-party/) 
# [Crazy back-streets party](http://dentedreality.com.au/2011/09/24/crazy-back-streets-party/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[party](http://dentedreality.com.au/tags/party/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812112418/) [10:59 pm, September 24, 2011](http://dentedreality.com.au/2011/09/24/crazy-back-streets-party/ "10:59 pm") 
jQuery(document).ready(function(){
var gmap\_m832fee8a9b1578eecb0af3f818f1a7a9 = {
positions : {
571 : new google.maps.LatLng( '38.7115', '-9.1435' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m832fee8a9b1578eecb0af3f818f1a7a9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.positions ) {
gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.bounds.extend( gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.positions[m] );
}
// Render markers
for ( var m in gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.positions ) {
gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.map,
position : gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.map.setCenter( gmap\_m832fee8a9b1578eecb0af3f818f1a7a9.positions[571] );
});
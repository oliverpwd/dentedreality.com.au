---
title: Not the Golden Gate Bridge
date: '2011-09-25T12:22:57+00:00'
format: image
service: flickr
tags:
- automattic
- birdge
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958223573_9afedd0a65_o.jpg?resize=607%2C452
---

[![Not the Golden Gate Bridge](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958223573_9afedd0a65_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/25/not-the-golden-gate-bridge/) 
# [Not the Golden Gate Bridge](http://dentedreality.com.au/2011/09/25/not-the-golden-gate-bridge/)

This is Lisbon’s version, designed by the same guy apparently.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[birdge](http://dentedreality.com.au/tags/birdge/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958223573/) [12:22 pm, September 25, 2011](http://dentedreality.com.au/2011/09/25/not-the-golden-gate-bridge/ "12:22 pm") 
jQuery(document).ready(function(){
var gmap\_m5c32d792b9bde70eafa8c3e92c270ef2 = {
positions : {
676 : new google.maps.LatLng( '38.692', '-9.178834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5c32d792b9bde70eafa8c3e92c270ef2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.positions ) {
gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.bounds.extend( gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.positions[m] );
}
// Render markers
for ( var m in gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.positions ) {
gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.map,
position : gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.map.setCenter( gmap\_m5c32d792b9bde70eafa8c3e92c270ef2.positions[676] );
});
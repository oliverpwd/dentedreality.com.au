---
title: On a Boat!
date: '2011-09-25T10:40:28+00:00'
format: image
service: flickr
tags:
- automattic
- boat
- Lisbon
- mast
- meetup
- portugal
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958223105_0bd1150881_o.jpg?resize=607%2C813
---

[![On a Boat!](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958223105_0bd1150881_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/25/on-a-boat/) 
# [On a Boat!](http://dentedreality.com.au/2011/09/25/on-a-boat/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[boat](http://dentedreality.com.au/tags/boat/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[mast](http://dentedreality.com.au/tags/mast/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958223105/) [10:40 am, September 25, 2011](http://dentedreality.com.au/2011/09/25/on-a-boat/ "10:40 am") 
jQuery(document).ready(function(){
var gmap\_mb56ef372c77119c4b2efb928cda82bc5 = {
positions : {
249 : new google.maps.LatLng( '38.702333', '-9.163' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb56ef372c77119c4b2efb928cda82bc5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb56ef372c77119c4b2efb928cda82bc5.positions ) {
gmap\_mb56ef372c77119c4b2efb928cda82bc5.bounds.extend( gmap\_mb56ef372c77119c4b2efb928cda82bc5.positions[m] );
}
// Render markers
for ( var m in gmap\_mb56ef372c77119c4b2efb928cda82bc5.positions ) {
gmap\_mb56ef372c77119c4b2efb928cda82bc5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb56ef372c77119c4b2efb928cda82bc5.map,
position : gmap\_mb56ef372c77119c4b2efb928cda82bc5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb56ef372c77119c4b2efb928cda82bc5.map.setCenter( gmap\_mb56ef372c77119c4b2efb928cda82bc5.positions[249] );
});
---
title: Team Social in Lisbon
date: '2011-09-23T07:02:45-06:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- view
latitude: '38.739333'
longitude: '-9.134667'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190316/6812110976_b08a5830b1_o.jpg
---

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190316/6812110976_b08a5830b1_o.jpg)](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-24/) 
# [Team Social in Lisbon](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-24/)

[![Team Social in Lisbon](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2011/09/14190316/6812110976_b08a5830b1_o.jpg)](http://www.flickr.com/photos/borkazoid/6812110976/)

38.739333-9.134667




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[Lisbon](https://dentedreality.com.au/tags/lisbon/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[portugal](https://dentedreality.com.au/tags/portugal/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)
* #[view](https://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812110976/) [7:02 am, September 23, 2011](https://dentedreality.com.au/2011/09/23/team-social-in-lisbon-24/ "7:02 am") 
jQuery(document).ready(function(){
var gmap\_m1c8c466a05841c5b80e43a41a7a4f05c = {
positions : {
386 : new google.maps.LatLng( '38.739333', '-9.134667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1c8c466a05841c5b80e43a41a7a4f05c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.positions ) {
gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.bounds.extend( gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.positions[m] );
}
// Render markers
for ( var m in gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.positions ) {
gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.map,
position : gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.map.setCenter( gmap\_m1c8c466a05841c5b80e43a41a7a4f05c.positions[386] );
});
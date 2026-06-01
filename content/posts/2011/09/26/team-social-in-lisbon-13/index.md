---
title: Team Social in Lisbon
date: '2011-09-26T12:51:11+00:00'
format: image
service: flickr
tags:
- automattic
- castle
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958224505_37bbdb25d9_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958224505_37bbdb25d9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-13/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-13/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[castle](http://dentedreality.com.au/tags/castle/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958224505/) [12:51 pm, September 26, 2011](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-13/ "12:51 pm") 
jQuery(document).ready(function(){
var gmap\_mdeedb03f347b1f29b34ee8edf110fd98 = {
positions : {
546 : new google.maps.LatLng( '38.7135', '-9.1335' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdeedb03f347b1f29b34ee8edf110fd98' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdeedb03f347b1f29b34ee8edf110fd98.positions ) {
gmap\_mdeedb03f347b1f29b34ee8edf110fd98.bounds.extend( gmap\_mdeedb03f347b1f29b34ee8edf110fd98.positions[m] );
}
// Render markers
for ( var m in gmap\_mdeedb03f347b1f29b34ee8edf110fd98.positions ) {
gmap\_mdeedb03f347b1f29b34ee8edf110fd98.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdeedb03f347b1f29b34ee8edf110fd98.map,
position : gmap\_mdeedb03f347b1f29b34ee8edf110fd98.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdeedb03f347b1f29b34ee8edf110fd98.map.setCenter( gmap\_mdeedb03f347b1f29b34ee8edf110fd98.positions[546] );
});
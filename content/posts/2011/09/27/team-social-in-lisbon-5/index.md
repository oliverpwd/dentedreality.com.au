---
title: Team Social in Lisbon
date: '2011-09-27T12:56:38+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- tomb
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958226889_0c3c98e737_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958226889_0c3c98e737_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-5/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-5/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[tomb](http://dentedreality.com.au/tags/tomb/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958226889/) [12:56 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-5/ "12:56 pm") 
jQuery(document).ready(function(){
var gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d = {
positions : {
783 : new google.maps.LatLng( '38.695833', '-9.205834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.positions ) {
gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.bounds.extend( gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.positions[m] );
}
// Render markers
for ( var m in gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.positions ) {
gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.map,
position : gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.map.setCenter( gmap\_m45fc125ad7b6fc11cc1703e1e6c0a98d.positions[783] );
});
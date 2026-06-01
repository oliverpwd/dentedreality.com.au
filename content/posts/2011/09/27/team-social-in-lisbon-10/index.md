---
title: Team Social in Lisbon
date: '2011-09-27T12:08:49+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958225209_85edf98118_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6958225209_85edf98118_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-10/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-10/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958225209/) [12:08 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-10/ "12:08 pm") 
jQuery(document).ready(function(){
var gmap\_m3bca3a28f661c18e190e8dc659c925d6 = {
positions : {
647 : new google.maps.LatLng( '38.720833', '-9.146334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3bca3a28f661c18e190e8dc659c925d6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3bca3a28f661c18e190e8dc659c925d6.positions ) {
gmap\_m3bca3a28f661c18e190e8dc659c925d6.bounds.extend( gmap\_m3bca3a28f661c18e190e8dc659c925d6.positions[m] );
}
// Render markers
for ( var m in gmap\_m3bca3a28f661c18e190e8dc659c925d6.positions ) {
gmap\_m3bca3a28f661c18e190e8dc659c925d6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3bca3a28f661c18e190e8dc659c925d6.map,
position : gmap\_m3bca3a28f661c18e190e8dc659c925d6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3bca3a28f661c18e190e8dc659c925d6.map.setCenter( gmap\_m3bca3a28f661c18e190e8dc659c925d6.positions[647] );
});
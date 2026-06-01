---
title: Team Social in Lisbon
date: '2011-09-27T10:25:26+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115004_7091a7e33b_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115004_7091a7e33b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-11/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-11/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812115004/) [10:25 am, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-11/ "10:25 am") 
jQuery(document).ready(function(){
var gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee = {
positions : {
546 : new google.maps.LatLng( '38.712333', '-9.139334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.positions ) {
gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.bounds.extend( gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.positions[m] );
}
// Render markers
for ( var m in gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.positions ) {
gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.map,
position : gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.map.setCenter( gmap\_m3f1d14b8ab69b4dc4e0fac716633b1ee.positions[546] );
});
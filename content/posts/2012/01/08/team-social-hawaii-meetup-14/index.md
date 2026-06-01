---
title: Team Social Hawaii Meetup
date: '2012-01-08T11:48:08+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539679_efabdb1d69_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539679_efabdb1d69_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-14/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-14/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959539679/) [11:48 am, January 8, 2012](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-14/ "11:48 am") 
jQuery(document).ready(function(){
var gmap\_m105a086072930fd529bfb8199f41569e = {
positions : {
919 : new google.maps.LatLng( '21.410833', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m105a086072930fd529bfb8199f41569e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m105a086072930fd529bfb8199f41569e.positions ) {
gmap\_m105a086072930fd529bfb8199f41569e.bounds.extend( gmap\_m105a086072930fd529bfb8199f41569e.positions[m] );
}
// Render markers
for ( var m in gmap\_m105a086072930fd529bfb8199f41569e.positions ) {
gmap\_m105a086072930fd529bfb8199f41569e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m105a086072930fd529bfb8199f41569e.map,
position : gmap\_m105a086072930fd529bfb8199f41569e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m105a086072930fd529bfb8199f41569e.map.setCenter( gmap\_m105a086072930fd529bfb8199f41569e.positions[919] );
});
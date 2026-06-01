---
title: Team Social Hawaii Meetup
date: '2012-01-08T18:30:28+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539875_fbda5399e5_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539875_fbda5399e5_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-13/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-13/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959539875/) [6:30 pm, January 8, 2012](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-13/ "6:30 pm") 
jQuery(document).ready(function(){
var gmap\_m8dd06a858540f75225c3993db493fc1a = {
positions : {
404 : new google.maps.LatLng( '21.410833', '-157.7425' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8dd06a858540f75225c3993db493fc1a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8dd06a858540f75225c3993db493fc1a.positions ) {
gmap\_m8dd06a858540f75225c3993db493fc1a.bounds.extend( gmap\_m8dd06a858540f75225c3993db493fc1a.positions[m] );
}
// Render markers
for ( var m in gmap\_m8dd06a858540f75225c3993db493fc1a.positions ) {
gmap\_m8dd06a858540f75225c3993db493fc1a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8dd06a858540f75225c3993db493fc1a.map,
position : gmap\_m8dd06a858540f75225c3993db493fc1a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8dd06a858540f75225c3993db493fc1a.map.setCenter( gmap\_m8dd06a858540f75225c3993db493fc1a.positions[404] );
});
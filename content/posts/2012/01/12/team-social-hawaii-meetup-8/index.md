---
title: Team Social Hawaii Meetup
date: '2012-01-12T05:55:03+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959541575_98dcd07685_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959541575_98dcd07685_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-8/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-8/)

Hugo’s awesome pixel-art logo. Made from post-its.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959541575/) [5:55 am, January 12, 2012](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-8/ "5:55 am") 
jQuery(document).ready(function(){
var gmap\_m67191519f5d8134d0c8a2dd224be1c04 = {
positions : {
220 : new google.maps.LatLng( '21.410833', '-157.742167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m67191519f5d8134d0c8a2dd224be1c04' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m67191519f5d8134d0c8a2dd224be1c04.positions ) {
gmap\_m67191519f5d8134d0c8a2dd224be1c04.bounds.extend( gmap\_m67191519f5d8134d0c8a2dd224be1c04.positions[m] );
}
// Render markers
for ( var m in gmap\_m67191519f5d8134d0c8a2dd224be1c04.positions ) {
gmap\_m67191519f5d8134d0c8a2dd224be1c04.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m67191519f5d8134d0c8a2dd224be1c04.map,
position : gmap\_m67191519f5d8134d0c8a2dd224be1c04.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m67191519f5d8134d0c8a2dd224be1c04.map.setCenter( gmap\_m67191519f5d8134d0c8a2dd224be1c04.positions[220] );
});
---
title: Team Social Hawaii Meetup
date: '2012-01-11T10:38:42+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428286_c5838b3bf4_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428286_c5838b3bf4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-10/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-10/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813428286/) [10:38 am, January 11, 2012](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-10/ "10:38 am") 
jQuery(document).ready(function(){
var gmap\_m5c7cc381e6d03e828906fa0f1fcf5809 = {
positions : {
159 : new google.maps.LatLng( '21.316', '-157.663334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5c7cc381e6d03e828906fa0f1fcf5809' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.positions ) {
gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.bounds.extend( gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.positions[m] );
}
// Render markers
for ( var m in gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.positions ) {
gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.map,
position : gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.map.setCenter( gmap\_m5c7cc381e6d03e828906fa0f1fcf5809.positions[159] );
});
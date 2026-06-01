---
title: Team Social Hawaii Meetup
date: '2012-01-11T16:28:15+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428496_ee5ae5c99d_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813428496_ee5ae5c99d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-9/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-9/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813428496/) [4:28 pm, January 11, 2012](http://dentedreality.com.au/2012/01/11/team-social-hawaii-meetup-9/ "4:28 pm") 
jQuery(document).ready(function(){
var gmap\_mca574b8035758c25ba73b98c1b8f01bc = {
positions : {
200 : new google.maps.LatLng( '21.410833', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mca574b8035758c25ba73b98c1b8f01bc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mca574b8035758c25ba73b98c1b8f01bc.positions ) {
gmap\_mca574b8035758c25ba73b98c1b8f01bc.bounds.extend( gmap\_mca574b8035758c25ba73b98c1b8f01bc.positions[m] );
}
// Render markers
for ( var m in gmap\_mca574b8035758c25ba73b98c1b8f01bc.positions ) {
gmap\_mca574b8035758c25ba73b98c1b8f01bc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mca574b8035758c25ba73b98c1b8f01bc.map,
position : gmap\_mca574b8035758c25ba73b98c1b8f01bc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mca574b8035758c25ba73b98c1b8f01bc.map.setCenter( gmap\_mca574b8035758c25ba73b98c1b8f01bc.positions[200] );
});
---
title: Team Social Hawaii Meetup
date: '2012-01-12T08:34:30+00:00'
format: image
service: flickr
tags:
- automattic
- beau
- beaulebens
- hawaii
- kailua
- me
- meetup
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813430286_74d6c2ec9b_o.jpg?resize=607%2C813
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813430286_74d6c2ec9b_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-5/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-5/)

I’m on a bike. Don’t try this at home.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813430286/) [8:34 am, January 12, 2012](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-5/ "8:34 am") 
jQuery(document).ready(function(){
var gmap\_m5996ad434728465c50acbed05a4c961d = {
positions : {
701 : new google.maps.LatLng( '21.404', '-157.743334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5996ad434728465c50acbed05a4c961d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5996ad434728465c50acbed05a4c961d.positions ) {
gmap\_m5996ad434728465c50acbed05a4c961d.bounds.extend( gmap\_m5996ad434728465c50acbed05a4c961d.positions[m] );
}
// Render markers
for ( var m in gmap\_m5996ad434728465c50acbed05a4c961d.positions ) {
gmap\_m5996ad434728465c50acbed05a4c961d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5996ad434728465c50acbed05a4c961d.map,
position : gmap\_m5996ad434728465c50acbed05a4c961d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5996ad434728465c50acbed05a4c961d.map.setCenter( gmap\_m5996ad434728465c50acbed05a4c961d.positions[701] );
});
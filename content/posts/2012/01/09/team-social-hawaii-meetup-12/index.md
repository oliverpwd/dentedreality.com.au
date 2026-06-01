---
title: Team Social Hawaii Meetup
date: '2012-01-09T10:05:05+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813427582_dd793927de_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813427582_dd793927de_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/09/team-social-hawaii-meetup-12/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/09/team-social-hawaii-meetup-12/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813427582/) [10:05 am, January 9, 2012](http://dentedreality.com.au/2012/01/09/team-social-hawaii-meetup-12/ "10:05 am") 
jQuery(document).ready(function(){
var gmap\_md960b6e6f184d8eace52e01c96be2297 = {
positions : {
302 : new google.maps.LatLng( '21.396333', '-157.723834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md960b6e6f184d8eace52e01c96be2297' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md960b6e6f184d8eace52e01c96be2297.positions ) {
gmap\_md960b6e6f184d8eace52e01c96be2297.bounds.extend( gmap\_md960b6e6f184d8eace52e01c96be2297.positions[m] );
}
// Render markers
for ( var m in gmap\_md960b6e6f184d8eace52e01c96be2297.positions ) {
gmap\_md960b6e6f184d8eace52e01c96be2297.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md960b6e6f184d8eace52e01c96be2297.map,
position : gmap\_md960b6e6f184d8eace52e01c96be2297.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md960b6e6f184d8eace52e01c96be2297.map.setCenter( gmap\_md960b6e6f184d8eace52e01c96be2297.positions[302] );
});
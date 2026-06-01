---
title: Team Social Hawaii Meetup
date: '2012-01-12T07:45:39+00:00'
format: image
service: flickr
tags:
- automattic
- hawaii
- kailua
- meetup
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959542639_24007bf850_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959542639_24007bf850_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-6/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-6/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959542639/) [7:45 am, January 12, 2012](http://dentedreality.com.au/2012/01/12/team-social-hawaii-meetup-6/ "7:45 am") 
jQuery(document).ready(function(){
var gmap\_m190be4a7ccb5677784c4fe2084831630 = {
positions : {
270 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m190be4a7ccb5677784c4fe2084831630' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m190be4a7ccb5677784c4fe2084831630.positions ) {
gmap\_m190be4a7ccb5677784c4fe2084831630.bounds.extend( gmap\_m190be4a7ccb5677784c4fe2084831630.positions[m] );
}
// Render markers
for ( var m in gmap\_m190be4a7ccb5677784c4fe2084831630.positions ) {
gmap\_m190be4a7ccb5677784c4fe2084831630.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m190be4a7ccb5677784c4fe2084831630.map,
position : gmap\_m190be4a7ccb5677784c4fe2084831630.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m190be4a7ccb5677784c4fe2084831630.map.setCenter( gmap\_m190be4a7ccb5677784c4fe2084831630.positions[270] );
});
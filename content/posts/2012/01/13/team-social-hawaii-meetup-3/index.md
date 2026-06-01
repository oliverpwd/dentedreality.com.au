---
title: Team Social Hawaii Meetup
date: '2012-01-13T04:36:47+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- sky
- sunrise
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813430966_8e70c43dfa_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6813430966_8e70c43dfa_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-3/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-3/)

Sun"rise"





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sunrise](http://dentedreality.com.au/tags/sunrise/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6813430966/) [4:36 am, January 13, 2012](http://dentedreality.com.au/2012/01/13/team-social-hawaii-meetup-3/ "4:36 am") 
jQuery(document).ready(function(){
var gmap\_ma01e4f2aac4c61254e73bd2052e08c62 = {
positions : {
232 : new google.maps.LatLng( '21.410999', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma01e4f2aac4c61254e73bd2052e08c62' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma01e4f2aac4c61254e73bd2052e08c62.positions ) {
gmap\_ma01e4f2aac4c61254e73bd2052e08c62.bounds.extend( gmap\_ma01e4f2aac4c61254e73bd2052e08c62.positions[m] );
}
// Render markers
for ( var m in gmap\_ma01e4f2aac4c61254e73bd2052e08c62.positions ) {
gmap\_ma01e4f2aac4c61254e73bd2052e08c62.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma01e4f2aac4c61254e73bd2052e08c62.map,
position : gmap\_ma01e4f2aac4c61254e73bd2052e08c62.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma01e4f2aac4c61254e73bd2052e08c62.map.setCenter( gmap\_ma01e4f2aac4c61254e73bd2052e08c62.positions[232] );
});
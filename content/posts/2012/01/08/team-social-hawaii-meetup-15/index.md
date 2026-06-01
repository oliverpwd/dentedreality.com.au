---
title: Team Social Hawaii Meetup
date: '2012-01-08T11:47:05+00:00'
format: image
service: flickr
tags:
- automattic
- beach
- hawaii
- kailua
- meetup
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539477_6fa414ba67_o.jpg?resize=607%2C452
---

[![Team Social Hawaii Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/01/6959539477_6fa414ba67_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-15/) 
# [Team Social Hawaii Meetup](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-15/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[hawaii](http://dentedreality.com.au/tags/hawaii/)
* #[kailua](http://dentedreality.com.au/tags/kailua/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6959539477/) [11:47 am, January 8, 2012](http://dentedreality.com.au/2012/01/08/team-social-hawaii-meetup-15/ "11:47 am") 
jQuery(document).ready(function(){
var gmap\_m6fdb208700572d5ec686d08209d99d7a = {
positions : {
373 : new google.maps.LatLng( '21.410833', '-157.742334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6fdb208700572d5ec686d08209d99d7a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6fdb208700572d5ec686d08209d99d7a.positions ) {
gmap\_m6fdb208700572d5ec686d08209d99d7a.bounds.extend( gmap\_m6fdb208700572d5ec686d08209d99d7a.positions[m] );
}
// Render markers
for ( var m in gmap\_m6fdb208700572d5ec686d08209d99d7a.positions ) {
gmap\_m6fdb208700572d5ec686d08209d99d7a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6fdb208700572d5ec686d08209d99d7a.map,
position : gmap\_m6fdb208700572d5ec686d08209d99d7a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6fdb208700572d5ec686d08209d99d7a.map.setCenter( gmap\_m6fdb208700572d5ec686d08209d99d7a.positions[373] );
});
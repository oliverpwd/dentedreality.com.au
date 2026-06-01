---
title: Team Social in Lisbon
date: '2011-09-27T12:54:54+00:00'
format: image
service: flickr
tags:
- automattic
- church
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812116614_4669425f1c_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812116614_4669425f1c_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-6/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-6/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[church](http://dentedreality.com.au/tags/church/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812116614/) [12:54 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-6/ "12:54 pm") 
jQuery(document).ready(function(){
var gmap\_m6471999499ff88c59c9131999a86b878 = {
positions : {
947 : new google.maps.LatLng( '38.695833', '-9.205834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6471999499ff88c59c9131999a86b878' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6471999499ff88c59c9131999a86b878.positions ) {
gmap\_m6471999499ff88c59c9131999a86b878.bounds.extend( gmap\_m6471999499ff88c59c9131999a86b878.positions[m] );
}
// Render markers
for ( var m in gmap\_m6471999499ff88c59c9131999a86b878.positions ) {
gmap\_m6471999499ff88c59c9131999a86b878.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6471999499ff88c59c9131999a86b878.map,
position : gmap\_m6471999499ff88c59c9131999a86b878.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6471999499ff88c59c9131999a86b878.map.setCenter( gmap\_m6471999499ff88c59c9131999a86b878.positions[947] );
});
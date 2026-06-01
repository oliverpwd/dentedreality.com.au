---
title: Team Social in Lisbon
date: '2011-09-27T16:53:39+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117226_b5772ea597_o.jpg?resize=607%2C813
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117226_b5772ea597_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-4/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-4/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812117226/) [4:53 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-4/ "4:53 pm") 
jQuery(document).ready(function(){
var gmap\_mc5177029cc6454cf8f888527986fca83 = {
positions : {
41 : new google.maps.LatLng( '38.707166', '-9.178667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc5177029cc6454cf8f888527986fca83' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc5177029cc6454cf8f888527986fca83.positions ) {
gmap\_mc5177029cc6454cf8f888527986fca83.bounds.extend( gmap\_mc5177029cc6454cf8f888527986fca83.positions[m] );
}
// Render markers
for ( var m in gmap\_mc5177029cc6454cf8f888527986fca83.positions ) {
gmap\_mc5177029cc6454cf8f888527986fca83.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc5177029cc6454cf8f888527986fca83.map,
position : gmap\_mc5177029cc6454cf8f888527986fca83.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc5177029cc6454cf8f888527986fca83.map.setCenter( gmap\_mc5177029cc6454cf8f888527986fca83.positions[41] );
});
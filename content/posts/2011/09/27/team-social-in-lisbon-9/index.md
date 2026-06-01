---
title: Team Social in Lisbon
date: '2011-09-27T12:22:27+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115610_9d34b692a9_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812115610_9d34b692a9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-9/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-9/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812115610/) [12:22 pm, September 27, 2011](http://dentedreality.com.au/2011/09/27/team-social-in-lisbon-9/ "12:22 pm") 
jQuery(document).ready(function(){
var gmap\_m138b81b5116477824265b16e20455926 = {
positions : {
956 : new google.maps.LatLng( '38.708', '-9.137' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m138b81b5116477824265b16e20455926' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m138b81b5116477824265b16e20455926.positions ) {
gmap\_m138b81b5116477824265b16e20455926.bounds.extend( gmap\_m138b81b5116477824265b16e20455926.positions[m] );
}
// Render markers
for ( var m in gmap\_m138b81b5116477824265b16e20455926.positions ) {
gmap\_m138b81b5116477824265b16e20455926.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m138b81b5116477824265b16e20455926.map,
position : gmap\_m138b81b5116477824265b16e20455926.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m138b81b5116477824265b16e20455926.map.setCenter( gmap\_m138b81b5116477824265b16e20455926.positions[956] );
});
---
title: Team Social in Lisbon
date: '2011-09-28T18:22:44+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117624_50d74bea31_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812117624_50d74bea31_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon-2/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon-2/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812117624/) [6:22 pm, September 28, 2011](http://dentedreality.com.au/2011/09/28/team-social-in-lisbon-2/ "6:22 pm") 
jQuery(document).ready(function(){
var gmap\_md1e24aae06e78c245a6f9000fb88c8ec = {
positions : {
402 : new google.maps.LatLng( '38.7175', '-9.153167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md1e24aae06e78c245a6f9000fb88c8ec' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md1e24aae06e78c245a6f9000fb88c8ec.positions ) {
gmap\_md1e24aae06e78c245a6f9000fb88c8ec.bounds.extend( gmap\_md1e24aae06e78c245a6f9000fb88c8ec.positions[m] );
}
// Render markers
for ( var m in gmap\_md1e24aae06e78c245a6f9000fb88c8ec.positions ) {
gmap\_md1e24aae06e78c245a6f9000fb88c8ec.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md1e24aae06e78c245a6f9000fb88c8ec.map,
position : gmap\_md1e24aae06e78c245a6f9000fb88c8ec.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md1e24aae06e78c245a6f9000fb88c8ec.map.setCenter( gmap\_md1e24aae06e78c245a6f9000fb88c8ec.positions[402] );
});
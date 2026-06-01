---
title: Team Social in Lisbon
date: '2011-09-26T12:37:33+00:00'
format: image
service: flickr
tags:
- automattic
- cannon
- Lisbon
- meetup
- portugal
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812114018_e2bf266827_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812114018_e2bf266827_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-15/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-15/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[cannon](http://dentedreality.com.au/tags/cannon/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812114018/) [12:37 pm, September 26, 2011](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-15/ "12:37 pm") 
jQuery(document).ready(function(){
var gmap\_m1d1732bff815bd9d79e2f710876c25c7 = {
positions : {
544 : new google.maps.LatLng( '38.711833', '-9.133334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1d1732bff815bd9d79e2f710876c25c7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1d1732bff815bd9d79e2f710876c25c7.positions ) {
gmap\_m1d1732bff815bd9d79e2f710876c25c7.bounds.extend( gmap\_m1d1732bff815bd9d79e2f710876c25c7.positions[m] );
}
// Render markers
for ( var m in gmap\_m1d1732bff815bd9d79e2f710876c25c7.positions ) {
gmap\_m1d1732bff815bd9d79e2f710876c25c7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1d1732bff815bd9d79e2f710876c25c7.map,
position : gmap\_m1d1732bff815bd9d79e2f710876c25c7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1d1732bff815bd9d79e2f710876c25c7.map.setCenter( gmap\_m1d1732bff815bd9d79e2f710876c25c7.positions[544] );
});
---
title: Team Social in Lisbon
date: '2011-09-26T12:40:40+00:00'
format: image
service: flickr
tags:
- automattic
- Lisbon
- meetup
- portugal
- teamsocial
- view
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812114308_f0ba6ba22d_o.jpg?resize=607%2C452
---

[![Team Social in Lisbon](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812114308_f0ba6ba22d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-14/) 
# [Team Social in Lisbon](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-14/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812114308/) [12:40 pm, September 26, 2011](http://dentedreality.com.au/2011/09/26/team-social-in-lisbon-14/ "12:40 pm") 
jQuery(document).ready(function(){
var gmap\_mcfa5c077404bd1f5ef5006662d300432 = {
positions : {
396 : new google.maps.LatLng( '38.712666', '-9.138834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mcfa5c077404bd1f5ef5006662d300432' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mcfa5c077404bd1f5ef5006662d300432.positions ) {
gmap\_mcfa5c077404bd1f5ef5006662d300432.bounds.extend( gmap\_mcfa5c077404bd1f5ef5006662d300432.positions[m] );
}
// Render markers
for ( var m in gmap\_mcfa5c077404bd1f5ef5006662d300432.positions ) {
gmap\_mcfa5c077404bd1f5ef5006662d300432.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mcfa5c077404bd1f5ef5006662d300432.map,
position : gmap\_mcfa5c077404bd1f5ef5006662d300432.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mcfa5c077404bd1f5ef5006662d300432.map.setCenter( gmap\_mcfa5c077404bd1f5ef5006662d300432.positions[396] );
});
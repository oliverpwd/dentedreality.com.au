---
title: Grand Meetup 2013
date: '2013-09-27T05:01:29+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076900946_4004f4d42b_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076900946_4004f4d42b_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-5/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-5/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076900946/) [5:01 am, September 27, 2013](http://dentedreality.com.au/2013/09/27/grand-meetup-2013-5/ "5:01 am") 
jQuery(document).ready(function(){
var gmap\_m94a56ac98282d51e2951f9ac3564a837 = {
positions : {
7 : new google.maps.LatLng( '37.784333', '-122.397501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m94a56ac98282d51e2951f9ac3564a837' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m94a56ac98282d51e2951f9ac3564a837.positions ) {
gmap\_m94a56ac98282d51e2951f9ac3564a837.bounds.extend( gmap\_m94a56ac98282d51e2951f9ac3564a837.positions[m] );
}
// Render markers
for ( var m in gmap\_m94a56ac98282d51e2951f9ac3564a837.positions ) {
gmap\_m94a56ac98282d51e2951f9ac3564a837.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m94a56ac98282d51e2951f9ac3564a837.map,
position : gmap\_m94a56ac98282d51e2951f9ac3564a837.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m94a56ac98282d51e2951f9ac3564a837.map.setCenter( gmap\_m94a56ac98282d51e2951f9ac3564a837.positions[7] );
});
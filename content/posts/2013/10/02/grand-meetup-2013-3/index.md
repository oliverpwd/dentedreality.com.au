---
title: Grand Meetup 2013
date: '2013-10-02T15:20:18+00:00'
format: image
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
- vision:night=079
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/10076902126_73bca1fd31_o.jpg?fit=1500%2C1500
---

[![Grand Meetup 2013](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/10076902126_73bca1fd31_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/02/grand-meetup-2013-3/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/10/02/grand-meetup-2013-3/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[vision:night=079](http://dentedreality.com.au/tags/visionnight079/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076902126/) [3:20 pm, October 2, 2013](http://dentedreality.com.au/2013/10/02/grand-meetup-2013-3/ "3:20 pm") 
jQuery(document).ready(function(){
var gmap\_m1738ed672064594d4b34ac459d29809a = {
positions : {
635 : new google.maps.LatLng( '36.961666', '-122.024667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m1738ed672064594d4b34ac459d29809a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m1738ed672064594d4b34ac459d29809a.positions ) {
gmap\_m1738ed672064594d4b34ac459d29809a.bounds.extend( gmap\_m1738ed672064594d4b34ac459d29809a.positions[m] );
}
// Render markers
for ( var m in gmap\_m1738ed672064594d4b34ac459d29809a.positions ) {
gmap\_m1738ed672064594d4b34ac459d29809a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m1738ed672064594d4b34ac459d29809a.map,
position : gmap\_m1738ed672064594d4b34ac459d29809a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m1738ed672064594d4b34ac459d29809a.map.setCenter( gmap\_m1738ed672064594d4b34ac459d29809a.positions[635] );
});
---
title: Grand Meetup 2013
date: '2013-09-25T08:54:47+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076822064_7a86d29256_o.jpg?resize=607%2C453
---

[![Grand Meetup 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076822064_7a86d29256_o.jpg?resize=607%2C453)](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-10/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-10/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076822064/) [8:54 am, September 25, 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-10/ "8:54 am") 
jQuery(document).ready(function(){
var gmap\_m60deb05d3f05cf0edbbe8024b83ef955 = {
positions : {
832 : new google.maps.LatLng( '38.154833', '-122.452334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m60deb05d3f05cf0edbbe8024b83ef955' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m60deb05d3f05cf0edbbe8024b83ef955.positions ) {
gmap\_m60deb05d3f05cf0edbbe8024b83ef955.bounds.extend( gmap\_m60deb05d3f05cf0edbbe8024b83ef955.positions[m] );
}
// Render markers
for ( var m in gmap\_m60deb05d3f05cf0edbbe8024b83ef955.positions ) {
gmap\_m60deb05d3f05cf0edbbe8024b83ef955.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m60deb05d3f05cf0edbbe8024b83ef955.map,
position : gmap\_m60deb05d3f05cf0edbbe8024b83ef955.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m60deb05d3f05cf0edbbe8024b83ef955.map.setCenter( gmap\_m60deb05d3f05cf0edbbe8024b83ef955.positions[832] );
});
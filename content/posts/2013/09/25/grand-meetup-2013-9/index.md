---
title: Grand Meetup 2013
date: '2013-09-25T15:30:06+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076860075_075eca71e9_o.jpg?resize=607%2C812
---

[![Grand Meetup 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076860075_075eca71e9_o.jpg?resize=607%2C812)](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-9/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-9/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076860075/) [3:30 pm, September 25, 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-9/ "3:30 pm") 
jQuery(document).ready(function(){
var gmap\_m7482175feb13d034d71640087c32f7bd = {
positions : {
951 : new google.maps.LatLng( '38.062166', '-122.5315' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7482175feb13d034d71640087c32f7bd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7482175feb13d034d71640087c32f7bd.positions ) {
gmap\_m7482175feb13d034d71640087c32f7bd.bounds.extend( gmap\_m7482175feb13d034d71640087c32f7bd.positions[m] );
}
// Render markers
for ( var m in gmap\_m7482175feb13d034d71640087c32f7bd.positions ) {
gmap\_m7482175feb13d034d71640087c32f7bd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7482175feb13d034d71640087c32f7bd.map,
position : gmap\_m7482175feb13d034d71640087c32f7bd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7482175feb13d034d71640087c32f7bd.map.setCenter( gmap\_m7482175feb13d034d71640087c32f7bd.positions[951] );
});
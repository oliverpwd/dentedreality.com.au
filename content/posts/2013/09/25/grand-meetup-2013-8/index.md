---
title: Grand Meetup 2013
date: '2013-09-25T16:13:00+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- grandmeetup2013
- meetup
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076898536_a77c44f9d5_o.jpg?resize=607%2C453
---

[![Grand Meetup 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/09/10076898536_a77c44f9d5_o.jpg?resize=607%2C453)](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-8/) 
# [Grand Meetup 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-8/)

Automattic’s annual full-company, week-long hackapalooza.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[grandmeetup2013](http://dentedreality.com.au/tags/grandmeetup2013/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/10076898536/) [4:13 pm, September 25, 2013](http://dentedreality.com.au/2013/09/25/grand-meetup-2013-8/ "4:13 pm") 
jQuery(document).ready(function(){
var gmap\_m5a50922a6b1a83477d3d740b9eeaf08d = {
positions : {
820 : new google.maps.LatLng( '38.062166', '-122.531667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5a50922a6b1a83477d3d740b9eeaf08d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.positions ) {
gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.bounds.extend( gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.positions[m] );
}
// Render markers
for ( var m in gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.positions ) {
gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.map,
position : gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.map.setCenter( gmap\_m5a50922a6b1a83477d3d740b9eeaf08d.positions[820] );
});
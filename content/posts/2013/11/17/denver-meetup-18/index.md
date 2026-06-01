---
title: Denver Meetup
date: '2013-11-17T12:33:23+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0634
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291125695_16cb5856dc_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291125695_16cb5856dc_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/17/denver-meetup-18/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-18/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0634](http://dentedreality.com.au/tags/visionoutdoor0634/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291125695/) [12:33 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-18/ "12:33 pm") 
jQuery(document).ready(function(){
var gmap\_mc8947d600af9ad90c864d575a7e761f6 = {
positions : {
918 : new google.maps.LatLng( '39.712677', '-104.999389' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc8947d600af9ad90c864d575a7e761f6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc8947d600af9ad90c864d575a7e761f6.positions ) {
gmap\_mc8947d600af9ad90c864d575a7e761f6.bounds.extend( gmap\_mc8947d600af9ad90c864d575a7e761f6.positions[m] );
}
// Render markers
for ( var m in gmap\_mc8947d600af9ad90c864d575a7e761f6.positions ) {
gmap\_mc8947d600af9ad90c864d575a7e761f6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc8947d600af9ad90c864d575a7e761f6.map,
position : gmap\_mc8947d600af9ad90c864d575a7e761f6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc8947d600af9ad90c864d575a7e761f6.map.setCenter( gmap\_mc8947d600af9ad90c864d575a7e761f6.positions[918] );
});
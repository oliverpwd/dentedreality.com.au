---
title: Wilderness Skills Clinic
date: '2011-12-11T07:56:49+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- rose
- survival
- wilderness
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215010_c838e16b3f_o.jpg?resize=607%2C452
---

[![Wilderness Skills Clinic](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6812215010_c838e16b3f_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-7/) 
# [Wilderness Skills Clinic](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-7/)





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[rose](http://dentedreality.com.au/tags/rose/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812215010/) [7:56 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-7/ "7:56 am") 
jQuery(document).ready(function(){
var gmap\_mfaeb64a703b74d4848bf14e930756226 = {
positions : {
672 : new google.maps.LatLng( '38.000833', '-122.611334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfaeb64a703b74d4848bf14e930756226' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfaeb64a703b74d4848bf14e930756226.positions ) {
gmap\_mfaeb64a703b74d4848bf14e930756226.bounds.extend( gmap\_mfaeb64a703b74d4848bf14e930756226.positions[m] );
}
// Render markers
for ( var m in gmap\_mfaeb64a703b74d4848bf14e930756226.positions ) {
gmap\_mfaeb64a703b74d4848bf14e930756226.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfaeb64a703b74d4848bf14e930756226.map,
position : gmap\_mfaeb64a703b74d4848bf14e930756226.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfaeb64a703b74d4848bf14e930756226.map.setCenter( gmap\_mfaeb64a703b74d4848bf14e930756226.positions[672] );
});
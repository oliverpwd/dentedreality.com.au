---
title: Wilderness Skills Clinic
date: '2011-12-11T07:58:59+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- camping
- disaster
- me
- outdoors
- survival
- wilderness
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958324627_326939726c_o.jpg?resize=607%2C452
---

[![Wilderness Skills Clinic](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958324627_326939726c_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-5/) 
# [Wilderness Skills Clinic](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-5/)

I’m in a debris hut





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958324627/) [7:58 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-5/ "7:58 am") 
jQuery(document).ready(function(){
var gmap\_mc84190a94c23ebedc25717cd251d7493 = {
positions : {
867 : new google.maps.LatLng( '38.000666', '-122.611334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc84190a94c23ebedc25717cd251d7493' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc84190a94c23ebedc25717cd251d7493.positions ) {
gmap\_mc84190a94c23ebedc25717cd251d7493.bounds.extend( gmap\_mc84190a94c23ebedc25717cd251d7493.positions[m] );
}
// Render markers
for ( var m in gmap\_mc84190a94c23ebedc25717cd251d7493.positions ) {
gmap\_mc84190a94c23ebedc25717cd251d7493.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc84190a94c23ebedc25717cd251d7493.map,
position : gmap\_mc84190a94c23ebedc25717cd251d7493.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc84190a94c23ebedc25717cd251d7493.map.setCenter( gmap\_mc84190a94c23ebedc25717cd251d7493.positions[867] );
});
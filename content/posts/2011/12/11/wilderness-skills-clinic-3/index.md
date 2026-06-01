---
title: Wilderness Skills Clinic
date: '2011-12-11T08:59:29+00:00'
format: image
service: flickr
tags:
- camping
- disaster
- outdoors
- survival
- wilderness
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958325437_0e34e7dc48_o.jpg?resize=607%2C452
---

[![Wilderness Skills Clinic](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/12/6958325437_0e34e7dc48_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-3/) 
# [Wilderness Skills Clinic](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-3/)





* #[camping](http://dentedreality.com.au/tags/camping/)
* #[disaster](http://dentedreality.com.au/tags/disaster/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[survival](http://dentedreality.com.au/tags/survival/)
* #[wilderness](http://dentedreality.com.au/tags/wilderness/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958325437/) [8:59 am, December 11, 2011](http://dentedreality.com.au/2011/12/11/wilderness-skills-clinic-3/ "8:59 am") 
jQuery(document).ready(function(){
var gmap\_m9b72be058565799263cc4299ccb95d73 = {
positions : {
909 : new google.maps.LatLng( '38', '-122.612834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9b72be058565799263cc4299ccb95d73' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9b72be058565799263cc4299ccb95d73.positions ) {
gmap\_m9b72be058565799263cc4299ccb95d73.bounds.extend( gmap\_m9b72be058565799263cc4299ccb95d73.positions[m] );
}
// Render markers
for ( var m in gmap\_m9b72be058565799263cc4299ccb95d73.positions ) {
gmap\_m9b72be058565799263cc4299ccb95d73.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9b72be058565799263cc4299ccb95d73.map,
position : gmap\_m9b72be058565799263cc4299ccb95d73.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9b72be058565799263cc4299ccb95d73.map.setCenter( gmap\_m9b72be058565799263cc4299ccb95d73.positions[909] );
});
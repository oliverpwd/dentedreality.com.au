---
title: Australia Day
date: '2011-01-26T13:59:17+00:00'
format: image
service: flickr
tags:
- australia
- australiaday
- australiaday2011
- sydney
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193003_f7094e5dab_o.jpg?resize=607%2C813
---

[![Australia Day](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434193003_f7094e5dab_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/01/26/australia-day-6/) 
# [Australia Day](http://dentedreality.com.au/2011/01/26/australia-day-6/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[australiaday](http://dentedreality.com.au/tags/australiaday/)
* #[australiaday2011](http://dentedreality.com.au/tags/australiaday2011/)
* #[sydney](http://dentedreality.com.au/tags/sydney/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434193003/) [1:59 pm, January 26, 2011](http://dentedreality.com.au/2011/01/26/australia-day-6/ "1:59 pm") 
jQuery(document).ready(function(){
var gmap\_mc50a27df26c7ade95dbfb4b79c2c7906 = {
positions : {
930 : new google.maps.LatLng( '-33.87', '151.188333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc50a27df26c7ade95dbfb4b79c2c7906' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.positions ) {
gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.bounds.extend( gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.positions[m] );
}
// Render markers
for ( var m in gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.positions ) {
gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.map,
position : gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.map.setCenter( gmap\_mc50a27df26c7ade95dbfb4b79c2c7906.positions[930] );
});
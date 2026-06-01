---
title: Hardly Strictly Bluegrass
date: '2013-10-06T12:47:47+00:00'
format: image
service: flickr
tags:
- hardlystrictlybluegrass
- hsb2013
- vision:mountain=0619
- vision:outdoor=0595
- vision:plant=0533
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291170103_5441a1527a_o.jpg?fit=1500%2C1500
---

[![Hardly Strictly Bluegrass](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/10/12291170103_5441a1527a_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/10/06/hardly-strictly-bluegrass-2/) 
# [Hardly Strictly Bluegrass](http://dentedreality.com.au/2013/10/06/hardly-strictly-bluegrass-2/)

Golden Gate Park, San Francisco





* #[hardlystrictlybluegrass](http://dentedreality.com.au/tags/hardlystrictlybluegrass/)
* #[hsb2013](http://dentedreality.com.au/tags/hsb2013/)
* #[vision:mountain=0619](http://dentedreality.com.au/tags/visionmountain0619/)
* #[vision:outdoor=0595](http://dentedreality.com.au/tags/visionoutdoor0595/)
* #[vision:plant=0533](http://dentedreality.com.au/tags/visionplant0533/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291170103/) [12:47 pm, October 6, 2013](http://dentedreality.com.au/2013/10/06/hardly-strictly-bluegrass-2/ "12:47 pm") 
jQuery(document).ready(function(){
var gmap\_m618945e4d67f8954663619b47d1ded9c = {
positions : {
7 : new google.maps.LatLng( '37.771166', '-122.485334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m618945e4d67f8954663619b47d1ded9c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m618945e4d67f8954663619b47d1ded9c.positions ) {
gmap\_m618945e4d67f8954663619b47d1ded9c.bounds.extend( gmap\_m618945e4d67f8954663619b47d1ded9c.positions[m] );
}
// Render markers
for ( var m in gmap\_m618945e4d67f8954663619b47d1ded9c.positions ) {
gmap\_m618945e4d67f8954663619b47d1ded9c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m618945e4d67f8954663619b47d1ded9c.map,
position : gmap\_m618945e4d67f8954663619b47d1ded9c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m618945e4d67f8954663619b47d1ded9c.map.setCenter( gmap\_m618945e4d67f8954663619b47d1ded9c.positions[7] );
});
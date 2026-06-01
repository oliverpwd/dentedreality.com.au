---
title: Republica Dominica
date: '2013-12-25T10:02:07+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
- panorama
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901129472_3a2ff02fa0_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13901129472_3a2ff02fa0_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/25/republica-dominica-22/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/25/republica-dominica-22/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)
* #[panorama](http://dentedreality.com.au/tags/panorama/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13901129472/) [10:02 am, December 25, 2013](http://dentedreality.com.au/2013/12/25/republica-dominica-22/ "10:02 am") 
jQuery(document).ready(function(){
var gmap\_mdc8f8a264f218b62537b0f1f4dda284d = {
positions : {
753 : new google.maps.LatLng( '19.285838', '-70.710695' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdc8f8a264f218b62537b0f1f4dda284d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdc8f8a264f218b62537b0f1f4dda284d.positions ) {
gmap\_mdc8f8a264f218b62537b0f1f4dda284d.bounds.extend( gmap\_mdc8f8a264f218b62537b0f1f4dda284d.positions[m] );
}
// Render markers
for ( var m in gmap\_mdc8f8a264f218b62537b0f1f4dda284d.positions ) {
gmap\_mdc8f8a264f218b62537b0f1f4dda284d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdc8f8a264f218b62537b0f1f4dda284d.map,
position : gmap\_mdc8f8a264f218b62537b0f1f4dda284d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdc8f8a264f218b62537b0f1f4dda284d.map.setCenter( gmap\_mdc8f8a264f218b62537b0f1f4dda284d.positions[753] );
});
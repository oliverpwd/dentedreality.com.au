---
title: Camping on Angel Island
date: '2011-11-26T03:49:28+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812210014_2241ec734d_o.jpg?resize=607%2C452
---

[![Camping on Angel Island](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812210014_2241ec734d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-4/) 
# [Camping on Angel Island](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-4/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812210014/) [3:49 am, November 26, 2011](http://dentedreality.com.au/2011/11/26/camping-on-angel-island-4/ "3:49 am") 
jQuery(document).ready(function(){
var gmap\_mbb62b425c9ced1cf25cd687138b0eb2f = {
positions : {
9 : new google.maps.LatLng( '37.864833', '-122.425001' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbb62b425c9ced1cf25cd687138b0eb2f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.positions ) {
gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.bounds.extend( gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.positions[m] );
}
// Render markers
for ( var m in gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.positions ) {
gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.map,
position : gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.map.setCenter( gmap\_mbb62b425c9ced1cf25cd687138b0eb2f.positions[9] );
});
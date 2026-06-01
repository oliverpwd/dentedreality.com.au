---
title: Camping on Angel Island
date: '2011-11-25T11:22:06+00:00'
format: image
service: flickr
tags:
- angelisland
- california
- camping
- outdoors
- sanfrancisco
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812209582_c2b2acc7af_o.jpg?resize=607%2C452
---

[![Camping on Angel Island](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/11/6812209582_c2b2acc7af_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-7/) 
# [Camping on Angel Island](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-7/)





* #[angelisland](http://dentedreality.com.au/tags/angelisland/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[camping](http://dentedreality.com.au/tags/camping/)
* #[outdoors](http://dentedreality.com.au/tags/outdoors/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812209582/) [11:22 am, November 25, 2011](http://dentedreality.com.au/2011/11/25/camping-on-angel-island-7/ "11:22 am") 
jQuery(document).ready(function(){
var gmap\_m9bc362f835057cd569bd7cef61dbed50 = {
positions : {
775 : new google.maps.LatLng( '37.873166', '-122.440667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9bc362f835057cd569bd7cef61dbed50' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9bc362f835057cd569bd7cef61dbed50.positions ) {
gmap\_m9bc362f835057cd569bd7cef61dbed50.bounds.extend( gmap\_m9bc362f835057cd569bd7cef61dbed50.positions[m] );
}
// Render markers
for ( var m in gmap\_m9bc362f835057cd569bd7cef61dbed50.positions ) {
gmap\_m9bc362f835057cd569bd7cef61dbed50.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9bc362f835057cd569bd7cef61dbed50.map,
position : gmap\_m9bc362f835057cd569bd7cef61dbed50.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9bc362f835057cd569bd7cef61dbed50.map.setCenter( gmap\_m9bc362f835057cd569bd7cef61dbed50.positions[775] );
});
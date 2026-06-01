---
title: Oslo
date: '2011-10-28T10:13:03+00:00'
format: image
service: flickr
tags:
- norway
- Oslo
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278029_2e86d9e977_o.jpg?resize=607%2C813
---

[![Oslo](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/10/6958278029_2e86d9e977_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/10/28/oslo-2/) 
# [Oslo](http://dentedreality.com.au/2011/10/28/oslo-2/)





* #[norway](http://dentedreality.com.au/tags/norway/)
* #[Oslo](http://dentedreality.com.au/tags/oslo/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6958278029/) [10:13 am, October 28, 2011](http://dentedreality.com.au/2011/10/28/oslo-2/ "10:13 am") 
jQuery(document).ready(function(){
var gmap\_ma42a05549ea37c4ec490418677d2e9da = {
positions : {
90 : new google.maps.LatLng( '59.929666', '10.706333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma42a05549ea37c4ec490418677d2e9da' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma42a05549ea37c4ec490418677d2e9da.positions ) {
gmap\_ma42a05549ea37c4ec490418677d2e9da.bounds.extend( gmap\_ma42a05549ea37c4ec490418677d2e9da.positions[m] );
}
// Render markers
for ( var m in gmap\_ma42a05549ea37c4ec490418677d2e9da.positions ) {
gmap\_ma42a05549ea37c4ec490418677d2e9da.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma42a05549ea37c4ec490418677d2e9da.map,
position : gmap\_ma42a05549ea37c4ec490418677d2e9da.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma42a05549ea37c4ec490418677d2e9da.map.setCenter( gmap\_ma42a05549ea37c4ec490418677d2e9da.positions[90] );
});
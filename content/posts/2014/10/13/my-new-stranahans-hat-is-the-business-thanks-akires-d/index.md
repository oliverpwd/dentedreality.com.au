---
title: ''
date: '2014-10-13T17:19:00+00:00'
format: image
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10727655_1490794794540606_939217248_n.jpg?resize=640%2C640
---

[![My new @stranahans hat is the business! Thanks @akires :D](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/10/10727655_1490794794540606_939217248_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/10/13/my-new-stranahans-hat-is-the-business-thanks-akires-d/) 

My new @stranahans hat is the business! Thanks @akires ![:D](http://i2.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_biggrin.gif?w=607)





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/uHGFaHimFU/) [5:19 pm, October 13, 2014](http://dentedreality.com.au/2014/10/13/my-new-stranahans-hat-is-the-business-thanks-akires-d/ "5:19 pm") 
jQuery(document).ready(function(){
var gmap\_m7c673d9ee3591c51635211d419198b12 = {
positions : {
908 : new google.maps.LatLng( '39.735583333', '-104.97867' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7c673d9ee3591c51635211d419198b12' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7c673d9ee3591c51635211d419198b12.positions ) {
gmap\_m7c673d9ee3591c51635211d419198b12.bounds.extend( gmap\_m7c673d9ee3591c51635211d419198b12.positions[m] );
}
// Render markers
for ( var m in gmap\_m7c673d9ee3591c51635211d419198b12.positions ) {
gmap\_m7c673d9ee3591c51635211d419198b12.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7c673d9ee3591c51635211d419198b12.map,
position : gmap\_m7c673d9ee3591c51635211d419198b12.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7c673d9ee3591c51635211d419198b12.map.setCenter( gmap\_m7c673d9ee3591c51635211d419198b12.positions[908] );
});
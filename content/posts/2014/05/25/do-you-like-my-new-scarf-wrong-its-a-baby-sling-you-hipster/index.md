---
title: ''
date: '2014-05-25T11:18:03+00:00'
format: image
service: instagram
tags:
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10388051_292834374226149_315574532_n.jpg?resize=640%2C640
---

[![Do you like my new scarf? WRONG! It's a baby sling you hipster.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/05/10388051_292834374226149_315574532_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/05/25/do-you-like-my-new-scarf-wrong-its-a-baby-sling-you-hipster/) 

Do you like my new scarf? WRONG! It’s a baby sling you hipster.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/obR011CmM3/) [11:18 am, May 25, 2014](http://dentedreality.com.au/2014/05/25/do-you-like-my-new-scarf-wrong-its-a-baby-sling-you-hipster/ "11:18 am") 
jQuery(document).ready(function(){
var gmap\_maf4adaff7d484cbc0516c399de65e634 = {
positions : {
344 : new google.maps.LatLng( '40.633580494', '-74.014391804' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf4adaff7d484cbc0516c399de65e634' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf4adaff7d484cbc0516c399de65e634.positions ) {
gmap\_maf4adaff7d484cbc0516c399de65e634.bounds.extend( gmap\_maf4adaff7d484cbc0516c399de65e634.positions[m] );
}
// Render markers
for ( var m in gmap\_maf4adaff7d484cbc0516c399de65e634.positions ) {
gmap\_maf4adaff7d484cbc0516c399de65e634.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf4adaff7d484cbc0516c399de65e634.map,
position : gmap\_maf4adaff7d484cbc0516c399de65e634.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf4adaff7d484cbc0516c399de65e634.map.setCenter( gmap\_maf4adaff7d484cbc0516c399de65e634.positions[344] );
});
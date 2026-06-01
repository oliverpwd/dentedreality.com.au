---
title: HUGE BILL!
date: '2009-12-15T12:31:54+00:00'
format: image
service: flickr
tags:
- bill
- Chile
- pesos
- Santiago
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4203485648_9768fbe9bc_o.jpg?resize=607%2C809
---

[![HUGE BILL!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2009/12/4203485648_9768fbe9bc_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2009/12/15/huge-bill/) 
# [HUGE BILL!](http://dentedreality.com.au/2009/12/15/huge-bill/)

Not really, it’s in pesos ![:)](http://i1.wp.com/dentedreality.com.au/wp-includes/images/smilies/simple-smile.png?w=607)





* #[bill](http://dentedreality.com.au/tags/bill/)
* #[Chile](http://dentedreality.com.au/tags/chile/)
* #[pesos](http://dentedreality.com.au/tags/pesos/)
* #[Santiago](http://dentedreality.com.au/tags/santiago/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4203485648/) [12:31 pm, December 15, 2009](http://dentedreality.com.au/2009/12/15/huge-bill/ "12:31 pm") 
jQuery(document).ready(function(){
var gmap\_m7dc6f5b9038da4d0f274fddfee0997a9 = {
positions : {
993 : new google.maps.LatLng( '-33.4345', '-70.640834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7dc6f5b9038da4d0f274fddfee0997a9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.positions ) {
gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.bounds.extend( gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.positions[m] );
}
// Render markers
for ( var m in gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.positions ) {
gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.map,
position : gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.map.setCenter( gmap\_m7dc6f5b9038da4d0f274fddfee0997a9.positions[993] );
});
---
title: Ramsay Wedding
date: '2011-01-16T11:14:45+00:00'
format: image
service: flickr
tags:
- beach
- dunsborough
- ramsaywedding
- sheree
- todd
- wedding
- westernaustralia
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114633_320d867236_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114633_320d867236_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/16/ramsay-wedding-52/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/16/ramsay-wedding-52/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434114633/) [11:14 am, January 16, 2011](http://dentedreality.com.au/2011/01/16/ramsay-wedding-52/ "11:14 am") 
jQuery(document).ready(function(){
var gmap\_m3acef6b03bf8d06b079a2caeb102daa6 = {
positions : {
798 : new google.maps.LatLng( '-33.543334', '115.033333' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3acef6b03bf8d06b079a2caeb102daa6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3acef6b03bf8d06b079a2caeb102daa6.positions ) {
gmap\_m3acef6b03bf8d06b079a2caeb102daa6.bounds.extend( gmap\_m3acef6b03bf8d06b079a2caeb102daa6.positions[m] );
}
// Render markers
for ( var m in gmap\_m3acef6b03bf8d06b079a2caeb102daa6.positions ) {
gmap\_m3acef6b03bf8d06b079a2caeb102daa6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3acef6b03bf8d06b079a2caeb102daa6.map,
position : gmap\_m3acef6b03bf8d06b079a2caeb102daa6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3acef6b03bf8d06b079a2caeb102daa6.map.setCenter( gmap\_m3acef6b03bf8d06b079a2caeb102daa6.positions[798] );
});
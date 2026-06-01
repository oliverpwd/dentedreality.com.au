---
title: Ramsay Wedding
date: '2011-01-16T11:12:43+00:00'
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
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114385_d11a89bbde_o.jpg?resize=607%2C452
---

[![Ramsay Wedding](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434114385_d11a89bbde_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/16/ramsay-wedding-53/) 
# [Ramsay Wedding](http://dentedreality.com.au/2011/01/16/ramsay-wedding-53/)

Pics from the weekend in Dunsborough for Todd and Ree’s awesome wedding!





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[dunsborough](http://dentedreality.com.au/tags/dunsborough/)
* #[ramsaywedding](http://dentedreality.com.au/tags/ramsaywedding/)
* #[sheree](http://dentedreality.com.au/tags/sheree/)
* #[todd](http://dentedreality.com.au/tags/todd/)
* #[wedding](http://dentedreality.com.au/tags/wedding/)
* #[westernaustralia](http://dentedreality.com.au/tags/westernaustralia/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434114385/) [11:12 am, January 16, 2011](http://dentedreality.com.au/2011/01/16/ramsay-wedding-53/ "11:12 am") 
jQuery(document).ready(function(){
var gmap\_maf3ee1d347b183524d97b930d4eb246b = {
positions : {
200 : new google.maps.LatLng( '-33.543667', '115.033' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf3ee1d347b183524d97b930d4eb246b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf3ee1d347b183524d97b930d4eb246b.positions ) {
gmap\_maf3ee1d347b183524d97b930d4eb246b.bounds.extend( gmap\_maf3ee1d347b183524d97b930d4eb246b.positions[m] );
}
// Render markers
for ( var m in gmap\_maf3ee1d347b183524d97b930d4eb246b.positions ) {
gmap\_maf3ee1d347b183524d97b930d4eb246b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf3ee1d347b183524d97b930d4eb246b.map,
position : gmap\_maf3ee1d347b183524d97b930d4eb246b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf3ee1d347b183524d97b930d4eb246b.map.setCenter( gmap\_maf3ee1d347b183524d97b930d4eb246b.positions[200] );
});
---
title: ''
date: '2016-08-09T23:14:37+00:00'
format: image
service: instagram
tags:
- colorado
- creek
- fatbike
- mountainbike
- prospecttrail
- telluride
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13745071_1632376450405714_1842533575_n.jpg?fit=640%2C640
---

[![Creek crossings on a #fatbike. Yes please. #mountainbike #creek #colorado #prospecttrail #telluride](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13745071_1632376450405714_1842533575_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/09/creek-crossings-on-a-fatbike-yes-please-mountainbike-creek-colorado-prospecttrail-telluride/) 

Creek crossings on a #fatbike. Yes please. #mountainbike #creek #colorado #prospecttrail #telluride





* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[creek](http://dentedreality.com.au/tags/creek/)
* #[fatbike](http://dentedreality.com.au/tags/fatbike/)
* #[mountainbike](http://dentedreality.com.au/tags/mountainbike/)
* #[prospecttrail](http://dentedreality.com.au/tags/prospecttrail/)
* #[telluride](http://dentedreality.com.au/tags/telluride/)

Posted on [Instagram](https://www.instagram.com/p/BI6oM0lAKiM/) [11:14 pm, August 9, 2016](http://dentedreality.com.au/2016/08/09/creek-crossings-on-a-fatbike-yes-please-mountainbike-creek-colorado-prospecttrail-telluride/ "11:14 pm") 
jQuery(document).ready(function(){
var gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1 = {
positions : {
82 : new google.maps.LatLng( '37.939153', '-107.816317' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.positions ) {
gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.bounds.extend( gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.positions[m] );
}
// Render markers
for ( var m in gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.positions ) {
gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.map,
position : gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.map.setCenter( gmap\_m6c6e9f38ce6ed85d48bcb4f08d5c38d1.positions[82] );
});
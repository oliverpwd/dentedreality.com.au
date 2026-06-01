---
title: Bremer Bay
date: '2011-01-18T05:44:10+00:00'
format: image
service: flickr
tags:
- australia
- beach
- bremerbay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434116193_67a1ec73b4_o.jpg?resize=607%2C452
---

[![Bremer Bay](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434116193_67a1ec73b4_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/18/bremer-bay-32/) 
# [Bremer Bay](http://dentedreality.com.au/2011/01/18/bremer-bay-32/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beach](http://dentedreality.com.au/tags/beach/)
* #[bremerbay](http://dentedreality.com.au/tags/bremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434116193/) [5:44 am, January 18, 2011](http://dentedreality.com.au/2011/01/18/bremer-bay-32/ "5:44 am") 
jQuery(document).ready(function(){
var gmap\_mc3d6a0bc442ca9200276315aba88ff9c = {
positions : {
50 : new google.maps.LatLng( '-34.393834', '119.399666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc3d6a0bc442ca9200276315aba88ff9c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc3d6a0bc442ca9200276315aba88ff9c.positions ) {
gmap\_mc3d6a0bc442ca9200276315aba88ff9c.bounds.extend( gmap\_mc3d6a0bc442ca9200276315aba88ff9c.positions[m] );
}
// Render markers
for ( var m in gmap\_mc3d6a0bc442ca9200276315aba88ff9c.positions ) {
gmap\_mc3d6a0bc442ca9200276315aba88ff9c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc3d6a0bc442ca9200276315aba88ff9c.map,
position : gmap\_mc3d6a0bc442ca9200276315aba88ff9c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc3d6a0bc442ca9200276315aba88ff9c.map.setCenter( gmap\_mc3d6a0bc442ca9200276315aba88ff9c.positions[50] );
});
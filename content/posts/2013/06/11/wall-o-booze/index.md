---
title: Wall o’ Booze
date: '2013-06-11T18:06:35+00:00'
format: image
service: flickr
tags:
- bar
- booze
- paddys
- Portland
- rye
- scotch
- whiskey
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439830720_572527c615_o.jpg?resize=607%2C452
---

[![Wall o' Booze](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9439830720_572527c615_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/06/11/wall-o-booze/) 
# [Wall o’ Booze](http://dentedreality.com.au/2013/06/11/wall-o-booze/)

At Paddy’s, in Portland





* #[bar](http://dentedreality.com.au/tags/bar/)
* #[booze](http://dentedreality.com.au/tags/booze/)
* #[paddys](http://dentedreality.com.au/tags/paddys/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[rye](http://dentedreality.com.au/tags/rye/)
* #[scotch](http://dentedreality.com.au/tags/scotch/)
* #[whiskey](http://dentedreality.com.au/tags/whiskey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9439830720/) [6:06 pm, June 11, 2013](http://dentedreality.com.au/2013/06/11/wall-o-booze/ "6:06 pm") 
jQuery(document).ready(function(){
var gmap\_me3223943d148023cc66c771e1964d7d7 = {
positions : {
302 : new google.maps.LatLng( '45.516999', '-122.673667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me3223943d148023cc66c771e1964d7d7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me3223943d148023cc66c771e1964d7d7.positions ) {
gmap\_me3223943d148023cc66c771e1964d7d7.bounds.extend( gmap\_me3223943d148023cc66c771e1964d7d7.positions[m] );
}
// Render markers
for ( var m in gmap\_me3223943d148023cc66c771e1964d7d7.positions ) {
gmap\_me3223943d148023cc66c771e1964d7d7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me3223943d148023cc66c771e1964d7d7.map,
position : gmap\_me3223943d148023cc66c771e1964d7d7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me3223943d148023cc66c771e1964d7d7.map.setCenter( gmap\_me3223943d148023cc66c771e1964d7d7.positions[302] );
});
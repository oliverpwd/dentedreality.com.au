---
title: The Cat Empire
date: '2012-04-19T17:31:04-06:00'
format: image
service: flickr
tags:
- catempire
- livemusic
- sanfrancisco
latitude: '37.771499'
longitude: '-122.4135'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190604/7770705990_f392c68bba_o.jpg
---

[![The Cat Empire](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190604/7770705990_f392c68bba_o.jpg)](https://dentedreality.com.au/2012/04/19/the-cat-empire-3/) 
# [The Cat Empire](https://dentedreality.com.au/2012/04/19/the-cat-empire-3/)

[![The Cat Empire](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190604/7770705990_f392c68bba_o.jpg)](http://www.flickr.com/photos/borkazoid/7770705990/)

37.771499-122.4135




* #[catempire](https://dentedreality.com.au/tags/catempire/)
* #[livemusic](https://dentedreality.com.au/tags/livemusic/)
* #[sanfrancisco](https://dentedreality.com.au/tags/sanfrancisco/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770705990/) [5:31 pm, April 19, 2012](https://dentedreality.com.au/2012/04/19/the-cat-empire-3/ "5:31 pm") 
jQuery(document).ready(function(){
var gmap\_mdfa105838bd33acd898cf2e6b1989f3b = {
positions : {
712 : new google.maps.LatLng( '37.771499', '-122.4135' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdfa105838bd33acd898cf2e6b1989f3b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdfa105838bd33acd898cf2e6b1989f3b.positions ) {
gmap\_mdfa105838bd33acd898cf2e6b1989f3b.bounds.extend( gmap\_mdfa105838bd33acd898cf2e6b1989f3b.positions[m] );
}
// Render markers
for ( var m in gmap\_mdfa105838bd33acd898cf2e6b1989f3b.positions ) {
gmap\_mdfa105838bd33acd898cf2e6b1989f3b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdfa105838bd33acd898cf2e6b1989f3b.map,
position : gmap\_mdfa105838bd33acd898cf2e6b1989f3b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdfa105838bd33acd898cf2e6b1989f3b.map.setCenter( gmap\_mdfa105838bd33acd898cf2e6b1989f3b.positions[712] );
});
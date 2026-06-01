---
title: The International Language of Coca Cola
date: '2006-12-27T23:20:23-07:00'
format: image
service: flickr
tags:
- cocacola
- coke
- phuket
- thailand
- thailand06
latitude: '7.955282'
longitude: '98.282489'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2006/12/14184348/348100219_1e3efefe61_o.jpg
---

[![The International Language of Coca Cola](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2006/12/14184348/348100219_1e3efefe61_o.jpg)](https://dentedreality.com.au/2006/12/27/the-international-language-of-coca-cola/) 
# [The International Language of Coca Cola](https://dentedreality.com.au/2006/12/27/the-international-language-of-coca-cola/)

[![The International Language of Coca Cola](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2006/12/14184348/348100219_1e3efefe61_o.jpg)](http://www.flickr.com/photos/borkazoid/348100219/)

7.95528298.282489




* #[cocacola](https://dentedreality.com.au/tags/cocacola/)
* #[coke](https://dentedreality.com.au/tags/coke/)
* #[phuket](https://dentedreality.com.au/tags/phuket/)
* #[thailand](https://dentedreality.com.au/tags/thailand/)
* #[thailand06](https://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/348100219/) [11:20 pm, December 27, 2006](https://dentedreality.com.au/2006/12/27/the-international-language-of-coca-cola/ "11:20 pm") 
jQuery(document).ready(function(){
var gmap\_m9e6c48614cedff3c72d08d6e51ce3859 = {
positions : {
169 : new google.maps.LatLng( '7.955282', '98.282489' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9e6c48614cedff3c72d08d6e51ce3859' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9e6c48614cedff3c72d08d6e51ce3859.positions ) {
gmap\_m9e6c48614cedff3c72d08d6e51ce3859.bounds.extend( gmap\_m9e6c48614cedff3c72d08d6e51ce3859.positions[m] );
}
// Render markers
for ( var m in gmap\_m9e6c48614cedff3c72d08d6e51ce3859.positions ) {
gmap\_m9e6c48614cedff3c72d08d6e51ce3859.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9e6c48614cedff3c72d08d6e51ce3859.map,
position : gmap\_m9e6c48614cedff3c72d08d6e51ce3859.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9e6c48614cedff3c72d08d6e51ce3859.map.setCenter( gmap\_m9e6c48614cedff3c72d08d6e51ce3859.positions[169] );
});
---
title: Wild Horse on the Beach
date: '2013-07-14T12:35:01+00:00'
format: image
service: flickr
tags:
- beach
- costarica
- horse
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440187712_3f06878d7a_o.jpg?resize=607%2C455
---

[![Wild Horse on the Beach](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440187712_3f06878d7a_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/07/14/wild-horse-on-the-beach/) 
# [Wild Horse on the Beach](http://dentedreality.com.au/2013/07/14/wild-horse-on-the-beach/)





* #[beach](http://dentedreality.com.au/tags/beach/)
* #[costarica](http://dentedreality.com.au/tags/costarica/)
* #[horse](http://dentedreality.com.au/tags/horse/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440187712/) [12:35 pm, July 14, 2013](http://dentedreality.com.au/2013/07/14/wild-horse-on-the-beach/ "12:35 pm") 
jQuery(document).ready(function(){
var gmap\_meacc0c09ab9520288d25188cf1d6ec50 = {
positions : {
574 : new google.maps.LatLng( '9.879827', '-85.531048' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_meacc0c09ab9520288d25188cf1d6ec50' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_meacc0c09ab9520288d25188cf1d6ec50.positions ) {
gmap\_meacc0c09ab9520288d25188cf1d6ec50.bounds.extend( gmap\_meacc0c09ab9520288d25188cf1d6ec50.positions[m] );
}
// Render markers
for ( var m in gmap\_meacc0c09ab9520288d25188cf1d6ec50.positions ) {
gmap\_meacc0c09ab9520288d25188cf1d6ec50.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_meacc0c09ab9520288d25188cf1d6ec50.map,
position : gmap\_meacc0c09ab9520288d25188cf1d6ec50.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_meacc0c09ab9520288d25188cf1d6ec50.map.setCenter( gmap\_meacc0c09ab9520288d25188cf1d6ec50.positions[574] );
});
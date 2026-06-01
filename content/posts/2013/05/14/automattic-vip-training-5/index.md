---
title: Automattic VIP Training
date: '2013-05-14T13:40:48+00:00'
format: image
service: flickr
tags:
- automattic
- vip
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436926943_8e983874cd_o.jpg?resize=607%2C452
---

[![Automattic VIP Training](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/05/9436926943_8e983874cd_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/05/14/automattic-vip-training-5/) 
# [Automattic VIP Training](http://dentedreality.com.au/2013/05/14/automattic-vip-training-5/)

Annual VIP training workshop, held in Napa, CA





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[vip](http://dentedreality.com.au/tags/vip/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9436926943/) [1:40 pm, May 14, 2013](http://dentedreality.com.au/2013/05/14/automattic-vip-training-5/ "1:40 pm") 
jQuery(document).ready(function(){
var gmap\_m0ea3a9fdce05a9b9752945dacb161884 = {
positions : {
716 : new google.maps.LatLng( '38.256', '-122.331167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0ea3a9fdce05a9b9752945dacb161884' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0ea3a9fdce05a9b9752945dacb161884.positions ) {
gmap\_m0ea3a9fdce05a9b9752945dacb161884.bounds.extend( gmap\_m0ea3a9fdce05a9b9752945dacb161884.positions[m] );
}
// Render markers
for ( var m in gmap\_m0ea3a9fdce05a9b9752945dacb161884.positions ) {
gmap\_m0ea3a9fdce05a9b9752945dacb161884.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0ea3a9fdce05a9b9752945dacb161884.map,
position : gmap\_m0ea3a9fdce05a9b9752945dacb161884.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0ea3a9fdce05a9b9752945dacb161884.map.setCenter( gmap\_m0ea3a9fdce05a9b9752945dacb161884.positions[716] );
});
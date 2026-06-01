---
title: NERTs in South Park
date: '2010-10-16T05:08:39+00:00'
format: image
service: flickr
tags:
- california
- cert
- nert
- sanfrancisco
- southpark
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183766950_b24f481cd6_o.jpg?resize=607%2C452
---

[![NERTs in South Park](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/10/5183766950_b24f481cd6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2010/10/16/nerts-in-south-park/) 
# [NERTs in South Park](http://dentedreality.com.au/2010/10/16/nerts-in-south-park/)





* #[california](http://dentedreality.com.au/tags/california/)
* #[cert](http://dentedreality.com.au/tags/cert/)
* #[nert](http://dentedreality.com.au/tags/nert/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[southpark](http://dentedreality.com.au/tags/southpark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183766950/) [5:08 am, October 16, 2010](http://dentedreality.com.au/2010/10/16/nerts-in-south-park/ "5:08 am") 
jQuery(document).ready(function(){
var gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689 = {
positions : {
604 : new google.maps.LatLng( '37.781666', '-122.394' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.positions ) {
gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.bounds.extend( gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.positions[m] );
}
// Render markers
for ( var m in gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.positions ) {
gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.map,
position : gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.map.setCenter( gmap\_m8a6e025d1fea42dcf3f9c6500c0ee689.positions[604] );
});
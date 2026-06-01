---
title: Jackson Arms
date: '2011-05-30T09:12:03+00:00'
format: image
service: flickr
tags:
- iris
- jacksonarms
- memorialday
- shooting
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435690_0829e88271_o.jpg?resize=607%2C813
---

[![Jackson Arms](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5803435690_0829e88271_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/05/30/jackson-arms-2/) 
# [Jackson Arms](http://dentedreality.com.au/2011/05/30/jackson-arms-2/)

Memorial Day at the range





* #[iris](http://dentedreality.com.au/tags/iris/)
* #[jacksonarms](http://dentedreality.com.au/tags/jacksonarms/)
* #[memorialday](http://dentedreality.com.au/tags/memorialday/)
* #[shooting](http://dentedreality.com.au/tags/shooting/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5803435690/) [9:12 am, May 30, 2011](http://dentedreality.com.au/2011/05/30/jackson-arms-2/ "9:12 am") 
jQuery(document).ready(function(){
var gmap\_m38cff9243357f55e882c313029a42c2f = {
positions : {
851 : new google.maps.LatLng( '37.645166', '-122.4025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m38cff9243357f55e882c313029a42c2f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m38cff9243357f55e882c313029a42c2f.positions ) {
gmap\_m38cff9243357f55e882c313029a42c2f.bounds.extend( gmap\_m38cff9243357f55e882c313029a42c2f.positions[m] );
}
// Render markers
for ( var m in gmap\_m38cff9243357f55e882c313029a42c2f.positions ) {
gmap\_m38cff9243357f55e882c313029a42c2f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m38cff9243357f55e882c313029a42c2f.map,
position : gmap\_m38cff9243357f55e882c313029a42c2f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m38cff9243357f55e882c313029a42c2f.map.setCenter( gmap\_m38cff9243357f55e882c313029a42c2f.positions[851] );
});
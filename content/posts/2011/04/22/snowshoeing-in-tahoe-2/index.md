---
title: Snowshoeing in Tahoe
date: '2011-04-22T10:30:24+00:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- california
- me
- snow
- snowshoeing
- tahoe
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146923_f88f1beff9_o.jpg?resize=607%2C452
---

[![Snowshoeing in Tahoe](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/04/5802146923_f88f1beff9_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe-2/) 
# [Snowshoeing in Tahoe](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe-2/)





* #[beau](http://dentedreality.com.au/tags/beau/)
* #[beaulebens](http://dentedreality.com.au/tags/beaulebens/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[me](http://dentedreality.com.au/tags/me/)
* #[snow](http://dentedreality.com.au/tags/snow/)
* #[snowshoeing](http://dentedreality.com.au/tags/snowshoeing/)
* #[tahoe](http://dentedreality.com.au/tags/tahoe/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802146923/) [10:30 am, April 22, 2011](http://dentedreality.com.au/2011/04/22/snowshoeing-in-tahoe-2/ "10:30 am") 
jQuery(document).ready(function(){
var gmap\_mbabc376f5ae25b88a495d030c64b0664 = {
positions : {
179 : new google.maps.LatLng( '39.366166', '-120.264834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mbabc376f5ae25b88a495d030c64b0664' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mbabc376f5ae25b88a495d030c64b0664.positions ) {
gmap\_mbabc376f5ae25b88a495d030c64b0664.bounds.extend( gmap\_mbabc376f5ae25b88a495d030c64b0664.positions[m] );
}
// Render markers
for ( var m in gmap\_mbabc376f5ae25b88a495d030c64b0664.positions ) {
gmap\_mbabc376f5ae25b88a495d030c64b0664.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mbabc376f5ae25b88a495d030c64b0664.map,
position : gmap\_mbabc376f5ae25b88a495d030c64b0664.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mbabc376f5ae25b88a495d030c64b0664.map.setCenter( gmap\_mbabc376f5ae25b88a495d030c64b0664.positions[179] );
});
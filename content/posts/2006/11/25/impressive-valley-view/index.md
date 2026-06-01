---
title: Impressive Valley View
date: '2006-11-25T10:23:48+00:00'
format: image
service: flickr
tags:
- bigsur
- bottchersgap
- california
- lospadresnationalpark
- mountains
- ridgeline
- valley
- view
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308097797_72dc2ebf20_o.jpg?resize=607%2C455
---

[![Impressive Valley View](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/11/308097797_72dc2ebf20_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/11/25/impressive-valley-view/) 
# [Impressive Valley View](http://dentedreality.com.au/2006/11/25/impressive-valley-view/)

One of many.





* #[bigsur](http://dentedreality.com.au/tags/bigsur/)
* #[bottchersgap](http://dentedreality.com.au/tags/bottchersgap/)
* #[california](http://dentedreality.com.au/tags/california/)
* #[lospadresnationalpark](http://dentedreality.com.au/tags/lospadresnationalpark/)
* #[mountains](http://dentedreality.com.au/tags/mountains/)
* #[ridgeline](http://dentedreality.com.au/tags/ridgeline/)
* #[valley](http://dentedreality.com.au/tags/valley/)
* #[view](http://dentedreality.com.au/tags/view/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/308097797/) [10:23 am, November 25, 2006](http://dentedreality.com.au/2006/11/25/impressive-valley-view/ "10:23 am") 
jQuery(document).ready(function(){
var gmap\_m5183b4729b70319e098c72815b8f599f = {
positions : {
505 : new google.maps.LatLng( '36.34389', '-121.776409' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5183b4729b70319e098c72815b8f599f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5183b4729b70319e098c72815b8f599f.positions ) {
gmap\_m5183b4729b70319e098c72815b8f599f.bounds.extend( gmap\_m5183b4729b70319e098c72815b8f599f.positions[m] );
}
// Render markers
for ( var m in gmap\_m5183b4729b70319e098c72815b8f599f.positions ) {
gmap\_m5183b4729b70319e098c72815b8f599f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5183b4729b70319e098c72815b8f599f.map,
position : gmap\_m5183b4729b70319e098c72815b8f599f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5183b4729b70319e098c72815b8f599f.map.setCenter( gmap\_m5183b4729b70319e098c72815b8f599f.positions[505] );
});
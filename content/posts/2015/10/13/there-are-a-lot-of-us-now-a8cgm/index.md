---
title: ''
date: '2015-10-13T13:34:57-06:00'
format: image
service: instagram
tags:
- a8cgm
latitude: '40.6853018'
longitude: '-111.5566372'
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12093700_1652343228363658_262023328_n.jpg?resize=640%2C640
---

[![There are a lot of us now #a8cgm](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12093700_1652343228363658_262023328_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/10/13/there-are-a-lot-of-us-now-a8cgm/) 

[![There are a lot of us now #a8cgm](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2015/10/12093700_1652343228363658_262023328_n.jpg?resize=640%2C640)](https://instagram.com/p/8yilyACmF1/)

There are a lot of us now #a8cgm

40.6853018-111.5566372




* #[a8cgm](https://dentedreality.com.au/tags/a8cgm/)

Posted on [Instagram](https://instagram.com/p/8yilyACmF1/) [1:34 pm, October 13, 2015](https://dentedreality.com.au/2015/10/13/there-are-a-lot-of-us-now-a8cgm/ "1:34 pm") 
jQuery(document).ready(function(){
var gmap\_m05ca837d1612bdf5e898943e1eba090f = {
positions : {
304 : new google.maps.LatLng( '40.685301808', '-111.556637182' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m05ca837d1612bdf5e898943e1eba090f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m05ca837d1612bdf5e898943e1eba090f.positions ) {
gmap\_m05ca837d1612bdf5e898943e1eba090f.bounds.extend( gmap\_m05ca837d1612bdf5e898943e1eba090f.positions[m] );
}
// Render markers
for ( var m in gmap\_m05ca837d1612bdf5e898943e1eba090f.positions ) {
gmap\_m05ca837d1612bdf5e898943e1eba090f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m05ca837d1612bdf5e898943e1eba090f.map,
position : gmap\_m05ca837d1612bdf5e898943e1eba090f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m05ca837d1612bdf5e898943e1eba090f.map.setCenter( gmap\_m05ca837d1612bdf5e898943e1eba090f.positions[304] );
});
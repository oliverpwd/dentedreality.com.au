---
title: ''
date: '2015-09-25T19:44:44+00:00'
format: image
service: instagram
tags:
- bbq
- omg
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11934611_471736106333823_1454555665_n.jpg?resize=640%2C640
---

[![Snacky time #bbq #omg](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11934611_471736106333823_1454555665_n.jpg?resize=640%2C640)](https://dentedreality.com.au/2015/09/25/snacky-time-bbq-omg/) 

[![Snacky time #bbq #omg](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/09/11934611_471736106333823_1454555665_n.jpg?resize=640%2C640)](https://instagram.com/p/8E2mZZimFm/)

Snacky time #bbq #omg





* #[bbq](https://dentedreality.com.au/tags/bbq/)
* #[omg](https://dentedreality.com.au/tags/omg/)

Posted on [Instagram](https://instagram.com/p/8E2mZZimFm/) [7:44 pm, September 25, 2015](https://dentedreality.com.au/2015/09/25/snacky-time-bbq-omg/ "7:44 pm") 
jQuery(document).ready(function(){
var gmap\_m6801e6f370bf54ce302c7698d42bd099 = {
positions : {
482 : new google.maps.LatLng( '39.7677224', '-104.899998687' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6801e6f370bf54ce302c7698d42bd099' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6801e6f370bf54ce302c7698d42bd099.positions ) {
gmap\_m6801e6f370bf54ce302c7698d42bd099.bounds.extend( gmap\_m6801e6f370bf54ce302c7698d42bd099.positions[m] );
}
// Render markers
for ( var m in gmap\_m6801e6f370bf54ce302c7698d42bd099.positions ) {
gmap\_m6801e6f370bf54ce302c7698d42bd099.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6801e6f370bf54ce302c7698d42bd099.map,
position : gmap\_m6801e6f370bf54ce302c7698d42bd099.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6801e6f370bf54ce302c7698d42bd099.map.setCenter( gmap\_m6801e6f370bf54ce302c7698d42bd099.positions[482] );
});
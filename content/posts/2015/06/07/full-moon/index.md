---
title: ''
date: '2015-06-07T10:00:58+00:00'
format: image
service: instagram
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11247641_1651938625026046_753006345_n.jpg?resize=640%2C640
---

[![Full Moon](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/06/11247641_1651938625026046_753006345_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/06/07/full-moon/) 

Full Moon





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](https://instagram.com/p/3okWjgCmFm/) [10:00 am, June 7, 2015](http://dentedreality.com.au/2015/06/07/full-moon/ "10:00 am") 
jQuery(document).ready(function(){
var gmap\_m79ed7ae703d848ececa07e1bf7cfe0de = {
positions : {
995 : new google.maps.LatLng( '42.039064556', '-74.440885462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m79ed7ae703d848ececa07e1bf7cfe0de' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.positions ) {
gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.bounds.extend( gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.positions[m] );
}
// Render markers
for ( var m in gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.positions ) {
gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.map,
position : gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.map.setCenter( gmap\_m79ed7ae703d848ececa07e1bf7cfe0de.positions[995] );
});
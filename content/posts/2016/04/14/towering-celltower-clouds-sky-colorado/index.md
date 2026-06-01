---
title: ''
date: '2016-04-14T16:25:40+00:00'
format: image
service: instagram
tags:
- celltower
- clouds
- colorado
- sky
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/1172538_571145886379605_2010258378_n.jpg?fit=640%2C640
---

[![Towering. #celltower #clouds #sky #colorado](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/04/1172538_571145886379605_2010258378_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/04/14/towering-celltower-clouds-sky-colorado/) 

Towering. #celltower #clouds #sky #colorado





* #[celltower](http://dentedreality.com.au/tags/celltower/)
* #[clouds](http://dentedreality.com.au/tags/clouds/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[sky](http://dentedreality.com.au/tags/sky/)

Posted on [Instagram](https://www.instagram.com/p/BEMoZMwimAA/) [4:25 pm, April 14, 2016](http://dentedreality.com.au/2016/04/14/towering-celltower-clouds-sky-colorado/ "4:25 pm") 
jQuery(document).ready(function(){
var gmap\_mf95d580d84e904ffb4fb4fc4d0e90657 = {
positions : {
228 : new google.maps.LatLng( '39.7392', '-104.984' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf95d580d84e904ffb4fb4fc4d0e90657' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.positions ) {
gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.bounds.extend( gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.positions[m] );
}
// Render markers
for ( var m in gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.positions ) {
gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.map,
position : gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.map.setCenter( gmap\_mf95d580d84e904ffb4fb4fc4d0e90657.positions[228] );
});
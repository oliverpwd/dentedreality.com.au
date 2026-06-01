---
title: ''
date: '2016-06-24T02:26:48-06:00'
format: image
service: instagram
latitude: '-32.0282407'
longitude: '115.752412'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13422854_199892197074970_967567465_n.jpg?fit=640%2C640
---

[![Ate my baby.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13422854_199892197074970_967567465_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/06/24/ate-my-baby/) 

[![Ate my baby.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/06/13422854_199892197074970_967567465_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BHB81N2g587/)

Ate my baby.

-32.0282407115.752412




Posted on [Instagram](https://www.instagram.com/p/BHB81N2g587/) [2:26 am, June 24, 2016](https://dentedreality.com.au/2016/06/24/ate-my-baby/ "2:26 am") 
jQuery(document).ready(function(){
var gmap\_mf8a8f3b1a038b494f208c10dbdbdae87 = {
positions : {
529 : new google.maps.LatLng( '-32.028240662173', '115.75241201871' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf8a8f3b1a038b494f208c10dbdbdae87' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.positions ) {
gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.bounds.extend( gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.positions[m] );
}
// Render markers
for ( var m in gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.positions ) {
gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.map,
position : gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.map.setCenter( gmap\_mf8a8f3b1a038b494f208c10dbdbdae87.positions[529] );
});
---
title: ''
date: '2016-07-03T02:18:57-06:00'
format: image
service: instagram
tags:
- boat
- darlingharbour
- sydney
- sydneyoperahouse
latitude: '-33.8580845'
longitude: '151.2138514'
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13562068_1565828683721650_544357105_n.jpg?fit=640%2C640
---

[![I'm on a boat. #boat #sydneyoperahouse #darlingharbour #sydney](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13562068_1565828683721650_544357105_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/07/03/im-on-a-boat-boat-sydneyoperahouse-darlingharbour-sydney/) 

[![I'm on a boat. #boat #sydneyoperahouse #darlingharbour #sydney](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/07/13562068_1565828683721650_544357105_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BHZHFlVA59M/)

I’m on a boat. #boat #sydneyoperahouse #darlingharbour #sydney

-33.8580845151.2138514




* #[boat](https://dentedreality.com.au/tags/boat/)
* #[darlingharbour](https://dentedreality.com.au/tags/darlingharbour/)
* #[sydney](https://dentedreality.com.au/tags/sydney/)
* #[sydneyoperahouse](https://dentedreality.com.au/tags/sydneyoperahouse/)

Posted on [Instagram](https://www.instagram.com/p/BHZHFlVA59M/) [2:18 am, July 3, 2016](https://dentedreality.com.au/2016/07/03/im-on-a-boat-boat-sydneyoperahouse-darlingharbour-sydney/ "2:18 am") 
jQuery(document).ready(function(){
var gmap\_mc524776bbff40fc7b715ae8efe2b7961 = {
positions : {
602 : new google.maps.LatLng( '-33.858084492996', '151.21385139503' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc524776bbff40fc7b715ae8efe2b7961' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc524776bbff40fc7b715ae8efe2b7961.positions ) {
gmap\_mc524776bbff40fc7b715ae8efe2b7961.bounds.extend( gmap\_mc524776bbff40fc7b715ae8efe2b7961.positions[m] );
}
// Render markers
for ( var m in gmap\_mc524776bbff40fc7b715ae8efe2b7961.positions ) {
gmap\_mc524776bbff40fc7b715ae8efe2b7961.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc524776bbff40fc7b715ae8efe2b7961.map,
position : gmap\_mc524776bbff40fc7b715ae8efe2b7961.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc524776bbff40fc7b715ae8efe2b7961.map.setCenter( gmap\_mc524776bbff40fc7b715ae8efe2b7961.positions[602] );
});
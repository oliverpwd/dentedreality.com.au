---
title: ''
date: '2016-08-09T23:22:29-06:00'
format: image
service: instagram
tags:
- colorado
- nofilter
- telluride
latitude: '37.9368324'
longitude: '-107.8467141'
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13694550_1116963468371291_1051901762_n.jpg?fit=640%2C640
---

[![Ridiculous sunset. #nofilter #colorado #telluride](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13694550_1116963468371291_1051901762_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/08/09/ridiculous-sunset-nofilter-colorado-telluride/) 

[![Ridiculous sunset. #nofilter #colorado #telluride](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13694550_1116963468371291_1051901762_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BI6pGaxAmpL/)

Ridiculous sunset. #nofilter #colorado #telluride

37.9368324-107.8467141




* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[nofilter](https://dentedreality.com.au/tags/nofilter/)
* #[telluride](https://dentedreality.com.au/tags/telluride/)

Posted on [Instagram](https://www.instagram.com/p/BI6pGaxAmpL/) [11:22 pm, August 9, 2016](https://dentedreality.com.au/2016/08/09/ridiculous-sunset-nofilter-colorado-telluride/ "11:22 pm") 
jQuery(document).ready(function(){
var gmap\_m64e34c50416dc9d0a82d92145fafc39c = {
positions : {
503 : new google.maps.LatLng( '37.936832357025', '-107.84671407332' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m64e34c50416dc9d0a82d92145fafc39c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m64e34c50416dc9d0a82d92145fafc39c.positions ) {
gmap\_m64e34c50416dc9d0a82d92145fafc39c.bounds.extend( gmap\_m64e34c50416dc9d0a82d92145fafc39c.positions[m] );
}
// Render markers
for ( var m in gmap\_m64e34c50416dc9d0a82d92145fafc39c.positions ) {
gmap\_m64e34c50416dc9d0a82d92145fafc39c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m64e34c50416dc9d0a82d92145fafc39c.map,
position : gmap\_m64e34c50416dc9d0a82d92145fafc39c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m64e34c50416dc9d0a82d92145fafc39c.map.setCenter( gmap\_m64e34c50416dc9d0a82d92145fafc39c.positions[503] );
});
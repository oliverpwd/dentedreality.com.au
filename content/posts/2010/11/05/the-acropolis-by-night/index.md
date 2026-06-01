---
title: The Acropolis by Night
date: '2010-11-05T14:01:18-06:00'
format: image
service: flickr
tags:
- acropolis
- Athens
- automattic
- greece
- teamsocial
latitude: '37.973833'
longitude: '23.731166'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789766_559971f1e6_o.jpg
---

[![The Acropolis by Night](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789766_559971f1e6_o.jpg)](https://dentedreality.com.au/2010/11/05/the-acropolis-by-night/) 
# [The Acropolis by Night](https://dentedreality.com.au/2010/11/05/the-acropolis-by-night/)

[![The Acropolis by Night](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183789766_559971f1e6_o.jpg)](http://www.flickr.com/photos/borkazoid/5183789766/)

37.97383323.731166




* #[acropolis](https://dentedreality.com.au/tags/acropolis/)
* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183789766/) [2:01 pm, November 5, 2010](https://dentedreality.com.au/2010/11/05/the-acropolis-by-night/ "2:01 pm") 
jQuery(document).ready(function(){
var gmap\_me407c49cd66ce594a3e1c1cf2a258131 = {
positions : {
686 : new google.maps.LatLng( '37.973833', '23.731166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me407c49cd66ce594a3e1c1cf2a258131' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me407c49cd66ce594a3e1c1cf2a258131.positions ) {
gmap\_me407c49cd66ce594a3e1c1cf2a258131.bounds.extend( gmap\_me407c49cd66ce594a3e1c1cf2a258131.positions[m] );
}
// Render markers
for ( var m in gmap\_me407c49cd66ce594a3e1c1cf2a258131.positions ) {
gmap\_me407c49cd66ce594a3e1c1cf2a258131.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me407c49cd66ce594a3e1c1cf2a258131.map,
position : gmap\_me407c49cd66ce594a3e1c1cf2a258131.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me407c49cd66ce594a3e1c1cf2a258131.map.setCenter( gmap\_me407c49cd66ce594a3e1c1cf2a258131.positions[686] );
});
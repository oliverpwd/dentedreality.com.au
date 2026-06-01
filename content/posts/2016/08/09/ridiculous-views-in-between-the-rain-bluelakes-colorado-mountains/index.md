---
title: ''
date: '2016-08-09T12:30:08+00:00'
format: image
service: instagram
tags:
- bluelakes
- colorado
- mountains
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13724509_686306028189374_1801083243_n.jpg?fit=640%2C640
---

[![Ridiculous views in between the rain. #bluelakes #colorado #mountains](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13724509_686306028189374_1801083243_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/08/09/ridiculous-views-in-between-the-rain-bluelakes-colorado-mountains/) 

Ridiculous views in between the rain. #bluelakes #colorado #mountains





* #[bluelakes](http://dentedreality.com.au/tags/bluelakes/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[mountains](http://dentedreality.com.au/tags/mountains/)

Posted on [Instagram](https://www.instagram.com/p/BI5eceSgBPo/) [12:30 pm, August 9, 2016](http://dentedreality.com.au/2016/08/09/ridiculous-views-in-between-the-rain-bluelakes-colorado-mountains/ "12:30 pm") 
jQuery(document).ready(function(){
var gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f = {
positions : {
248 : new google.maps.LatLng( '38.002025736531', '-107.816817714' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.positions ) {
gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.bounds.extend( gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.positions[m] );
}
// Render markers
for ( var m in gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.positions ) {
gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.map,
position : gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.map.setCenter( gmap\_m45e3b1cddfeb8fbe15b4d73b81b1000f.positions[248] );
});
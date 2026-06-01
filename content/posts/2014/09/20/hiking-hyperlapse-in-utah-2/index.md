---
title: ''
date: '2014-09-20T21:34:25+00:00'
format: image
tags:
- hyperlapse
- photo
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10684286_903498756330014_1445202550_n.jpg?resize=640%2C640
---

[![Hiking #hyperlapse in Utah.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/09/10684286_903498756330014_1445202550_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2014/09/20/hiking-hyperlapse-in-utah-2/) 

Hiking #hyperlapse in Utah.





* #[hyperlapse](http://dentedreality.com.au/tags/hyperlapse/)
* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/tMVB_VimPy/) [9:34 pm, September 20, 2014](http://dentedreality.com.au/2014/09/20/hiking-hyperlapse-in-utah-2/ "9:34 pm") 
jQuery(document).ready(function(){
var gmap\_m12cf89b22351e8da39fbe1a33833be61 = {
positions : {
788 : new google.maps.LatLng( '40.685043627', '-111.55658947' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m12cf89b22351e8da39fbe1a33833be61' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m12cf89b22351e8da39fbe1a33833be61.positions ) {
gmap\_m12cf89b22351e8da39fbe1a33833be61.bounds.extend( gmap\_m12cf89b22351e8da39fbe1a33833be61.positions[m] );
}
// Render markers
for ( var m in gmap\_m12cf89b22351e8da39fbe1a33833be61.positions ) {
gmap\_m12cf89b22351e8da39fbe1a33833be61.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m12cf89b22351e8da39fbe1a33833be61.map,
position : gmap\_m12cf89b22351e8da39fbe1a33833be61.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m12cf89b22351e8da39fbe1a33833be61.map.setCenter( gmap\_m12cf89b22351e8da39fbe1a33833be61.positions[788] );
});
---
title: Koop/Slash
date: '2011-03-11T16:06:31+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802099143_e6f3568974_o.jpg?resize=607%2C813
---

[![Koop/Slash](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802099143_e6f3568974_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2011/03/11/koopslash/) 
# [Koop/Slash](http://dentedreality.com.au/2011/03/11/koopslash/)





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802099143/) [4:06 pm, March 11, 2011](http://dentedreality.com.au/2011/03/11/koopslash/ "4:06 pm") 
jQuery(document).ready(function(){
var gmap\_me55de3b355d34adfc77546be46a1aaf1 = {
positions : {
651 : new google.maps.LatLng( '30.269666', '-97.749834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me55de3b355d34adfc77546be46a1aaf1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me55de3b355d34adfc77546be46a1aaf1.positions ) {
gmap\_me55de3b355d34adfc77546be46a1aaf1.bounds.extend( gmap\_me55de3b355d34adfc77546be46a1aaf1.positions[m] );
}
// Render markers
for ( var m in gmap\_me55de3b355d34adfc77546be46a1aaf1.positions ) {
gmap\_me55de3b355d34adfc77546be46a1aaf1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me55de3b355d34adfc77546be46a1aaf1.map,
position : gmap\_me55de3b355d34adfc77546be46a1aaf1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me55de3b355d34adfc77546be46a1aaf1.map.setCenter( gmap\_me55de3b355d34adfc77546be46a1aaf1.positions[651] );
});
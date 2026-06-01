---
title: Chexees feet are small.
date: '2011-03-12T23:34:03+00:00'
format: image
service: flickr
tags:
- Austin
- sxsw
- sxsw2011
- texas
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802099493_a989a18475_o.jpg?resize=607%2C452
---

[![Chexees feet are small.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/03/5802099493_a989a18475_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/03/12/chexees-feet-are-small/) 
# [Chexees feet are small.](http://dentedreality.com.au/2011/03/12/chexees-feet-are-small/)

The one on the left is her foot, in her shoe, inside my shoe.





* #[Austin](http://dentedreality.com.au/tags/austin/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[sxsw2011](http://dentedreality.com.au/tags/sxsw2011/)
* #[texas](http://dentedreality.com.au/tags/texas/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802099493/) [11:34 pm, March 12, 2011](http://dentedreality.com.au/2011/03/12/chexees-feet-are-small/ "11:34 pm") 
jQuery(document).ready(function(){
var gmap\_mff4821bd41efd374a44d54c320dca7e1 = {
positions : {
812 : new google.maps.LatLng( '30.267833', '-97.745667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mff4821bd41efd374a44d54c320dca7e1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mff4821bd41efd374a44d54c320dca7e1.positions ) {
gmap\_mff4821bd41efd374a44d54c320dca7e1.bounds.extend( gmap\_mff4821bd41efd374a44d54c320dca7e1.positions[m] );
}
// Render markers
for ( var m in gmap\_mff4821bd41efd374a44d54c320dca7e1.positions ) {
gmap\_mff4821bd41efd374a44d54c320dca7e1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mff4821bd41efd374a44d54c320dca7e1.map,
position : gmap\_mff4821bd41efd374a44d54c320dca7e1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mff4821bd41efd374a44d54c320dca7e1.map.setCenter( gmap\_mff4821bd41efd374a44d54c320dca7e1.positions[812] );
});
---
title: Spilled Blood
date: '2006-12-30T06:26:14+00:00'
format: image
service: flickr
tags:
- bleeder
- blood
- boxing
- fight
- mat
- muaythai
- phuket
- ring
- thaiboxing
- thailand
- thailand06
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349555781_5229a46306_o.jpg?resize=607%2C455
---

[![Spilled Blood](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2006/12/349555781_5229a46306_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2006/12/30/spilled-blood/) 
# [Spilled Blood](http://dentedreality.com.au/2006/12/30/spilled-blood/)

We had 2 bleeders in the fights that we saw (eye-brow only). Looks like they weren’t the first bleeders in this ring.





* #[bleeder](http://dentedreality.com.au/tags/bleeder/)
* #[blood](http://dentedreality.com.au/tags/blood/)
* #[boxing](http://dentedreality.com.au/tags/boxing/)
* #[fight](http://dentedreality.com.au/tags/fight/)
* #[mat](http://dentedreality.com.au/tags/mat/)
* #[muaythai](http://dentedreality.com.au/tags/muaythai/)
* #[phuket](http://dentedreality.com.au/tags/phuket/)
* #[ring](http://dentedreality.com.au/tags/ring/)
* #[thaiboxing](http://dentedreality.com.au/tags/thaiboxing/)
* #[thailand](http://dentedreality.com.au/tags/thailand/)
* #[thailand06](http://dentedreality.com.au/tags/thailand06/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/349555781/) [6:26 am, December 30, 2006](http://dentedreality.com.au/2006/12/30/spilled-blood/ "6:26 am") 
jQuery(document).ready(function(){
var gmap\_m4468b0d0f9d53c7abe13b7d288dc7477 = {
positions : {
224 : new google.maps.LatLng( '7.896794', '98.295879' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m4468b0d0f9d53c7abe13b7d288dc7477' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.positions ) {
gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.bounds.extend( gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.positions[m] );
}
// Render markers
for ( var m in gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.positions ) {
gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.map,
position : gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.map.setCenter( gmap\_m4468b0d0f9d53c7abe13b7d288dc7477.positions[224] );
});
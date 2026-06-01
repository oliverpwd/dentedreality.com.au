---
title: Yarrow
date: '2010-04-09T10:05:34+00:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
- yarrow
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516460330_2184a58277_o.jpg?resize=607%2C809
---

[![Yarrow](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516460330_2184a58277_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2010/04/09/yarrow/) 
# [Yarrow](http://dentedreality.com.au/2010/04/09/yarrow/)

As seen during our edible/medicinal plant walk.





* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)
* #[yarrow](http://dentedreality.com.au/tags/yarrow/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516460330/) [10:05 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/yarrow/ "10:05 am") 
jQuery(document).ready(function(){
var gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06 = {
positions : {
770 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.positions ) {
gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.bounds.extend( gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.positions[m] );
}
// Render markers
for ( var m in gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.positions ) {
gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.map,
position : gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.map.setCenter( gmap\_mf6e0b96e86f3ae0ab61c7d6175a03b06.positions[770] );
});
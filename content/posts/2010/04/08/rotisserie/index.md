---
title: Rotisserie
date: '2010-04-08T08:18:21+00:00'
format: image
service: flickr
tags:
- chicken
- rotisserie
- tombrown
- trackerschool
- tracking
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515811869_fe4dba5d59_o.jpg?resize=607%2C455
---

[![Rotisserie](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4515811869_fe4dba5d59_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/08/rotisserie/) 
# [Rotisserie](http://dentedreality.com.au/2010/04/08/rotisserie/)

Standard class, Tracker School.





* #[chicken](http://dentedreality.com.au/tags/chicken/)
* #[rotisserie](http://dentedreality.com.au/tags/rotisserie/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515811869/) [8:18 am, April 8, 2010](http://dentedreality.com.au/2010/04/08/rotisserie/ "8:18 am") 
jQuery(document).ready(function(){
var gmap\_m9bb586fc589084dd3e45460d39fce141 = {
positions : {
177 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9bb586fc589084dd3e45460d39fce141' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9bb586fc589084dd3e45460d39fce141.positions ) {
gmap\_m9bb586fc589084dd3e45460d39fce141.bounds.extend( gmap\_m9bb586fc589084dd3e45460d39fce141.positions[m] );
}
// Render markers
for ( var m in gmap\_m9bb586fc589084dd3e45460d39fce141.positions ) {
gmap\_m9bb586fc589084dd3e45460d39fce141.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9bb586fc589084dd3e45460d39fce141.map,
position : gmap\_m9bb586fc589084dd3e45460d39fce141.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9bb586fc589084dd3e45460d39fce141.map.setCenter( gmap\_m9bb586fc589084dd3e45460d39fce141.positions[177] );
});
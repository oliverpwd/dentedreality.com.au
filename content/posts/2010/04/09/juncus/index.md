---
title: Juncus
date: '2010-04-09T09:40:03+00:00'
format: image
service: flickr
tags:
- juncus
- tombrown
- trackerschool
- tracking
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516459654_f198736948_o.jpg?resize=607%2C455
---

[![Juncus](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516459654_f198736948_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/juncus/) 
# [Juncus](http://dentedreality.com.au/2010/04/09/juncus/)

As seen during our edible/medicinal plant walk.





* #[juncus](http://dentedreality.com.au/tags/juncus/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516459654/) [9:40 am, April 9, 2010](http://dentedreality.com.au/2010/04/09/juncus/ "9:40 am") 
jQuery(document).ready(function(){
var gmap\_m53297d903036bba931c79458a76eb46f = {
positions : {
855 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m53297d903036bba931c79458a76eb46f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m53297d903036bba931c79458a76eb46f.positions ) {
gmap\_m53297d903036bba931c79458a76eb46f.bounds.extend( gmap\_m53297d903036bba931c79458a76eb46f.positions[m] );
}
// Render markers
for ( var m in gmap\_m53297d903036bba931c79458a76eb46f.positions ) {
gmap\_m53297d903036bba931c79458a76eb46f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m53297d903036bba931c79458a76eb46f.map,
position : gmap\_m53297d903036bba931c79458a76eb46f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m53297d903036bba931c79458a76eb46f.map.setCenter( gmap\_m53297d903036bba931c79458a76eb46f.positions[855] );
});
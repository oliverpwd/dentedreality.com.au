---
title: Tree + Sky
date: '2010-03-13T09:48:03+00:00'
format: image
service: flickr
tags:
- blue
- silhouette
- sky
- sxsw
- tree
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/03/4515770471_3a289a5566_o.jpg?resize=607%2C809
---

[![Tree + Sky](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/03/4515770471_3a289a5566_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2010/03/13/tree-sky/) 
# [Tree + Sky](http://dentedreality.com.au/2010/03/13/tree-sky/)

Taken in Austin, TX during SXSW





* #[blue](http://dentedreality.com.au/tags/blue/)
* #[silhouette](http://dentedreality.com.au/tags/silhouette/)
* #[sky](http://dentedreality.com.au/tags/sky/)
* #[sxsw](http://dentedreality.com.au/tags/sxsw/)
* #[tree](http://dentedreality.com.au/tags/tree/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515770471/) [9:48 am, March 13, 2010](http://dentedreality.com.au/2010/03/13/tree-sky/ "9:48 am") 
jQuery(document).ready(function(){
var gmap\_m18df6c92bbc3bd4fd445e592f55aab0b = {
positions : {
7 : new google.maps.LatLng( '30.245333', '-97.778334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m18df6c92bbc3bd4fd445e592f55aab0b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.positions ) {
gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.bounds.extend( gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.positions[m] );
}
// Render markers
for ( var m in gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.positions ) {
gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.map,
position : gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.map.setCenter( gmap\_m18df6c92bbc3bd4fd445e592f55aab0b.positions[7] );
});
---
title: Bremer Bay
date: '2011-01-19T13:13:49+00:00'
format: image
service: flickr
tags:
- australia
- bremer
- bremerbay
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434787446_8f29622727_o.jpg?resize=607%2C452
---

[![Bremer Bay](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2011/01/5434787446_8f29622727_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/01/19/bremer-bay-27/) 
# [Bremer Bay](http://dentedreality.com.au/2011/01/19/bremer-bay-27/)





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[bremer](http://dentedreality.com.au/tags/bremer/)
* #[bremerbay](http://dentedreality.com.au/tags/bremerbay/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434787446/) [1:13 pm, January 19, 2011](http://dentedreality.com.au/2011/01/19/bremer-bay-27/ "1:13 pm") 
jQuery(document).ready(function(){
var gmap\_mee306cf6e063416c9fd81acdbc04f319 = {
positions : {
835 : new google.maps.LatLng( '-34.394', '119.399666' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mee306cf6e063416c9fd81acdbc04f319' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mee306cf6e063416c9fd81acdbc04f319.positions ) {
gmap\_mee306cf6e063416c9fd81acdbc04f319.bounds.extend( gmap\_mee306cf6e063416c9fd81acdbc04f319.positions[m] );
}
// Render markers
for ( var m in gmap\_mee306cf6e063416c9fd81acdbc04f319.positions ) {
gmap\_mee306cf6e063416c9fd81acdbc04f319.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mee306cf6e063416c9fd81acdbc04f319.map,
position : gmap\_mee306cf6e063416c9fd81acdbc04f319.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mee306cf6e063416c9fd81acdbc04f319.map.setCenter( gmap\_mee306cf6e063416c9fd81acdbc04f319.positions[835] );
});
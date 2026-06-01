---
title: Republica Dominica
date: '2013-12-25T10:02:18+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924679874_8fed11d210_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924679874_8fed11d210_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/25/republica-dominica-21/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/25/republica-dominica-21/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924679874/) [10:02 am, December 25, 2013](http://dentedreality.com.au/2013/12/25/republica-dominica-21/ "10:02 am") 
jQuery(document).ready(function(){
var gmap\_m106a6fde5830203c543ff363e57cbf25 = {
positions : {
812 : new google.maps.LatLng( '19.285838', '-70.710695' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m106a6fde5830203c543ff363e57cbf25' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m106a6fde5830203c543ff363e57cbf25.positions ) {
gmap\_m106a6fde5830203c543ff363e57cbf25.bounds.extend( gmap\_m106a6fde5830203c543ff363e57cbf25.positions[m] );
}
// Render markers
for ( var m in gmap\_m106a6fde5830203c543ff363e57cbf25.positions ) {
gmap\_m106a6fde5830203c543ff363e57cbf25.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m106a6fde5830203c543ff363e57cbf25.map,
position : gmap\_m106a6fde5830203c543ff363e57cbf25.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m106a6fde5830203c543ff363e57cbf25.map.setCenter( gmap\_m106a6fde5830203c543ff363e57cbf25.positions[812] );
});
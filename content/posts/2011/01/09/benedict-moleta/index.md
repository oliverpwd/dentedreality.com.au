---
title: Benedict Moleta
date: '2011-01-09T15:54:34-07:00'
format: image
service: flickr
latitude: '-31.948834'
longitude: '115.8565'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185955/5434107147_3cf3c32181_o.jpg
---

[![Benedict Moleta](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185955/5434107147_3cf3c32181_o.jpg)](https://dentedreality.com.au/2011/01/09/benedict-moleta/) 
# [Benedict Moleta](https://dentedreality.com.au/2011/01/09/benedict-moleta/)

[![Benedict Moleta](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2011/01/14185955/5434107147_3cf3c32181_o.jpg)](http://www.flickr.com/photos/borkazoid/5434107147/)

-31.948834115.8565




Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434107147/) [3:54 pm, January 9, 2011](https://dentedreality.com.au/2011/01/09/benedict-moleta/ "3:54 pm") 
jQuery(document).ready(function(){
var gmap\_m9f4740d86c2b297b68a38de9d82229b9 = {
positions : {
904 : new google.maps.LatLng( '-31.948834', '115.8565' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m9f4740d86c2b297b68a38de9d82229b9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m9f4740d86c2b297b68a38de9d82229b9.positions ) {
gmap\_m9f4740d86c2b297b68a38de9d82229b9.bounds.extend( gmap\_m9f4740d86c2b297b68a38de9d82229b9.positions[m] );
}
// Render markers
for ( var m in gmap\_m9f4740d86c2b297b68a38de9d82229b9.positions ) {
gmap\_m9f4740d86c2b297b68a38de9d82229b9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m9f4740d86c2b297b68a38de9d82229b9.map,
position : gmap\_m9f4740d86c2b297b68a38de9d82229b9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m9f4740d86c2b297b68a38de9d82229b9.map.setCenter( gmap\_m9f4740d86c2b297b68a38de9d82229b9.positions[904] );
});
---
title: ''
date: '2013-11-18T01:15:29+00:00'
format: image
tags:
- photo
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/70a13d8e501011e3adcc12f8d832854b_8.jpg?resize=640%2C640
---

[![Epic light show. Trans-Siberian Orchestra.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/70a13d8e501011e3adcc12f8d832854b_8.jpg?resize=640%2C640)](http://dentedreality.com.au/2013/11/18/epic-light-show-trans-siberian-orchestra/) 

Epic light show. Trans-Siberian Orchestra.





* #[photo](http://dentedreality.com.au/tags/photo/)

Posted on [Instagram](http://instagram.com/p/g2AjjkimDH/) [1:15 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/epic-light-show-trans-siberian-orchestra/ "1:15 am") 
jQuery(document).ready(function(){
var gmap\_mca1cf882ce4339fbf318d7c6a1500d58 = {
positions : {
248 : new google.maps.LatLng( '39.748773781', '-105.007839203' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mca1cf882ce4339fbf318d7c6a1500d58' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mca1cf882ce4339fbf318d7c6a1500d58.positions ) {
gmap\_mca1cf882ce4339fbf318d7c6a1500d58.bounds.extend( gmap\_mca1cf882ce4339fbf318d7c6a1500d58.positions[m] );
}
// Render markers
for ( var m in gmap\_mca1cf882ce4339fbf318d7c6a1500d58.positions ) {
gmap\_mca1cf882ce4339fbf318d7c6a1500d58.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mca1cf882ce4339fbf318d7c6a1500d58.map,
position : gmap\_mca1cf882ce4339fbf318d7c6a1500d58.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mca1cf882ce4339fbf318d7c6a1500d58.map.setCenter( gmap\_mca1cf882ce4339fbf318d7c6a1500d58.positions[248] );
});
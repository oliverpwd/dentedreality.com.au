---
title: BAM
date: '2014-01-18T15:37:10+00:00'
format: image
service: flickr
tags:
- bam
- brooklyn
- newyork
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13927390714_c13cab7893_o.jpg?resize=607%2C455
---

[![BAM](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/01/13927390714_c13cab7893_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/01/18/bam-2/) 
# [BAM](http://dentedreality.com.au/2014/01/18/bam-2/)





* #[bam](http://dentedreality.com.au/tags/bam/)
* #[brooklyn](http://dentedreality.com.au/tags/brooklyn/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13927390714/) [3:37 pm, January 18, 2014](http://dentedreality.com.au/2014/01/18/bam-2/ "3:37 pm") 
jQuery(document).ready(function(){
var gmap\_m0c4008deed030a92c10529f9a6e53ec8 = {
positions : {
948 : new google.maps.LatLng( '40.686977', '-73.977753' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0c4008deed030a92c10529f9a6e53ec8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0c4008deed030a92c10529f9a6e53ec8.positions ) {
gmap\_m0c4008deed030a92c10529f9a6e53ec8.bounds.extend( gmap\_m0c4008deed030a92c10529f9a6e53ec8.positions[m] );
}
// Render markers
for ( var m in gmap\_m0c4008deed030a92c10529f9a6e53ec8.positions ) {
gmap\_m0c4008deed030a92c10529f9a6e53ec8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0c4008deed030a92c10529f9a6e53ec8.map,
position : gmap\_m0c4008deed030a92c10529f9a6e53ec8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0c4008deed030a92c10529f9a6e53ec8.map.setCenter( gmap\_m0c4008deed030a92c10529f9a6e53ec8.positions[948] );
});
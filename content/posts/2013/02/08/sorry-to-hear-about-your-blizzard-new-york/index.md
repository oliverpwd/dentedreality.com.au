---
title: Sorry to hear about your blizzard New York
date: '2013-02-08T06:47:17-07:00'
format: image
service: flickr
tags:
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
latitude: '37.756333'
longitude: '-122.418667'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8456769784_a2f33f2aff_o.jpg
---

[![Sorry to hear about your blizzard New York](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8456769784_a2f33f2aff_o.jpg)](https://dentedreality.com.au/2013/02/08/sorry-to-hear-about-your-blizzard-new-york/) 
# [Sorry to hear about your blizzard New York](https://dentedreality.com.au/2013/02/08/sorry-to-hear-about-your-blizzard-new-york/)

[![Sorry to hear about your blizzard New York](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8456769784_a2f33f2aff_o.jpg)](http://www.flickr.com/photos/borkazoid/8456769784/)

37.756333-122.418667




* #[flickriosapp:filter=nofilter](https://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8456769784/) [6:47 am, February 8, 2013](https://dentedreality.com.au/2013/02/08/sorry-to-hear-about-your-blizzard-new-york/ "6:47 am") 
jQuery(document).ready(function(){
var gmap\_md57720fec6e27061d6a26b8f930a58a2 = {
positions : {
818 : new google.maps.LatLng( '37.756333', '-122.418667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md57720fec6e27061d6a26b8f930a58a2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md57720fec6e27061d6a26b8f930a58a2.positions ) {
gmap\_md57720fec6e27061d6a26b8f930a58a2.bounds.extend( gmap\_md57720fec6e27061d6a26b8f930a58a2.positions[m] );
}
// Render markers
for ( var m in gmap\_md57720fec6e27061d6a26b8f930a58a2.positions ) {
gmap\_md57720fec6e27061d6a26b8f930a58a2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md57720fec6e27061d6a26b8f930a58a2.map,
position : gmap\_md57720fec6e27061d6a26b8f930a58a2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md57720fec6e27061d6a26b8f930a58a2.map.setCenter( gmap\_md57720fec6e27061d6a26b8f930a58a2.positions[818] );
});
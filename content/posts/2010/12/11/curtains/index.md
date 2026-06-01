---
title: Curtains
date: '2010-12-11T15:38:50-06:00'
format: image
service: flickr
tags:
- curtains
- party
- red
latitude: '37.419999'
longitude: '-122.211667'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/12/14185913/5434640814_133a11fd23_o.jpg
---

[![Curtains](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/12/14185913/5434640814_133a11fd23_o.jpg)](https://dentedreality.com.au/2010/12/11/curtains/) 
# [Curtains](https://dentedreality.com.au/2010/12/11/curtains/)

[![Curtains](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/12/14185913/5434640814_133a11fd23_o.jpg)](http://www.flickr.com/photos/borkazoid/5434640814/)

37.419999-122.211667




* #[curtains](https://dentedreality.com.au/tags/curtains/)
* #[party](https://dentedreality.com.au/tags/party/)
* #[red](https://dentedreality.com.au/tags/red/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5434640814/) [3:38 pm, December 11, 2010](https://dentedreality.com.au/2010/12/11/curtains/ "3:38 pm") 
jQuery(document).ready(function(){
var gmap\_m068881589552ee4cd53484c87cb59519 = {
positions : {
655 : new google.maps.LatLng( '37.419999', '-122.211667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m068881589552ee4cd53484c87cb59519' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m068881589552ee4cd53484c87cb59519.positions ) {
gmap\_m068881589552ee4cd53484c87cb59519.bounds.extend( gmap\_m068881589552ee4cd53484c87cb59519.positions[m] );
}
// Render markers
for ( var m in gmap\_m068881589552ee4cd53484c87cb59519.positions ) {
gmap\_m068881589552ee4cd53484c87cb59519.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m068881589552ee4cd53484c87cb59519.map,
position : gmap\_m068881589552ee4cd53484c87cb59519.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m068881589552ee4cd53484c87cb59519.map.setCenter( gmap\_m068881589552ee4cd53484c87cb59519.positions[655] );
});
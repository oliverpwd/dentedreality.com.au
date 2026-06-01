---
title: Yerba Buena
date: '2010-04-09T11:40:08-06:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
- yerbabuena
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4516467882_5b8e85c34e_o-768x1024.jpg
---

[![Yerba Buena](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4516467882_5b8e85c34e_o-768x1024.jpg)](https://dentedreality.com.au/2010/04/09/yerba-buena/) 
# [Yerba Buena](https://dentedreality.com.au/2010/04/09/yerba-buena/)

[![Yerba Buena](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4516467882_5b8e85c34e_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4516467882/)

As seen during our edible/medicinal plant walk.

37.177141-122.116744




* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)
* #[yerbabuena](https://dentedreality.com.au/tags/yerbabuena/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516467882/) [11:40 am, April 9, 2010](https://dentedreality.com.au/2010/04/09/yerba-buena/ "11:40 am") 
jQuery(document).ready(function(){
var gmap\_ma0069b2d6898fe6490c956786296e1f1 = {
positions : {
830 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma0069b2d6898fe6490c956786296e1f1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma0069b2d6898fe6490c956786296e1f1.positions ) {
gmap\_ma0069b2d6898fe6490c956786296e1f1.bounds.extend( gmap\_ma0069b2d6898fe6490c956786296e1f1.positions[m] );
}
// Render markers
for ( var m in gmap\_ma0069b2d6898fe6490c956786296e1f1.positions ) {
gmap\_ma0069b2d6898fe6490c956786296e1f1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma0069b2d6898fe6490c956786296e1f1.map,
position : gmap\_ma0069b2d6898fe6490c956786296e1f1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma0069b2d6898fe6490c956786296e1f1.map.setCenter( gmap\_ma0069b2d6898fe6490c956786296e1f1.positions[830] );
});
---
title: Tracker School
date: '2010-04-09T11:44:55-06:00'
format: image
service: flickr
tags:
- tombrown
- trackerschool
- tracking
latitude: '37.177141'
longitude: '-122.116744'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515833651_e8be7665b6_o-768x1024.jpg
---

[![Tracker School](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515833651_e8be7665b6_o-768x1024.jpg)](https://dentedreality.com.au/2010/04/09/tracker-school-2/) 
# [Tracker School](https://dentedreality.com.au/2010/04/09/tracker-school-2/)

[![Tracker School](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2010/04/14185650/4515833651_e8be7665b6_o-768x1024.jpg)](http://www.flickr.com/photos/borkazoid/4515833651/)

As seen during our edible/medicinal plant walk.

37.177141-122.116744




* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4515833651/) [11:44 am, April 9, 2010](https://dentedreality.com.au/2010/04/09/tracker-school-2/ "11:44 am") 
jQuery(document).ready(function(){
var gmap\_m5fa4d0a080b11cb63cbfc053621e9363 = {
positions : {
925 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5fa4d0a080b11cb63cbfc053621e9363' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5fa4d0a080b11cb63cbfc053621e9363.positions ) {
gmap\_m5fa4d0a080b11cb63cbfc053621e9363.bounds.extend( gmap\_m5fa4d0a080b11cb63cbfc053621e9363.positions[m] );
}
// Render markers
for ( var m in gmap\_m5fa4d0a080b11cb63cbfc053621e9363.positions ) {
gmap\_m5fa4d0a080b11cb63cbfc053621e9363.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5fa4d0a080b11cb63cbfc053621e9363.map,
position : gmap\_m5fa4d0a080b11cb63cbfc053621e9363.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5fa4d0a080b11cb63cbfc053621e9363.map.setCenter( gmap\_m5fa4d0a080b11cb63cbfc053621e9363.positions[925] );
});
---
title: Fish in the Coals
date: '2010-04-09T15:44:14+00:00'
format: image
service: flickr
tags:
- coals
- fire
- fish
- tombrown
- trackerschool
- tracking
image: http://dentedreality.com.au/wp-content/uploads/2010/04/4516473006_492b32f3dd_o-1024x768.jpg
---

[![Fish in the Coals](http://dentedreality.com.au/wp-content/uploads/2010/04/4516473006_492b32f3dd_o-1024x768.jpg)](https://dentedreality.com.au/2010/04/09/fish-in-the-coals/) 
# [Fish in the Coals](https://dentedreality.com.au/2010/04/09/fish-in-the-coals/)

[![Fish in the Coals](http://dentedreality.com.au/wp-content/uploads/2010/04/4516473006_492b32f3dd_o-1024x768.jpg)](http://www.flickr.com/photos/borkazoid/4516473006/)

Standard class, Tracker School.





* #[coals](https://dentedreality.com.au/tags/coals/)
* #[fire](https://dentedreality.com.au/tags/fire/)
* #[fish](https://dentedreality.com.au/tags/fish/)
* #[tombrown](https://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](https://dentedreality.com.au/tags/trackerschool/)
* #[tracking](https://dentedreality.com.au/tags/tracking/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516473006/) [3:44 pm, April 9, 2010](https://dentedreality.com.au/2010/04/09/fish-in-the-coals/ "3:44 pm") 
jQuery(document).ready(function(){
var gmap\_maf719b135698252b375b58eedfe7f3cd = {
positions : {
693 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf719b135698252b375b58eedfe7f3cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf719b135698252b375b58eedfe7f3cd.positions ) {
gmap\_maf719b135698252b375b58eedfe7f3cd.bounds.extend( gmap\_maf719b135698252b375b58eedfe7f3cd.positions[m] );
}
// Render markers
for ( var m in gmap\_maf719b135698252b375b58eedfe7f3cd.positions ) {
gmap\_maf719b135698252b375b58eedfe7f3cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf719b135698252b375b58eedfe7f3cd.map,
position : gmap\_maf719b135698252b375b58eedfe7f3cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf719b135698252b375b58eedfe7f3cd.map.setCenter( gmap\_maf719b135698252b375b58eedfe7f3cd.positions[693] );
});
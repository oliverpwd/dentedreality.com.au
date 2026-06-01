---
title: ''
date: '2018-04-18T20:37:56+00:00'
format: image
service: instagram
tags:
- colorado
- downhill
- enduro
- mtb
- specialized
image: https://dentedreality.com.au/wp-content/uploads/2018/04/30856280_1005251726294399_6102754193783652352_n.jpg
---

[![Mid-week rides FTW @kchoffman  @michaelarestad #specialized #mtb #enduro #colorado #downhill](https://dentedreality.com.au/wp-content/uploads/2018/04/30856280_1005251726294399_6102754193783652352_n.jpg)](https://dentedreality.com.au/2018/04/18/mid-week-rides-ftw-kchoffman-michaelarestad-specialized-mtb-enduro-colorado-downhill/) 

[![Mid-week rides FTW @kchoffman  @michaelarestad #specialized #mtb #enduro #colorado #downhill](https://dentedreality.com.au/wp-content/uploads/2018/04/30856280_1005251726294399_6102754193783652352_n.jpg)](https://www.instagram.com/p/BhvEvDzljwI/)

Mid-week rides FTW @kchoffman @michaelarestad #specialized #mtb #enduro #colorado #downhill





* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[downhill](https://dentedreality.com.au/tags/downhill/)
* #[enduro](https://dentedreality.com.au/tags/enduro/)
* #[mtb](https://dentedreality.com.au/tags/mtb/)
* #[specialized](https://dentedreality.com.au/tags/specialized/)

Posted on [Instagram](https://www.instagram.com/p/BhvEvDzljwI/) [8:37 pm, April 18, 2018](https://dentedreality.com.au/2018/04/18/mid-week-rides-ftw-kchoffman-michaelarestad-specialized-mtb-enduro-colorado-downhill/ "8:37 pm") 
jQuery(document).ready(function(){
var gmap\_m510a6a9bbadd4edfd5537889301498e8 = {
positions : {
903 : new google.maps.LatLng( '39.79784', '-105.24801' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m510a6a9bbadd4edfd5537889301498e8' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m510a6a9bbadd4edfd5537889301498e8.positions ) {
gmap\_m510a6a9bbadd4edfd5537889301498e8.bounds.extend( gmap\_m510a6a9bbadd4edfd5537889301498e8.positions[m] );
}
// Render markers
for ( var m in gmap\_m510a6a9bbadd4edfd5537889301498e8.positions ) {
gmap\_m510a6a9bbadd4edfd5537889301498e8.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m510a6a9bbadd4edfd5537889301498e8.map,
position : gmap\_m510a6a9bbadd4edfd5537889301498e8.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m510a6a9bbadd4edfd5537889301498e8.map.setCenter( gmap\_m510a6a9bbadd4edfd5537889301498e8.positions[903] );
});
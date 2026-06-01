---
title: DC For The Weekend
date: '2012-07-01T09:36:00-06:00'
format: image
service: flickr
tags:
- beau
- beaulebens
- erika
- me
- washingtondc
latitude: '38.942666'
longitude: '-77.084'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/07/14190638/7911191902_7c8fb9e16e_o.jpg
---

[![DC For The Weekend](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/07/14190638/7911191902_7c8fb9e16e_o.jpg)](https://dentedreality.com.au/2012/07/01/dc-for-the-weekend/) 
# [DC For The Weekend](https://dentedreality.com.au/2012/07/01/dc-for-the-weekend/)

[![DC For The Weekend](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/07/14190638/7911191902_7c8fb9e16e_o.jpg)](http://www.flickr.com/photos/borkazoid/7911191902/)

38.942666-77.084




* #[beau](https://dentedreality.com.au/tags/beau/)
* #[beaulebens](https://dentedreality.com.au/tags/beaulebens/)
* #[erika](https://dentedreality.com.au/tags/erika/)
* #[me](https://dentedreality.com.au/tags/me/)
* #[washingtondc](https://dentedreality.com.au/tags/washingtondc/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7911191902/) [9:36 am, July 1, 2012](https://dentedreality.com.au/2012/07/01/dc-for-the-weekend/ "9:36 am") 
jQuery(document).ready(function(){
var gmap\_maa13c05ed7185acba9e24770c2d43fc5 = {
positions : {
652 : new google.maps.LatLng( '38.942666', '-77.084' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maa13c05ed7185acba9e24770c2d43fc5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maa13c05ed7185acba9e24770c2d43fc5.positions ) {
gmap\_maa13c05ed7185acba9e24770c2d43fc5.bounds.extend( gmap\_maa13c05ed7185acba9e24770c2d43fc5.positions[m] );
}
// Render markers
for ( var m in gmap\_maa13c05ed7185acba9e24770c2d43fc5.positions ) {
gmap\_maa13c05ed7185acba9e24770c2d43fc5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maa13c05ed7185acba9e24770c2d43fc5.map,
position : gmap\_maa13c05ed7185acba9e24770c2d43fc5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maa13c05ed7185acba9e24770c2d43fc5.map.setCenter( gmap\_maa13c05ed7185acba9e24770c2d43fc5.positions[652] );
});
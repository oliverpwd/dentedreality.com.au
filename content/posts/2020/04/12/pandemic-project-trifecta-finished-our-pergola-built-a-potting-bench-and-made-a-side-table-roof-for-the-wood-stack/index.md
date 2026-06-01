---
title: ''
date: '2020-04-12T13:45:27-06:00'
format: image
service: instagram
latitude: '39.7391'
longitude: '-104.9836'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/04/12142507/92832454_926727464418818_6468433695243940262_n.jpg
---

[![Pandemic Project Trifecta. Finished our pergola, built a potting bench, and made a side table/roof for the wood stack.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/04/12142507/92832454_926727464418818_6468433695243940262_n.jpg)](https://dentedreality.com.au/2020/04/12/pandemic-project-trifecta-finished-our-pergola-built-a-potting-bench-and-made-a-side-table-roof-for-the-wood-stack/) 

![Pandemic Project Trifecta. Finished our pergola, built a potting bench, and made a side table/roof for the wood stack.](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2020/04/12142507/92832454_926727464418818_6468433695243940262_n.jpg)

[![Pandemic Project Trifecta. Finished our pergola, built a potting bench, and made a side table/roof for the wood stack.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/92832454_926727464418818_6468433695243940262_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=T5qgNW9f9EQAX-gKJN2&oh=b4644d1bbb2a7f63f29c7568760a7d06&oe=5EBE33B0)![Pandemic Project Trifecta. Finished our pergola, built a potting bench, and made a side table/roof for the wood stack.](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/92832454_926727464418818_6468433695243940262_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_ohc=T5qgNW9f9EQAX-gKJN2&oh=b4644d1bbb2a7f63f29c7568760a7d06&oe=5EBE33B0)](https://www.instagram.com/p/B-5J2UBpuVx/)

Pandemic Project Trifecta. Finished our pergola, built a potting bench, and made a side table/roof for the wood stack.

39.7391-104.9836




Posted on [Instagram](https://www.instagram.com/p/B-5J2UBpuVx/) [1:45 pm, April 12, 2020](https://dentedreality.com.au/2020/04/12/pandemic-project-trifecta-finished-our-pergola-built-a-potting-bench-and-made-a-side-table-roof-for-the-wood-stack/ "1:45 pm") 
jQuery(document).ready(function(){
var gmap\_me34f547c967ccbfd39f73d3ecb41b2ea = {
positions : {
834 : new google.maps.LatLng( '39.7391', '-104.9836' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_me34f547c967ccbfd39f73d3ecb41b2ea' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.positions ) {
gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.bounds.extend( gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.positions[m] );
}
// Render markers
for ( var m in gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.positions ) {
gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.map,
position : gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.map.setCenter( gmap\_me34f547c967ccbfd39f73d3ecb41b2ea.positions[834] );
});
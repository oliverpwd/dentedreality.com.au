---
title: ''
date: '2017-07-24T22:53:43+00:00'
format: image
service: instagram
tags:
- camping
- canoecamping
- colorado
- river
- train
- unionpacific
- utah
image: https://dentedreality.com.au/wp-content/uploads/2017/07/20225371_120087598622183_9027016581737086976_n.jpg
---

[![Union Pacific. Toot, toot. #train #unionpacific #colorado #canoecamping #camping #river #utah](https://dentedreality.com.au/wp-content/uploads/2017/07/20225371_120087598622183_9027016581737086976_n.jpg)](https://dentedreality.com.au/2017/07/24/union-pacific-toot-toot-train-unionpacific-colorado-canoecamping-camping-river-utah/) 

[![Union Pacific. Toot, toot. #train #unionpacific #colorado #canoecamping #camping #river #utah](https://dentedreality.com.au/wp-content/uploads/2017/07/20225371_120087598622183_9027016581737086976_n.jpg)](https://www.instagram.com/p/BW9PPGcBvD-/)

Union Pacific. Toot, toot. #train #unionpacific #colorado #canoecamping #camping #river #utah





* #[camping](https://dentedreality.com.au/tags/camping/)
* #[canoecamping](https://dentedreality.com.au/tags/canoecamping/)
* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[river](https://dentedreality.com.au/tags/river/)
* #[train](https://dentedreality.com.au/tags/train/)
* #[unionpacific](https://dentedreality.com.au/tags/unionpacific/)
* #[utah](https://dentedreality.com.au/tags/utah/)

Posted on [Instagram](https://www.instagram.com/p/BW9PPGcBvD-/) [10:53 pm, July 24, 2017](https://dentedreality.com.au/2017/07/24/union-pacific-toot-toot-train-unionpacific-colorado-canoecamping-camping-river-utah/ "10:53 pm") 
jQuery(document).ready(function(){
var gmap\_m7f4fffe718ac166a72a7308e8d4cff1c = {
positions : {
392 : new google.maps.LatLng( '39.862997046629', '-105.08438988874' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7f4fffe718ac166a72a7308e8d4cff1c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.positions ) {
gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.bounds.extend( gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.positions[m] );
}
// Render markers
for ( var m in gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.positions ) {
gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.map,
position : gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.map.setCenter( gmap\_m7f4fffe718ac166a72a7308e8d4cff1c.positions[392] );
});
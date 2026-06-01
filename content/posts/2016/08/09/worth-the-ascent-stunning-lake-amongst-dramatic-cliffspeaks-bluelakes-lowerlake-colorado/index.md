---
title: ''
date: '2016-08-09T12:39:38-06:00'
format: image
service: instagram
tags:
- bluelakes
- colorado
- lowerlake
latitude: '38.0020257'
longitude: '-107.8168177'
image: https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13731111_1758812484369918_1150758294_n.jpg?fit=640%2C640
---

[![Worth the ascent. Stunning lake amongst dramatic cliffs/peaks. #bluelakes #lowerlake #colorado](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13731111_1758812484369918_1150758294_n.jpg?fit=640%2C640)](https://dentedreality.com.au/2016/08/09/worth-the-ascent-stunning-lake-amongst-dramatic-cliffspeaks-bluelakes-lowerlake-colorado/) 

[![Worth the ascent. Stunning lake amongst dramatic cliffs/peaks. #bluelakes #lowerlake #colorado](https://i2.wp.com/dentedreality.com.au/wp-content/uploads/2016/08/13731111_1758812484369918_1150758294_n.jpg?fit=640%2C640)](https://www.instagram.com/p/BI5fiBsgwjB/)

Worth the ascent. Stunning lake amongst dramatic cliffs/peaks. #bluelakes #lowerlake #colorado

38.0020257-107.8168177




* #[bluelakes](https://dentedreality.com.au/tags/bluelakes/)
* #[colorado](https://dentedreality.com.au/tags/colorado/)
* #[lowerlake](https://dentedreality.com.au/tags/lowerlake/)

Posted on [Instagram](https://www.instagram.com/p/BI5fiBsgwjB/) [12:39 pm, August 9, 2016](https://dentedreality.com.au/2016/08/09/worth-the-ascent-stunning-lake-amongst-dramatic-cliffspeaks-bluelakes-lowerlake-colorado/ "12:39 pm") 
jQuery(document).ready(function(){
var gmap\_m2697cd662f1afa1d5957da9ad73501cd = {
positions : {
258 : new google.maps.LatLng( '38.002025736531', '-107.816817714' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2697cd662f1afa1d5957da9ad73501cd' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2697cd662f1afa1d5957da9ad73501cd.positions ) {
gmap\_m2697cd662f1afa1d5957da9ad73501cd.bounds.extend( gmap\_m2697cd662f1afa1d5957da9ad73501cd.positions[m] );
}
// Render markers
for ( var m in gmap\_m2697cd662f1afa1d5957da9ad73501cd.positions ) {
gmap\_m2697cd662f1afa1d5957da9ad73501cd.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2697cd662f1afa1d5957da9ad73501cd.map,
position : gmap\_m2697cd662f1afa1d5957da9ad73501cd.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2697cd662f1afa1d5957da9ad73501cd.map.setCenter( gmap\_m2697cd662f1afa1d5957da9ad73501cd.positions[258] );
});
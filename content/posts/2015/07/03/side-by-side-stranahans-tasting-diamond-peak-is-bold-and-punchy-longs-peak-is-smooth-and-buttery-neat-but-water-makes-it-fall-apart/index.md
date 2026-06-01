---
title: ''
date: '2015-07-03T19:53:34+00:00'
format: image
service: instagram
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/07/11351506_380803518783961_788716839_n.jpg?resize=640%2C640
---

[![Side by side @stranahans tasting. Diamond Peak is bold and punchy. Long's Peak is smooth and buttery neat, but water makes it fall apart.](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2015/07/11351506_380803518783961_788716839_n.jpg?resize=640%2C640)](http://dentedreality.com.au/2015/07/03/side-by-side-stranahans-tasting-diamond-peak-is-bold-and-punchy-longs-peak-is-smooth-and-buttery-neat-but-water-makes-it-fall-apart/) 

Side by side @stranahans tasting. Diamond Peak is bold and punchy. Long’s Peak is smooth and buttery neat, but water makes it fall apart.





Posted on [Instagram](https://instagram.com/p/4sk1pCimG9/) [7:53 pm, July 3, 2015](http://dentedreality.com.au/2015/07/03/side-by-side-stranahans-tasting-diamond-peak-is-bold-and-punchy-longs-peak-is-smooth-and-buttery-neat-but-water-makes-it-fall-apart/ "7:53 pm") 
jQuery(document).ready(function(){
var gmap\_m14d94e0f1f819c770f1758298366d77e = {
positions : {
958 : new google.maps.LatLng( '39.759955', '-104.96933' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m14d94e0f1f819c770f1758298366d77e' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m14d94e0f1f819c770f1758298366d77e.positions ) {
gmap\_m14d94e0f1f819c770f1758298366d77e.bounds.extend( gmap\_m14d94e0f1f819c770f1758298366d77e.positions[m] );
}
// Render markers
for ( var m in gmap\_m14d94e0f1f819c770f1758298366d77e.positions ) {
gmap\_m14d94e0f1f819c770f1758298366d77e.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m14d94e0f1f819c770f1758298366d77e.map,
position : gmap\_m14d94e0f1f819c770f1758298366d77e.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m14d94e0f1f819c770f1758298366d77e.map.setCenter( gmap\_m14d94e0f1f819c770f1758298366d77e.positions[958] );
});
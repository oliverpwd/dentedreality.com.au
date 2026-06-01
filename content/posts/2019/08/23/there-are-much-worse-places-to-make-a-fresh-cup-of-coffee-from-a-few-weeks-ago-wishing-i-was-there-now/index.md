---
title: ''
date: '2019-08-23T16:09:40-06:00'
format: image
service: instagram
latitude: '39.4091364'
longitude: '-105.5007863'
image: https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23162457/67200240_2475667995843942_1831190326978762121_n.jpg?fit=640%2C640&ssl=1
---

[![There are much worse places to make a fresh cup of coffee. (from a few weeks ago, wishing I was there now)](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23162457/67200240_2475667995843942_1831190326978762121_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/08/23/there-are-much-worse-places-to-make-a-fresh-cup-of-coffee-from-a-few-weeks-ago-wishing-i-was-there-now/) 

[![There are much worse places to make a fresh cup of coffee. (from a few weeks ago, wishing I was there now)](https://i1.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/08/23162457/67200240_2475667995843942_1831190326978762121_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B1hdItbprar/)

There are much worse places to make a fresh cup of coffee. (from a few weeks ago, wishing I was there now)

39.4091364-105.5007863




Posted on [Instagram](https://www.instagram.com/p/B1hdItbprar/) [4:09 pm, August 23, 2019](https://dentedreality.com.au/2019/08/23/there-are-much-worse-places-to-make-a-fresh-cup-of-coffee-from-a-few-weeks-ago-wishing-i-was-there-now/ "4:09 pm") 
jQuery(document).ready(function(){
var gmap\_mf476f9b82b770f10fc8d19253598f79f = {
positions : {
119 : new google.maps.LatLng( '39.4091364', '-105.5007863' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf476f9b82b770f10fc8d19253598f79f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf476f9b82b770f10fc8d19253598f79f.positions ) {
gmap\_mf476f9b82b770f10fc8d19253598f79f.bounds.extend( gmap\_mf476f9b82b770f10fc8d19253598f79f.positions[m] );
}
// Render markers
for ( var m in gmap\_mf476f9b82b770f10fc8d19253598f79f.positions ) {
gmap\_mf476f9b82b770f10fc8d19253598f79f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf476f9b82b770f10fc8d19253598f79f.map,
position : gmap\_mf476f9b82b770f10fc8d19253598f79f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf476f9b82b770f10fc8d19253598f79f.map.setCenter( gmap\_mf476f9b82b770f10fc8d19253598f79f.positions[119] );
});
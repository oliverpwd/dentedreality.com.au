---
title: Lone Tree in the Dark
date: '2008-04-05T02:51:12-06:00'
format: image
service: flickr
tags:
- australia
- backlighting
- foresthillwinery
- renniewedding
- timswedding
- tree
- westernaustraliadenmark
latitude: '-34.983877'
longitude: '117.298278'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184651/2432616233_f100c6e720_o.jpg
---

[![Lone Tree in the Dark](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184651/2432616233_f100c6e720_o.jpg)](https://dentedreality.com.au/2008/04/05/lone-tree-in-the-dark/) 
# [Lone Tree in the Dark](https://dentedreality.com.au/2008/04/05/lone-tree-in-the-dark/)

[![Lone Tree in the Dark](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184651/2432616233_f100c6e720_o.jpg)](http://www.flickr.com/photos/borkazoid/2432616233/)

As viewed from the balcony at Forest-Hill Winery. I believe this was Tim’s idea – top work son!

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[backlighting](https://dentedreality.com.au/tags/backlighting/)
* #[foresthillwinery](https://dentedreality.com.au/tags/foresthillwinery/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[tree](https://dentedreality.com.au/tags/tree/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432616233/) [2:51 am, April 5, 2008](https://dentedreality.com.au/2008/04/05/lone-tree-in-the-dark/ "2:51 am") 
jQuery(document).ready(function(){
var gmap\_mfc7748ff370f3800f9d253271e940076 = {
positions : {
360 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mfc7748ff370f3800f9d253271e940076' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mfc7748ff370f3800f9d253271e940076.positions ) {
gmap\_mfc7748ff370f3800f9d253271e940076.bounds.extend( gmap\_mfc7748ff370f3800f9d253271e940076.positions[m] );
}
// Render markers
for ( var m in gmap\_mfc7748ff370f3800f9d253271e940076.positions ) {
gmap\_mfc7748ff370f3800f9d253271e940076.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mfc7748ff370f3800f9d253271e940076.map,
position : gmap\_mfc7748ff370f3800f9d253271e940076.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mfc7748ff370f3800f9d253271e940076.map.setCenter( gmap\_mfc7748ff370f3800f9d253271e940076.positions[360] );
});
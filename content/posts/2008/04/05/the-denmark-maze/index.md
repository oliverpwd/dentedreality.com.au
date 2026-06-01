---
title: The Denmark Maze
date: '2008-04-05T18:21:01-06:00'
format: image
service: flickr
tags:
- australia
- denmarkmaze
- maze
- renniewedding
- timswedding
- westernaustraliadenmark
latitude: '-34.983877'
longitude: '117.298278'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184653/2433437824_1388aa7d14_o.jpg
---

[![The Denmark Maze](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184653/2433437824_1388aa7d14_o.jpg)](https://dentedreality.com.au/2008/04/05/the-denmark-maze/) 
# [The Denmark Maze](https://dentedreality.com.au/2008/04/05/the-denmark-maze/)

[![The Denmark Maze](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2008/04/14184653/2433437824_1388aa7d14_o.jpg)](http://www.flickr.com/photos/borkazoid/2433437824/)

-34.983877117.298278




* #[australia](https://dentedreality.com.au/tags/australia/)
* #[denmarkmaze](https://dentedreality.com.au/tags/denmarkmaze/)
* #[maze](https://dentedreality.com.au/tags/maze/)
* #[renniewedding](https://dentedreality.com.au/tags/renniewedding/)
* #[timswedding](https://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](https://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433437824/) [6:21 pm, April 5, 2008](https://dentedreality.com.au/2008/04/05/the-denmark-maze/ "6:21 pm") 
jQuery(document).ready(function(){
var gmap\_m77b4a4cd74fa557ae835e924c3cbacc7 = {
positions : {
303 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m77b4a4cd74fa557ae835e924c3cbacc7' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.positions ) {
gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.bounds.extend( gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.positions[m] );
}
// Render markers
for ( var m in gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.positions ) {
gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.map,
position : gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.map.setCenter( gmap\_m77b4a4cd74fa557ae835e924c3cbacc7.positions[303] );
});
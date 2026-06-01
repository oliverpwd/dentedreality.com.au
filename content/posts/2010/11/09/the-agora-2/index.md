---
title: The Agora
date: '2010-11-09T08:54:57-07:00'
format: image
service: flickr
tags:
- agora
- Athens
- automattic
- greece
- teamsocial
latitude: '37.976833'
longitude: '23.722166'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14183411/5183790632_573e93832a_o.jpg
---

[![The Agora](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14183411/5183790632_573e93832a_o.jpg)](https://dentedreality.com.au/2010/11/09/the-agora-2/) 
# [The Agora](https://dentedreality.com.au/2010/11/09/the-agora-2/)

[![The Agora](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14183411/5183790632_573e93832a_o.jpg)](http://www.flickr.com/photos/borkazoid/5183790632/)

37.97683323.722166




* #[agora](https://dentedreality.com.au/tags/agora/)
* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183790632/) [8:54 am, November 9, 2010](https://dentedreality.com.au/2010/11/09/the-agora-2/ "8:54 am") 
jQuery(document).ready(function(){
var gmap\_m320f5fb31a4456578ac80fb3e9237dfe = {
positions : {
292 : new google.maps.LatLng( '37.976833', '23.722166' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m320f5fb31a4456578ac80fb3e9237dfe' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m320f5fb31a4456578ac80fb3e9237dfe.positions ) {
gmap\_m320f5fb31a4456578ac80fb3e9237dfe.bounds.extend( gmap\_m320f5fb31a4456578ac80fb3e9237dfe.positions[m] );
}
// Render markers
for ( var m in gmap\_m320f5fb31a4456578ac80fb3e9237dfe.positions ) {
gmap\_m320f5fb31a4456578ac80fb3e9237dfe.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m320f5fb31a4456578ac80fb3e9237dfe.map,
position : gmap\_m320f5fb31a4456578ac80fb3e9237dfe.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m320f5fb31a4456578ac80fb3e9237dfe.map.setCenter( gmap\_m320f5fb31a4456578ac80fb3e9237dfe.positions[292] );
});
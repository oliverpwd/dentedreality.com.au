---
title: Athens, Greece
date: '2010-11-09T09:08:11-06:00'
format: image
service: flickr
tags:
- Athens
- automattic
- greece
- teamsocial
latitude: '37.973666'
longitude: '23.726499'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183191733_76b49dc1c1_o.jpg
---

[![Athens, Greece](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183191733_76b49dc1c1_o.jpg)](https://dentedreality.com.au/2010/11/09/athens-greece-2/) 
# [Athens, Greece](https://dentedreality.com.au/2010/11/09/athens-greece-2/)

[![Athens, Greece](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2010/11/14185851/5183191733_76b49dc1c1_o.jpg)](http://www.flickr.com/photos/borkazoid/5183191733/)

37.97366623.726499




* #[Athens](https://dentedreality.com.au/tags/athens/)
* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[greece](https://dentedreality.com.au/tags/greece/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5183191733/) [9:08 am, November 9, 2010](https://dentedreality.com.au/2010/11/09/athens-greece-2/ "9:08 am") 
jQuery(document).ready(function(){
var gmap\_m8be0551f892b6a198930d730aad38b1a = {
positions : {
478 : new google.maps.LatLng( '37.973666', '23.726499' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8be0551f892b6a198930d730aad38b1a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8be0551f892b6a198930d730aad38b1a.positions ) {
gmap\_m8be0551f892b6a198930d730aad38b1a.bounds.extend( gmap\_m8be0551f892b6a198930d730aad38b1a.positions[m] );
}
// Render markers
for ( var m in gmap\_m8be0551f892b6a198930d730aad38b1a.positions ) {
gmap\_m8be0551f892b6a198930d730aad38b1a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8be0551f892b6a198930d730aad38b1a.map,
position : gmap\_m8be0551f892b6a198930d730aad38b1a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8be0551f892b6a198930d730aad38b1a.map.setCenter( gmap\_m8be0551f892b6a198930d730aad38b1a.positions[478] );
});
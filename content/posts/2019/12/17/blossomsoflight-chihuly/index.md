---
title: ''
date: '2019-12-17T07:48:13-07:00'
format: image
service: instagram
tags:
- blossomsoflight
latitude: '39.7320808'
longitude: '-104.9611041'
image: https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/17082501/79371661_130794338376598_4563723827637016425_n.jpg
---

[![#blossomsoflight Chihuly](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/17082501/79371661_130794338376598_4563723827637016425_n.jpg)](https://dentedreality.com.au/2019/12/17/blossomsoflight-chihuly/) 

![#blossomsoflight Chihuly](https://s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/12/17082501/79371661_130794338376598_4563723827637016425_n.jpg)

[![#blossomsoflight Chihuly](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/79371661_130794338376598_4563723827637016425_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=d0fd3d652ec1409b646c15b914ad18bf&oe=5EAF7A8D)![#blossomsoflight Chihuly](https://scontent.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/79371661_130794338376598_4563723827637016425_n.jpg?_nc_ht=scontent.cdninstagram.com&oh=d0fd3d652ec1409b646c15b914ad18bf&oe=5EAF7A8D)](https://www.instagram.com/p/B6LW0_kJgHB/)

#blossomsoflight Chihuly

39.7320808-104.9611041




* #[blossomsoflight](https://dentedreality.com.au/tags/blossomsoflight/)

Posted on [Instagram](https://www.instagram.com/p/B6LW0_kJgHB/) [7:48 am, December 17, 2019](https://dentedreality.com.au/2019/12/17/blossomsoflight-chihuly/ "7:48 am") 
jQuery(document).ready(function(){
var gmap\_m2bbab894c55bfc3f8dd938c78f4530c3 = {
positions : {
413 : new google.maps.LatLng( '39.7320808', '-104.9611041' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2bbab894c55bfc3f8dd938c78f4530c3' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.positions ) {
gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.bounds.extend( gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.positions[m] );
}
// Render markers
for ( var m in gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.positions ) {
gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.map,
position : gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.map.setCenter( gmap\_m2bbab894c55bfc3f8dd938c78f4530c3.positions[413] );
});
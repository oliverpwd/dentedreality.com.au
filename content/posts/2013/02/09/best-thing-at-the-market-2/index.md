---
title: Best Thing At The Market
date: '2013-02-09T08:01:43-07:00'
format: image
service: flickr
tags:
- flickriosapp:filter=nofilter
- uploaded:by=flickrmobile
latitude: '37.794999'
longitude: '-122.392334'
image: https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8458497947_e7daec4776_o.jpg
---

[![Best Thing At The Market](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8458497947_e7daec4776_o.jpg)](https://dentedreality.com.au/2013/02/09/best-thing-at-the-market-2/) 
# [Best Thing At The Market](https://dentedreality.com.au/2013/02/09/best-thing-at-the-market-2/)

[![Best Thing At The Market](https://dentedreality-content.s3.amazonaws.com/wp-content/uploads/2013/02/14190738/8458497947_e7daec4776_o.jpg)](http://www.flickr.com/photos/borkazoid/8458497947/)

@4505\_Meats cheeseburger.

37.794999-122.392334




* #[flickriosapp:filter=nofilter](https://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[uploaded:by=flickrmobile](https://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8458497947/) [8:01 am, February 9, 2013](https://dentedreality.com.au/2013/02/09/best-thing-at-the-market-2/ "8:01 am") 
jQuery(document).ready(function(){
var gmap\_m7669cae5badf5f6637b4bb246d82e97f = {
positions : {
588 : new google.maps.LatLng( '37.794999', '-122.392334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m7669cae5badf5f6637b4bb246d82e97f' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m7669cae5badf5f6637b4bb246d82e97f.positions ) {
gmap\_m7669cae5badf5f6637b4bb246d82e97f.bounds.extend( gmap\_m7669cae5badf5f6637b4bb246d82e97f.positions[m] );
}
// Render markers
for ( var m in gmap\_m7669cae5badf5f6637b4bb246d82e97f.positions ) {
gmap\_m7669cae5badf5f6637b4bb246d82e97f.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m7669cae5badf5f6637b4bb246d82e97f.map,
position : gmap\_m7669cae5badf5f6637b4bb246d82e97f.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m7669cae5badf5f6637b4bb246d82e97f.map.setCenter( gmap\_m7669cae5badf5f6637b4bb246d82e97f.positions[588] );
});
---
title: ''
date: '2019-09-07T16:21:22-06:00'
format: image
service: instagram
tags:
- crushwalls
latitude: '39.7611297'
longitude: '-104.9817828'
image: https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/07162458/69343651_168079094346067_4381599436713194755_n.jpg?fit=640%2C640&ssl=1
---

[![A couple of cool murals going up at Crema for #crushwalls #keyringprivate](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/07162458/69343651_168079094346067_4381599436713194755_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2019/09/07/a-couple-of-cool-murals-going-up-at-crema-for-crushwalls-keyringprivate/) 

[![A couple of cool murals going up at Crema for #crushwalls #keyringprivate](https://i0.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2019/09/07162458/69343651_168079094346067_4381599436713194755_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/B2IGZgBJa-Z/)

A couple of cool murals going up at Crema for #crushwalls #keyringprivate

39.7611297-104.9817828




* #[crushwalls](https://dentedreality.com.au/tags/crushwalls/)

Posted on [Instagram](https://www.instagram.com/p/B2IGZgBJa-Z/) [4:21 pm, September 7, 2019](https://dentedreality.com.au/2019/09/07/a-couple-of-cool-murals-going-up-at-crema-for-crushwalls-keyringprivate/ "4:21 pm") 
jQuery(document).ready(function(){
var gmap\_md742811064b9e577331e4ce63882f1ac = {
positions : {
214 : new google.maps.LatLng( '39.7611297', '-104.9817828' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md742811064b9e577331e4ce63882f1ac' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md742811064b9e577331e4ce63882f1ac.positions ) {
gmap\_md742811064b9e577331e4ce63882f1ac.bounds.extend( gmap\_md742811064b9e577331e4ce63882f1ac.positions[m] );
}
// Render markers
for ( var m in gmap\_md742811064b9e577331e4ce63882f1ac.positions ) {
gmap\_md742811064b9e577331e4ce63882f1ac.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md742811064b9e577331e4ce63882f1ac.map,
position : gmap\_md742811064b9e577331e4ce63882f1ac.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md742811064b9e577331e4ce63882f1ac.map.setCenter( gmap\_md742811064b9e577331e4ce63882f1ac.positions[214] );
});
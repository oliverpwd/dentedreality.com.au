---
title: ''
date: '2018-01-25T17:24:04+00:00'
format: image
service: instagram
tags:
- nofilter
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/01/26866007_212676432639706_8191943904237453312_n.jpg?fit=640%2C640&ssl=1
---

[![Good work on the sunset, Denver. #nofilter](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/01/26866007_212676432639706_8191943904237453312_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2018/01/25/good-work-on-the-sunset-denver-nofilter/) 

[![Good work on the sunset, Denver. #nofilter](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2018/01/26866007_212676432639706_8191943904237453312_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BeZHcADBSyJ/)

Good work on the sunset, Denver. #nofilter





* #[nofilter](https://dentedreality.com.au/tags/nofilter/)

Posted on [Instagram](https://www.instagram.com/p/BeZHcADBSyJ/) [5:24 pm, January 25, 2018](https://dentedreality.com.au/2018/01/25/good-work-on-the-sunset-denver-nofilter/ "5:24 pm") 
jQuery(document).ready(function(){
var gmap\_mf9d734f768d4d956a489d5c4078f2620 = {
positions : {
441 : new google.maps.LatLng( '39.7675084', '-104.9740488' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf9d734f768d4d956a489d5c4078f2620' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf9d734f768d4d956a489d5c4078f2620.positions ) {
gmap\_mf9d734f768d4d956a489d5c4078f2620.bounds.extend( gmap\_mf9d734f768d4d956a489d5c4078f2620.positions[m] );
}
// Render markers
for ( var m in gmap\_mf9d734f768d4d956a489d5c4078f2620.positions ) {
gmap\_mf9d734f768d4d956a489d5c4078f2620.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf9d734f768d4d956a489d5c4078f2620.map,
position : gmap\_mf9d734f768d4d956a489d5c4078f2620.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf9d734f768d4d956a489d5c4078f2620.map.setCenter( gmap\_mf9d734f768d4d956a489d5c4078f2620.positions[441] );
});
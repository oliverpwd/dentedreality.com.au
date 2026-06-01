---
title: Denver Meetup
date: '2013-11-18T08:50:49+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0819
- vision:mountain=0866
- vision:outdoor=099
- vision:sky=072
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291557754_bfafb59a0c_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291557754_bfafb59a0c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-12/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-12/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0819](http://dentedreality.com.au/tags/visionclouds0819/)
* #[vision:mountain=0866](http://dentedreality.com.au/tags/visionmountain0866/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=072](http://dentedreality.com.au/tags/visionsky072/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291557754/) [8:50 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-12/ "8:50 am") 
jQuery(document).ready(function(){
var gmap\_m5da8446f4266e897323559042ec100cc = {
positions : {
698 : new google.maps.LatLng( '39.663569', '-105.204964' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5da8446f4266e897323559042ec100cc' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5da8446f4266e897323559042ec100cc.positions ) {
gmap\_m5da8446f4266e897323559042ec100cc.bounds.extend( gmap\_m5da8446f4266e897323559042ec100cc.positions[m] );
}
// Render markers
for ( var m in gmap\_m5da8446f4266e897323559042ec100cc.positions ) {
gmap\_m5da8446f4266e897323559042ec100cc.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5da8446f4266e897323559042ec100cc.map,
position : gmap\_m5da8446f4266e897323559042ec100cc.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5da8446f4266e897323559042ec100cc.map.setCenter( gmap\_m5da8446f4266e897323559042ec100cc.positions[698] );
});
---
title: Denver Meetup
date: '2013-11-17T15:33:49+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0602
- vision:plant=086
- vision:sky=0916
- vision:sunset=0688
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291560864_26617d008c_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291560864_26617d008c_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/17/denver-meetup-17/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-17/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0602](http://dentedreality.com.au/tags/visionoutdoor0602/)
* #[vision:plant=086](http://dentedreality.com.au/tags/visionplant086/)
* #[vision:sky=0916](http://dentedreality.com.au/tags/visionsky0916/)
* #[vision:sunset=0688](http://dentedreality.com.au/tags/visionsunset0688/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291560864/) [3:33 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-17/ "3:33 pm") 
jQuery(document).ready(function(){
var gmap\_ma1f47d4d2790825002ee7de01e2c15f2 = {
positions : {
535 : new google.maps.LatLng( '39.7486', '-105.0075' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma1f47d4d2790825002ee7de01e2c15f2' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma1f47d4d2790825002ee7de01e2c15f2.positions ) {
gmap\_ma1f47d4d2790825002ee7de01e2c15f2.bounds.extend( gmap\_ma1f47d4d2790825002ee7de01e2c15f2.positions[m] );
}
// Render markers
for ( var m in gmap\_ma1f47d4d2790825002ee7de01e2c15f2.positions ) {
gmap\_ma1f47d4d2790825002ee7de01e2c15f2.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma1f47d4d2790825002ee7de01e2c15f2.map,
position : gmap\_ma1f47d4d2790825002ee7de01e2c15f2.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma1f47d4d2790825002ee7de01e2c15f2.map.setCenter( gmap\_ma1f47d4d2790825002ee7de01e2c15f2.positions[535] );
});
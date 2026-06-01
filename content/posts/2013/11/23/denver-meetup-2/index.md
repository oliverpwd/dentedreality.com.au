---
title: Denver Meetup
date: '2013-11-23T08:09:18+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:car=0794
- vision:outdoor=0911
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291288933_d0c914b478_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291288933_d0c914b478_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/23/denver-meetup-2/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/23/denver-meetup-2/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:car=0794](http://dentedreality.com.au/tags/visioncar0794/)
* #[vision:outdoor=0911](http://dentedreality.com.au/tags/visionoutdoor0911/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291288933/) [8:09 am, November 23, 2013](http://dentedreality.com.au/2013/11/23/denver-meetup-2/ "8:09 am") 
jQuery(document).ready(function(){
var gmap\_m5a7bea329f87bde009de3f096e38f63a = {
positions : {
884 : new google.maps.LatLng( '39.743827', '-104.995231' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5a7bea329f87bde009de3f096e38f63a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5a7bea329f87bde009de3f096e38f63a.positions ) {
gmap\_m5a7bea329f87bde009de3f096e38f63a.bounds.extend( gmap\_m5a7bea329f87bde009de3f096e38f63a.positions[m] );
}
// Render markers
for ( var m in gmap\_m5a7bea329f87bde009de3f096e38f63a.positions ) {
gmap\_m5a7bea329f87bde009de3f096e38f63a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5a7bea329f87bde009de3f096e38f63a.map,
position : gmap\_m5a7bea329f87bde009de3f096e38f63a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5a7bea329f87bde009de3f096e38f63a.map.setCenter( gmap\_m5a7bea329f87bde009de3f096e38f63a.positions[884] );
});
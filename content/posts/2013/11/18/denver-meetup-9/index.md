---
title: Denver Meetup
date: '2013-11-18T08:58:18+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0925
- vision:mountain=086
- vision:outdoor=099
- vision:sky=0964
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291293473_b022fba0ee_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291293473_b022fba0ee_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-9/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-9/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0925](http://dentedreality.com.au/tags/visionclouds0925/)
* #[vision:mountain=086](http://dentedreality.com.au/tags/visionmountain086/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=0964](http://dentedreality.com.au/tags/visionsky0964/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291293473/) [8:58 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-9/ "8:58 am") 
jQuery(document).ready(function(){
var gmap\_maf6849a59740424d3f254ef0da427e2d = {
positions : {
942 : new google.maps.LatLng( '39.660841', '-105.203462' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maf6849a59740424d3f254ef0da427e2d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maf6849a59740424d3f254ef0da427e2d.positions ) {
gmap\_maf6849a59740424d3f254ef0da427e2d.bounds.extend( gmap\_maf6849a59740424d3f254ef0da427e2d.positions[m] );
}
// Render markers
for ( var m in gmap\_maf6849a59740424d3f254ef0da427e2d.positions ) {
gmap\_maf6849a59740424d3f254ef0da427e2d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maf6849a59740424d3f254ef0da427e2d.map,
position : gmap\_maf6849a59740424d3f254ef0da427e2d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maf6849a59740424d3f254ef0da427e2d.map.setCenter( gmap\_maf6849a59740424d3f254ef0da427e2d.positions[942] );
});
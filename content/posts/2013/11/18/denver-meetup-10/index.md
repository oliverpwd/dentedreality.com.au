---
title: Denver Meetup
date: '2013-11-18T08:58:01+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0742
- vision:mountain=076
- vision:outdoor=099
- vision:sky=0873
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291682826_c8c7e2f461_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291682826_c8c7e2f461_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/18/denver-meetup-10/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-10/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0742](http://dentedreality.com.au/tags/visionclouds0742/)
* #[vision:mountain=076](http://dentedreality.com.au/tags/visionmountain076/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=0873](http://dentedreality.com.au/tags/visionsky0873/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291682826/) [8:58 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-10/ "8:58 am") 
jQuery(document).ready(function(){
var gmap\_maa4dec7900dcf5dad32fbb521b7d45eb = {
positions : {
737 : new google.maps.LatLng( '39.660838', '-105.2035' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_maa4dec7900dcf5dad32fbb521b7d45eb' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.positions ) {
gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.bounds.extend( gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.positions[m] );
}
// Render markers
for ( var m in gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.positions ) {
gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.map,
position : gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.map.setCenter( gmap\_maa4dec7900dcf5dad32fbb521b7d45eb.positions[737] );
});
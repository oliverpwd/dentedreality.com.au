---
title: Denver Meetup
date: '2013-11-17T16:23:42+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:mountain=0559
- vision:outdoor=0665
- vision:sky=0887
- vision:sunset=0811
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291559684_7208f0a463_o.jpg?resize=607%2C341
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291559684_7208f0a463_o.jpg?resize=607%2C341)](http://dentedreality.com.au/2013/11/17/denver-meetup-15/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-15/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:mountain=0559](http://dentedreality.com.au/tags/visionmountain0559/)
* #[vision:outdoor=0665](http://dentedreality.com.au/tags/visionoutdoor0665/)
* #[vision:sky=0887](http://dentedreality.com.au/tags/visionsky0887/)
* #[vision:sunset=0811](http://dentedreality.com.au/tags/visionsunset0811/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291559684/) [4:23 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-15/ "4:23 pm") 
jQuery(document).ready(function(){
var gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d = {
positions : {
752 : new google.maps.LatLng( '39.748711', '-105.007448' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.positions ) {
gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.bounds.extend( gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.positions[m] );
}
// Render markers
for ( var m in gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.positions ) {
gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.map,
position : gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.map.setCenter( gmap\_m8ed96369d69040b2d2d5c5fcd4f4788d.positions[752] );
});
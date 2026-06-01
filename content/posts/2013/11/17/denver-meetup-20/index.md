---
title: Denver Meetup
date: '2013-11-17T12:16:35+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0638
- vision:text=0589
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291284223_8e3c1a8bed_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291284223_8e3c1a8bed_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/17/denver-meetup-20/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/17/denver-meetup-20/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0638](http://dentedreality.com.au/tags/visionoutdoor0638/)
* #[vision:text=0589](http://dentedreality.com.au/tags/visiontext0589/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291284223/) [12:16 pm, November 17, 2013](http://dentedreality.com.au/2013/11/17/denver-meetup-20/ "12:16 pm") 
jQuery(document).ready(function(){
var gmap\_m584887fbfe0548e38445ca37171dacf1 = {
positions : {
334 : new google.maps.LatLng( '39.712494', '-104.99872' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m584887fbfe0548e38445ca37171dacf1' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m584887fbfe0548e38445ca37171dacf1.positions ) {
gmap\_m584887fbfe0548e38445ca37171dacf1.bounds.extend( gmap\_m584887fbfe0548e38445ca37171dacf1.positions[m] );
}
// Render markers
for ( var m in gmap\_m584887fbfe0548e38445ca37171dacf1.positions ) {
gmap\_m584887fbfe0548e38445ca37171dacf1.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m584887fbfe0548e38445ca37171dacf1.map,
position : gmap\_m584887fbfe0548e38445ca37171dacf1.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m584887fbfe0548e38445ca37171dacf1.map.setCenter( gmap\_m584887fbfe0548e38445ca37171dacf1.positions[334] );
});
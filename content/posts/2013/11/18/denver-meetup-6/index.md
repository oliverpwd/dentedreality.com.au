---
title: Denver Meetup
date: '2013-11-18T09:09:59+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:clouds=0955
- vision:mountain=0842
- vision:outdoor=099
- vision:sky=098
- vision:sunset=0557
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291685456_51827a3444_o.jpg?resize=607%2C455
---

[![Denver Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291685456_51827a3444_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2013/11/18/denver-meetup-6/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/18/denver-meetup-6/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:clouds=0955](http://dentedreality.com.au/tags/visionclouds0955/)
* #[vision:mountain=0842](http://dentedreality.com.au/tags/visionmountain0842/)
* #[vision:outdoor=099](http://dentedreality.com.au/tags/visionoutdoor099/)
* #[vision:sky=098](http://dentedreality.com.au/tags/visionsky098/)
* #[vision:sunset=0557](http://dentedreality.com.au/tags/visionsunset0557/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291685456/) [9:09 am, November 18, 2013](http://dentedreality.com.au/2013/11/18/denver-meetup-6/ "9:09 am") 
jQuery(document).ready(function(){
var gmap\_m14416f53ce7118195f4a3f08e5ece63b = {
positions : {
713 : new google.maps.LatLng( '39.660805', '-105.203423' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m14416f53ce7118195f4a3f08e5ece63b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m14416f53ce7118195f4a3f08e5ece63b.positions ) {
gmap\_m14416f53ce7118195f4a3f08e5ece63b.bounds.extend( gmap\_m14416f53ce7118195f4a3f08e5ece63b.positions[m] );
}
// Render markers
for ( var m in gmap\_m14416f53ce7118195f4a3f08e5ece63b.positions ) {
gmap\_m14416f53ce7118195f4a3f08e5ece63b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m14416f53ce7118195f4a3f08e5ece63b.map,
position : gmap\_m14416f53ce7118195f4a3f08e5ece63b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m14416f53ce7118195f4a3f08e5ece63b.map.setCenter( gmap\_m14416f53ce7118195f4a3f08e5ece63b.positions[713] );
});
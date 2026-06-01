---
title: San Diego Meetup
date: '2012-09-12T13:05:27+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- meetup
- sandiego
- sandiego2012
- work
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264534_7246066479_o.jpg?resize=607%2C455
---

[![San Diego Meetup](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460264534_7246066479_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/09/12/san-diego-meetup-10/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/12/san-diego-meetup-10/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460264534/) [1:05 pm, September 12, 2012](http://dentedreality.com.au/2012/09/12/san-diego-meetup-10/ "1:05 pm") 
jQuery(document).ready(function(){
var gmap\_mf169e0d2f6de222813d225d7926d5ec9 = {
positions : {
785 : new google.maps.LatLng( '32.569719', '-116.911939' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mf169e0d2f6de222813d225d7926d5ec9' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mf169e0d2f6de222813d225d7926d5ec9.positions ) {
gmap\_mf169e0d2f6de222813d225d7926d5ec9.bounds.extend( gmap\_mf169e0d2f6de222813d225d7926d5ec9.positions[m] );
}
// Render markers
for ( var m in gmap\_mf169e0d2f6de222813d225d7926d5ec9.positions ) {
gmap\_mf169e0d2f6de222813d225d7926d5ec9.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mf169e0d2f6de222813d225d7926d5ec9.map,
position : gmap\_mf169e0d2f6de222813d225d7926d5ec9.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mf169e0d2f6de222813d225d7926d5ec9.map.setCenter( gmap\_mf169e0d2f6de222813d225d7926d5ec9.positions[785] );
});
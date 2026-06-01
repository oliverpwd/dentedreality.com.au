---
title: San Diego Meetup
date: '2012-09-12T11:54:58+00:00'
format: image
service: flickr
tags:
- automattic
- grandmeetup
- meetup
- sandiego
- sandiego2012
- work
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460263804_0727a1cab6_o.jpg?resize=607%2C809
---

[![San Diego Meetup](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460263804_0727a1cab6_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2012/09/12/san-diego-meetup-14/) 
# [San Diego Meetup](http://dentedreality.com.au/2012/09/12/san-diego-meetup-14/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[grandmeetup](http://dentedreality.com.au/tags/grandmeetup/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[sandiego](http://dentedreality.com.au/tags/sandiego/)
* #[sandiego2012](http://dentedreality.com.au/tags/sandiego2012/)
* #[work](http://dentedreality.com.au/tags/work/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460263804/) [11:54 am, September 12, 2012](http://dentedreality.com.au/2012/09/12/san-diego-meetup-14/ "11:54 am") 
jQuery(document).ready(function(){
var gmap\_ma2f1275f3ea6b629f806a737e21e4b87 = {
positions : {
220 : new google.maps.LatLng( '32.569586', '-116.9111' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma2f1275f3ea6b629f806a737e21e4b87' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma2f1275f3ea6b629f806a737e21e4b87.positions ) {
gmap\_ma2f1275f3ea6b629f806a737e21e4b87.bounds.extend( gmap\_ma2f1275f3ea6b629f806a737e21e4b87.positions[m] );
}
// Render markers
for ( var m in gmap\_ma2f1275f3ea6b629f806a737e21e4b87.positions ) {
gmap\_ma2f1275f3ea6b629f806a737e21e4b87.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma2f1275f3ea6b629f806a737e21e4b87.map,
position : gmap\_ma2f1275f3ea6b629f806a737e21e4b87.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma2f1275f3ea6b629f806a737e21e4b87.map.setCenter( gmap\_ma2f1275f3ea6b629f806a737e21e4b87.positions[220] );
});
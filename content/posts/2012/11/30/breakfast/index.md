---
title: Breakfast
date: '2012-11-30T05:34:38+00:00'
format: image
service: flickr
tags:
- automattic
- bacon
- breakfast
- meetup
- neworleans
- nola
- teamsocial
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460395372_8dacb09526_o.jpg?resize=607%2C452
---

[![Breakfast](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8460395372_8dacb09526_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/11/30/breakfast/) 
# [Breakfast](http://dentedreality.com.au/2012/11/30/breakfast/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[bacon](http://dentedreality.com.au/tags/bacon/)
* #[breakfast](http://dentedreality.com.au/tags/breakfast/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460395372/) [5:34 am, November 30, 2012](http://dentedreality.com.au/2012/11/30/breakfast/ "5:34 am") 
jQuery(document).ready(function(){
var gmap\_md8fe8fe91c9ca59b5adae0430b9418d5 = {
positions : {
315 : new google.maps.LatLng( '29.932333', '-90.1025' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_md8fe8fe91c9ca59b5adae0430b9418d5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.positions ) {
gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.bounds.extend( gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.positions[m] );
}
// Render markers
for ( var m in gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.positions ) {
gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.map,
position : gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.map.setCenter( gmap\_md8fe8fe91c9ca59b5adae0430b9418d5.positions[315] );
});
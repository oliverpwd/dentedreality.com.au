---
title: Swamp Tour!
date: '2012-11-29T07:43:19+00:00'
format: image
service: flickr
tags:
- automattic
- meetup
- neworleans
- nola
- swamp
- swamptour
- teamsocial
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459291919_cb6b827ddc_o.jpg?resize=607%2C809
---

[![Swamp Tour!](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2012/11/8459291919_cb6b827ddc_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2012/11/29/swamp-tour-4/) 
# [Swamp Tour!](http://dentedreality.com.au/2012/11/29/swamp-tour-4/)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[neworleans](http://dentedreality.com.au/tags/neworleans/)
* #[nola](http://dentedreality.com.au/tags/nola/)
* #[swamp](http://dentedreality.com.au/tags/swamp/)
* #[swamptour](http://dentedreality.com.au/tags/swamptour/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8459291919/) [7:43 am, November 29, 2012](http://dentedreality.com.au/2012/11/29/swamp-tour-4/ "7:43 am") 
jQuery(document).ready(function(){
var gmap\_made2440692e8ea5fd7bcbee999656255 = {
positions : {
166 : new google.maps.LatLng( '29.916222', '-90.41825' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_made2440692e8ea5fd7bcbee999656255' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_made2440692e8ea5fd7bcbee999656255.positions ) {
gmap\_made2440692e8ea5fd7bcbee999656255.bounds.extend( gmap\_made2440692e8ea5fd7bcbee999656255.positions[m] );
}
// Render markers
for ( var m in gmap\_made2440692e8ea5fd7bcbee999656255.positions ) {
gmap\_made2440692e8ea5fd7bcbee999656255.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_made2440692e8ea5fd7bcbee999656255.map,
position : gmap\_made2440692e8ea5fd7bcbee999656255.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_made2440692e8ea5fd7bcbee999656255.map.setCenter( gmap\_made2440692e8ea5fd7bcbee999656255.positions[166] );
});
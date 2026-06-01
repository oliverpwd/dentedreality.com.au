---
title: Life of Riley
date: '2011-05-23T17:02:58+00:00'
format: image
service: flickr
tags:
- meetup
- PDX
- Portland
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802181789_88f4f79047_o.jpg?resize=607%2C452
---

[![Life of Riley](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/05/5802181789_88f4f79047_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/05/23/life-of-riley/) 
# [Life of Riley](http://dentedreality.com.au/2011/05/23/life-of-riley/)

We spent a couple nights here. Shuffleboard, pool table, drinks. Win.





* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/5802181789/) [5:02 pm, May 23, 2011](http://dentedreality.com.au/2011/05/23/life-of-riley/ "5:02 pm") 
jQuery(document).ready(function(){
var gmap\_m34bc12ca5295c08230d0f01cd77b005b = {
positions : {
793 : new google.maps.LatLng( '45.524833', '-122.681167' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m34bc12ca5295c08230d0f01cd77b005b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m34bc12ca5295c08230d0f01cd77b005b.positions ) {
gmap\_m34bc12ca5295c08230d0f01cd77b005b.bounds.extend( gmap\_m34bc12ca5295c08230d0f01cd77b005b.positions[m] );
}
// Render markers
for ( var m in gmap\_m34bc12ca5295c08230d0f01cd77b005b.positions ) {
gmap\_m34bc12ca5295c08230d0f01cd77b005b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m34bc12ca5295c08230d0f01cd77b005b.map,
position : gmap\_m34bc12ca5295c08230d0f01cd77b005b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m34bc12ca5295c08230d0f01cd77b005b.map.setCenter( gmap\_m34bc12ca5295c08230d0f01cd77b005b.positions[793] );
});
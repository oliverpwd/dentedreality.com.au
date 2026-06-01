---
title: Team Social in Boston
date: '2012-04-08T12:23:12-06:00'
format: image
service: flickr
tags:
- automattic
- jetty
- meetup
- pier
- teamsocial
latitude: '42.367333'
longitude: '-71.067334'
image: https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190548/7770463188_ee1b8f6981_o-1024x764.jpg?resize=607%2C452&ssl=1
---

[![Team Social in Boston](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190548/7770463188_ee1b8f6981_o-1024x764.jpg?resize=607%2C452&ssl=1)](https://dentedreality.com.au/2012/04/08/team-social-in-boston-9/) 
# [Team Social in Boston](https://dentedreality.com.au/2012/04/08/team-social-in-boston-9/)

[![Team Social in Boston](https://i2.wp.com/s3.amazonaws.com/dentedreality-content/wp-content/uploads/2012/04/14190548/7770463188_ee1b8f6981_o-1024x764.jpg?resize=607%2C452&ssl=1)](http://www.flickr.com/photos/borkazoid/7770463188/)

42.367333-71.067334




* #[automattic](https://dentedreality.com.au/tags/automattic/)
* #[jetty](https://dentedreality.com.au/tags/jetty/)
* #[meetup](https://dentedreality.com.au/tags/meetup/)
* #[pier](https://dentedreality.com.au/tags/pier/)
* #[teamsocial](https://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770463188/) [12:23 pm, April 8, 2012](https://dentedreality.com.au/2012/04/08/team-social-in-boston-9/ "12:23 pm") 
jQuery(document).ready(function(){
var gmap\_m15efb0ac3886109f28b410bcbb6ea3c5 = {
positions : {
555 : new google.maps.LatLng( '42.367333', '-71.067334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m15efb0ac3886109f28b410bcbb6ea3c5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.positions ) {
gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.bounds.extend( gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.positions[m] );
}
// Render markers
for ( var m in gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.positions ) {
gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.map,
position : gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.map.setCenter( gmap\_m15efb0ac3886109f28b410bcbb6ea3c5.positions[555] );
});
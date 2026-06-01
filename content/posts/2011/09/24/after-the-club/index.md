---
title: After the club
date: '2011-09-24T22:39:01+00:00'
format: image
service: flickr
tags:
- andypeatling
- apeatling
- automattic
- jjj
- johnjamesjacoby
- justin
- justinshreve
- Lisbon
- mdawaffe
- meetup
- mike
- portugal
- teamsocial
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812112116_9b2c1455b6_o.jpg?resize=607%2C452
---

[![After the club](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2011/09/6812112116_9b2c1455b6_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2011/09/24/after-the-club/) 
# [After the club](http://dentedreality.com.au/2011/09/24/after-the-club/)





* #[andypeatling](http://dentedreality.com.au/tags/andypeatling/)
* #[apeatling](http://dentedreality.com.au/tags/apeatling/)
* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[jjj](http://dentedreality.com.au/tags/jjj/)
* #[johnjamesjacoby](http://dentedreality.com.au/tags/johnjamesjacoby/)
* #[justin](http://dentedreality.com.au/tags/justin/)
* #[justinshreve](http://dentedreality.com.au/tags/justinshreve/)
* #[Lisbon](http://dentedreality.com.au/tags/lisbon/)
* #[mdawaffe](http://dentedreality.com.au/tags/mdawaffe/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mike](http://dentedreality.com.au/tags/mike/)
* #[portugal](http://dentedreality.com.au/tags/portugal/)
* #[teamsocial](http://dentedreality.com.au/tags/teamsocial/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/6812112116/) [10:39 pm, September 24, 2011](http://dentedreality.com.au/2011/09/24/after-the-club/ "10:39 pm") 
jQuery(document).ready(function(){
var gmap\_m3491ad13ecb0dfee44ec6728cf0f551a = {
positions : {
600 : new google.maps.LatLng( '38.718666', '-9.118667' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m3491ad13ecb0dfee44ec6728cf0f551a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.positions ) {
gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.bounds.extend( gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.positions[m] );
}
// Render markers
for ( var m in gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.positions ) {
gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.map,
position : gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.map.setCenter( gmap\_m3491ad13ecb0dfee44ec6728cf0f551a.positions[600] );
});
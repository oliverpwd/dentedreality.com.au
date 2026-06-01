---
title: Beach Tennis
date: '2008-04-04T22:43:43+00:00'
format: image
service: flickr
tags:
- australia
- beachtennis
- maryann
- renniewedding
- tim
- timswedding
- westernaustraliadenmark
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433430644_527b048e5e_o.jpg?resize=607%2C455
---

[![Beach Tennis](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2433430644_527b048e5e_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2008/04/04/beach-tennis/) 
# [Beach Tennis](http://dentedreality.com.au/2008/04/04/beach-tennis/)

How do other people celebrate getting married?





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[beachtennis](http://dentedreality.com.au/tags/beachtennis/)
* #[maryann](http://dentedreality.com.au/tags/maryann/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[tim](http://dentedreality.com.au/tags/tim/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2433430644/) [10:43 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/beach-tennis/ "10:43 pm") 
jQuery(document).ready(function(){
var gmap\_m2cc8aa1b25352f53775de373a84f075c = {
positions : {
35 : new google.maps.LatLng( '-34.983877', '117.298278' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2cc8aa1b25352f53775de373a84f075c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2cc8aa1b25352f53775de373a84f075c.positions ) {
gmap\_m2cc8aa1b25352f53775de373a84f075c.bounds.extend( gmap\_m2cc8aa1b25352f53775de373a84f075c.positions[m] );
}
// Render markers
for ( var m in gmap\_m2cc8aa1b25352f53775de373a84f075c.positions ) {
gmap\_m2cc8aa1b25352f53775de373a84f075c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2cc8aa1b25352f53775de373a84f075c.map,
position : gmap\_m2cc8aa1b25352f53775de373a84f075c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2cc8aa1b25352f53775de373a84f075c.map.setCenter( gmap\_m2cc8aa1b25352f53775de373a84f075c.positions[35] );
});
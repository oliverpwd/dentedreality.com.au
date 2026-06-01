---
title: Redonkadonk
date: '2013-06-10T09:31:26+00:00'
format: image
service: flickr
tags:
- brunchbox
- meat
- PDX
- Portland
- redonkadonk
- sandwich
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437045663_9377201d77_o.jpg?resize=607%2C813
---

[![Redonkadonk](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/06/9437045663_9377201d77_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/06/10/redonkadonk/) 
# [Redonkadonk](http://dentedreality.com.au/2013/06/10/redonkadonk/)

Amazing sandwich from the Brunch Box cart in Portland





* #[brunchbox](http://dentedreality.com.au/tags/brunchbox/)
* #[meat](http://dentedreality.com.au/tags/meat/)
* #[PDX](http://dentedreality.com.au/tags/pdx/)
* #[Portland](http://dentedreality.com.au/tags/portland/)
* #[redonkadonk](http://dentedreality.com.au/tags/redonkadonk/)
* #[sandwich](http://dentedreality.com.au/tags/sandwich/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437045663/) [9:31 am, June 10, 2013](http://dentedreality.com.au/2013/06/10/redonkadonk/ "9:31 am") 
jQuery(document).ready(function(){
var gmap\_ma655935eaf0b4196c02bd66142dfd965 = {
positions : {
248 : new google.maps.LatLng( '45.521166', '-122.679834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_ma655935eaf0b4196c02bd66142dfd965' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_ma655935eaf0b4196c02bd66142dfd965.positions ) {
gmap\_ma655935eaf0b4196c02bd66142dfd965.bounds.extend( gmap\_ma655935eaf0b4196c02bd66142dfd965.positions[m] );
}
// Render markers
for ( var m in gmap\_ma655935eaf0b4196c02bd66142dfd965.positions ) {
gmap\_ma655935eaf0b4196c02bd66142dfd965.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_ma655935eaf0b4196c02bd66142dfd965.map,
position : gmap\_ma655935eaf0b4196c02bd66142dfd965.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_ma655935eaf0b4196c02bd66142dfd965.map.setCenter( gmap\_ma655935eaf0b4196c02bd66142dfd965.positions[248] );
});
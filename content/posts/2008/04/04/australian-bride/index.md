---
title: Australian Bride
date: '2008-04-04T21:42:02+00:00'
format: image
service: flickr
tags:
- australia
- barefoot
- beer
- bride
- glasses
- maryann
- renniewedding
- sunnies
- timswedding
- westernaustraliadenmark
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432612091_4f6f48084a_o.jpg?resize=607%2C808
---

[![Australian Bride](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2008/04/2432612091_4f6f48084a_o.jpg?resize=607%2C808)](http://dentedreality.com.au/2008/04/04/australian-bride/) 
# [Australian Bride](http://dentedreality.com.au/2008/04/04/australian-bride/)

I love this photo, I think it really captures the casual-yet-classy, down-to-earth wedding that they had. Rock out MA.





* #[australia](http://dentedreality.com.au/tags/australia/)
* #[barefoot](http://dentedreality.com.au/tags/barefoot/)
* #[beer](http://dentedreality.com.au/tags/beer/)
* #[bride](http://dentedreality.com.au/tags/bride/)
* #[glasses](http://dentedreality.com.au/tags/glasses/)
* #[maryann](http://dentedreality.com.au/tags/maryann/)
* #[renniewedding](http://dentedreality.com.au/tags/renniewedding/)
* #[sunnies](http://dentedreality.com.au/tags/sunnies/)
* #[timswedding](http://dentedreality.com.au/tags/timswedding/)
* #[westernaustraliadenmark](http://dentedreality.com.au/tags/westernaustraliadenmark/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/2432612091/) [9:42 pm, April 4, 2008](http://dentedreality.com.au/2008/04/04/australian-bride/ "9:42 pm") 
jQuery(document).ready(function(){
var gmap\_m0afbaedab273e8c16c55f0c1fda8ac35 = {
positions : {
663 : new google.maps.LatLng( '-35.03604', '117.329177' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0afbaedab273e8c16c55f0c1fda8ac35' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.positions ) {
gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.bounds.extend( gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.positions[m] );
}
// Render markers
for ( var m in gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.positions ) {
gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.map,
position : gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.map.setCenter( gmap\_m0afbaedab273e8c16c55f0c1fda8ac35.positions[663] );
});
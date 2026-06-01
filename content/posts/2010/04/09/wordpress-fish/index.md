---
title: WordPress Fish
date: '2010-04-09T15:39:06+00:00'
format: image
service: flickr
tags:
- fish
- foil
- matt
- photomatt
- tombrown
- trackerschool
- tracking
- wordpress
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516472152_af2d485d98_o.jpg?resize=607%2C455
---

[![WordPress Fish](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2010/04/4516472152_af2d485d98_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2010/04/09/wordpress-fish/) 
# [WordPress Fish](http://dentedreality.com.au/2010/04/09/wordpress-fish/)

We had to do something unique so that we could recognize our fish in amongst 70 other fish on the coals. Ours was a (W) WordPress logo ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[fish](http://dentedreality.com.au/tags/fish/)
* #[foil](http://dentedreality.com.au/tags/foil/)
* #[matt](http://dentedreality.com.au/tags/matt/)
* #[photomatt](http://dentedreality.com.au/tags/photomatt/)
* #[tombrown](http://dentedreality.com.au/tags/tombrown/)
* #[trackerschool](http://dentedreality.com.au/tags/trackerschool/)
* #[tracking](http://dentedreality.com.au/tags/tracking/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/4516472152/) [3:39 pm, April 9, 2010](http://dentedreality.com.au/2010/04/09/wordpress-fish/ "3:39 pm") 
jQuery(document).ready(function(){
var gmap\_m6baf4be760c1404af94b53b120777b62 = {
positions : {
494 : new google.maps.LatLng( '37.177141', '-122.116744' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m6baf4be760c1404af94b53b120777b62' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m6baf4be760c1404af94b53b120777b62.positions ) {
gmap\_m6baf4be760c1404af94b53b120777b62.bounds.extend( gmap\_m6baf4be760c1404af94b53b120777b62.positions[m] );
}
// Render markers
for ( var m in gmap\_m6baf4be760c1404af94b53b120777b62.positions ) {
gmap\_m6baf4be760c1404af94b53b120777b62.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m6baf4be760c1404af94b53b120777b62.map,
position : gmap\_m6baf4be760c1404af94b53b120777b62.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m6baf4be760c1404af94b53b120777b62.map.setCenter( gmap\_m6baf4be760c1404af94b53b120777b62.positions[494] );
});
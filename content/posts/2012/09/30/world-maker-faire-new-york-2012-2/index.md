---
title: World Maker Faire, New York, 2012
date: '2012-09-30T09:58:28+00:00'
format: image
service: flickr
tags:
- diy
- make
- maker
- MakerFaire
- newyork
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460301770_35d790ccdb_o.jpg?resize=607%2C455
---

[![World Maker Faire, New York, 2012](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/09/8460301770_35d790ccdb_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2012/09/30/world-maker-faire-new-york-2012-2/) 
# [World Maker Faire, New York, 2012](http://dentedreality.com.au/2012/09/30/world-maker-faire-new-york-2012-2/)





* #[diy](http://dentedreality.com.au/tags/diy/)
* #[make](http://dentedreality.com.au/tags/make/)
* #[maker](http://dentedreality.com.au/tags/maker/)
* #[MakerFaire](http://dentedreality.com.au/tags/makerfaire/)
* #[newyork](http://dentedreality.com.au/tags/newyork/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8460301770/) [9:58 am, September 30, 2012](http://dentedreality.com.au/2012/09/30/world-maker-faire-new-york-2012-2/ "9:58 am") 
jQuery(document).ready(function(){
var gmap\_mb2c22eee68778c86c75bdc52eb76b3b0 = {
positions : {
62 : new google.maps.LatLng( '40.748808', '-73.853789' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb2c22eee68778c86c75bdc52eb76b3b0' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.positions ) {
gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.bounds.extend( gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.positions[m] );
}
// Render markers
for ( var m in gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.positions ) {
gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.map,
position : gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.map.setCenter( gmap\_mb2c22eee68778c86c75bdc52eb76b3b0.positions[62] );
});
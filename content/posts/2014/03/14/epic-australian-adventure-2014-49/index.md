---
title: Epic Australian Adventure, 2014
date: '2014-03-14T09:07:21+00:00'
format: image
service: flickr
tags:
- perth
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904712922_3bc527e119_o.jpg?resize=607%2C809
---

[![Epic Australian Adventure, 2014](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13904712922_3bc527e119_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-49/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-49/)

Perth, Mooloolaba and Melbourne





* #[perth](http://dentedreality.com.au/tags/perth/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13904712922/) [9:07 am, March 14, 2014](http://dentedreality.com.au/2014/03/14/epic-australian-adventure-2014-49/ "9:07 am") 
jQuery(document).ready(function(){
var gmap\_mdd17aa04357b6222e6bb5658141eda36 = {
positions : {
784 : new google.maps.LatLng( '-31.956412', '115.815558' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mdd17aa04357b6222e6bb5658141eda36' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mdd17aa04357b6222e6bb5658141eda36.positions ) {
gmap\_mdd17aa04357b6222e6bb5658141eda36.bounds.extend( gmap\_mdd17aa04357b6222e6bb5658141eda36.positions[m] );
}
// Render markers
for ( var m in gmap\_mdd17aa04357b6222e6bb5658141eda36.positions ) {
gmap\_mdd17aa04357b6222e6bb5658141eda36.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mdd17aa04357b6222e6bb5658141eda36.map,
position : gmap\_mdd17aa04357b6222e6bb5658141eda36.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mdd17aa04357b6222e6bb5658141eda36.map.setCenter( gmap\_mdd17aa04357b6222e6bb5658141eda36.positions[784] );
});
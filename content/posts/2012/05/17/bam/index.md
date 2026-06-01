---
title: BAM!
date: '2012-05-17T11:00:49+00:00'
format: image
service: flickr
tags:
- graffiti
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770796612_acaac10bb1_o.jpg?resize=607%2C452
---

[![BAM!](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/05/7770796612_acaac10bb1_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/05/17/bam/) 
# [BAM!](http://dentedreality.com.au/2012/05/17/bam/)





* #[graffiti](http://dentedreality.com.au/tags/graffiti/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/7770796612/) [11:00 am, May 17, 2012](http://dentedreality.com.au/2012/05/17/bam/ "11:00 am") 
jQuery(document).ready(function(){
var gmap\_m5af7a8aee0a925c262a356db07fbdb22 = {
positions : {
128 : new google.maps.LatLng( '37.789666', '-122.418834' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5af7a8aee0a925c262a356db07fbdb22' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5af7a8aee0a925c262a356db07fbdb22.positions ) {
gmap\_m5af7a8aee0a925c262a356db07fbdb22.bounds.extend( gmap\_m5af7a8aee0a925c262a356db07fbdb22.positions[m] );
}
// Render markers
for ( var m in gmap\_m5af7a8aee0a925c262a356db07fbdb22.positions ) {
gmap\_m5af7a8aee0a925c262a356db07fbdb22.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5af7a8aee0a925c262a356db07fbdb22.map,
position : gmap\_m5af7a8aee0a925c262a356db07fbdb22.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5af7a8aee0a925c262a356db07fbdb22.map.setCenter( gmap\_m5af7a8aee0a925c262a356db07fbdb22.positions[128] );
});
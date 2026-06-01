---
title: Epic Australian Adventure, 2014
date: '2014-03-20T09:53:18+00:00'
format: image
service: flickr
tags:
- mooloolaba
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928294034_a621052926_o.jpg?resize=607%2C455
---

[![Epic Australian Adventure, 2014](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2014/03/13928294034_a621052926_o.jpg?resize=607%2C455)](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-12/) 
# [Epic Australian Adventure, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-12/)

Perth, Mooloolaba and Melbourne





* #[mooloolaba](http://dentedreality.com.au/tags/mooloolaba/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13928294034/) [9:53 am, March 20, 2014](http://dentedreality.com.au/2014/03/20/epic-australian-adventure-2014-12/ "9:53 am") 
jQuery(document).ready(function(){
var gmap\_mb90358cb6508ce965d41048429eb1254 = {
positions : {
318 : new google.maps.LatLng( '-26.7503', '153.046861' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mb90358cb6508ce965d41048429eb1254' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mb90358cb6508ce965d41048429eb1254.positions ) {
gmap\_mb90358cb6508ce965d41048429eb1254.bounds.extend( gmap\_mb90358cb6508ce965d41048429eb1254.positions[m] );
}
// Render markers
for ( var m in gmap\_mb90358cb6508ce965d41048429eb1254.positions ) {
gmap\_mb90358cb6508ce965d41048429eb1254.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mb90358cb6508ce965d41048429eb1254.map,
position : gmap\_mb90358cb6508ce965d41048429eb1254.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mb90358cb6508ce965d41048429eb1254.map.setCenter( gmap\_mb90358cb6508ce965d41048429eb1254.positions[318] );
});
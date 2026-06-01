---
title: Republica Dominica
date: '2013-12-29T13:40:50+00:00'
format: image
service: flickr
tags:
- dominicanrepublic
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924252145_f09fb1050f_o.jpg?fit=1500%2C1500
---

[![Republica Dominica](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/12/13924252145_f09fb1050f_o.jpg?fit=1500%2C1500)](http://dentedreality.com.au/2013/12/29/republica-dominica-8/) 
# [Republica Dominica](http://dentedreality.com.au/2013/12/29/republica-dominica-8/)





* #[dominicanrepublic](http://dentedreality.com.au/tags/dominicanrepublic/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/13924252145/) [1:40 pm, December 29, 2013](http://dentedreality.com.au/2013/12/29/republica-dominica-8/ "1:40 pm") 
jQuery(document).ready(function(){
var gmap\_mc9f8216e8bad2343e6af52a732e5511b = {
positions : {
268 : new google.maps.LatLng( '19.409555', '-70.641573' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc9f8216e8bad2343e6af52a732e5511b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc9f8216e8bad2343e6af52a732e5511b.positions ) {
gmap\_mc9f8216e8bad2343e6af52a732e5511b.bounds.extend( gmap\_mc9f8216e8bad2343e6af52a732e5511b.positions[m] );
}
// Render markers
for ( var m in gmap\_mc9f8216e8bad2343e6af52a732e5511b.positions ) {
gmap\_mc9f8216e8bad2343e6af52a732e5511b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc9f8216e8bad2343e6af52a732e5511b.map,
position : gmap\_mc9f8216e8bad2343e6af52a732e5511b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc9f8216e8bad2343e6af52a732e5511b.map.setCenter( gmap\_mc9f8216e8bad2343e6af52a732e5511b.positions[268] );
});
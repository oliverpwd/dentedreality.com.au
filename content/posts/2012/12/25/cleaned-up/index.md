---
title: Cleaned Up
date: '2012-12-25T08:38:29+00:00'
format: image
service: flickr
tags:
- alcohol
- christmas
- christmas2012
- flickriosapp:filter=nofilter
- moonshine
- uploaded:by=flickrmobile
- whiskey
image: http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8307860970_72329f85fe_o.jpg?resize=607%2C452
---

[![Cleaned Up](http://i2.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8307860970_72329f85fe_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2012/12/25/cleaned-up/) 
# [Cleaned Up](http://dentedreality.com.au/2012/12/25/cleaned-up/)

New Years is going to be good!





* #[alcohol](http://dentedreality.com.au/tags/alcohol/)
* #[christmas](http://dentedreality.com.au/tags/christmas/)
* #[christmas2012](http://dentedreality.com.au/tags/christmas2012/)
* #[flickriosapp:filter=nofilter](http://dentedreality.com.au/tags/flickriosappfilternofilter/)
* #[moonshine](http://dentedreality.com.au/tags/moonshine/)
* #[uploaded:by=flickrmobile](http://dentedreality.com.au/tags/uploadedbyflickrmobile/)
* #[whiskey](http://dentedreality.com.au/tags/whiskey/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8307860970/) [8:38 am, December 25, 2012](http://dentedreality.com.au/2012/12/25/cleaned-up/ "8:38 am") 
jQuery(document).ready(function(){
var gmap\_m5bc7e79e62499be55db74380e5ae552b = {
positions : {
403 : new google.maps.LatLng( '38.955166', '-77.073' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m5bc7e79e62499be55db74380e5ae552b' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m5bc7e79e62499be55db74380e5ae552b.positions ) {
gmap\_m5bc7e79e62499be55db74380e5ae552b.bounds.extend( gmap\_m5bc7e79e62499be55db74380e5ae552b.positions[m] );
}
// Render markers
for ( var m in gmap\_m5bc7e79e62499be55db74380e5ae552b.positions ) {
gmap\_m5bc7e79e62499be55db74380e5ae552b.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m5bc7e79e62499be55db74380e5ae552b.map,
position : gmap\_m5bc7e79e62499be55db74380e5ae552b.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m5bc7e79e62499be55db74380e5ae552b.map.setCenter( gmap\_m5bc7e79e62499be55db74380e5ae552b.positions[403] );
});
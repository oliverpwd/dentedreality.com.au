---
title: One Eye Open
date: '2012-12-25T09:52:38+00:00'
format: image
service: flickr
tags:
- aardvarkfilter
- bambi
- chihuahua
- christmas
- christmas2012
- dog
- flickriosapp:filter=aardvark
- uploaded:by=flickrmobile
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8307036429_51139e73a7_o.jpg?resize=607%2C661
---

[![One Eye Open](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2012/12/8307036429_51139e73a7_o.jpg?resize=607%2C661)](http://dentedreality.com.au/2012/12/25/one-eye-open/) 
# [One Eye Open](http://dentedreality.com.au/2012/12/25/one-eye-open/)

One stink eye.





* #[aardvarkfilter](http://dentedreality.com.au/tags/aardvarkfilter/)
* #[bambi](http://dentedreality.com.au/tags/bambi/)
* #[chihuahua](http://dentedreality.com.au/tags/chihuahua/)
* #[christmas](http://dentedreality.com.au/tags/christmas/)
* #[christmas2012](http://dentedreality.com.au/tags/christmas2012/)
* #[dog](http://dentedreality.com.au/tags/dog/)
* #[flickriosapp:filter=aardvark](http://dentedreality.com.au/tags/flickriosappfilteraardvark/)
* #[uploaded:by=flickrmobile](http://dentedreality.com.au/tags/uploadedbyflickrmobile/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/8307036429/) [9:52 am, December 25, 2012](http://dentedreality.com.au/2012/12/25/one-eye-open/ "9:52 am") 
jQuery(document).ready(function(){
var gmap\_m2116f802c131518defb1879bc5233ed4 = {
positions : {
447 : new google.maps.LatLng( '38.955166', '-77.073' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m2116f802c131518defb1879bc5233ed4' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m2116f802c131518defb1879bc5233ed4.positions ) {
gmap\_m2116f802c131518defb1879bc5233ed4.bounds.extend( gmap\_m2116f802c131518defb1879bc5233ed4.positions[m] );
}
// Render markers
for ( var m in gmap\_m2116f802c131518defb1879bc5233ed4.positions ) {
gmap\_m2116f802c131518defb1879bc5233ed4.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m2116f802c131518defb1879bc5233ed4.map,
position : gmap\_m2116f802c131518defb1879bc5233ed4.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m2116f802c131518defb1879bc5233ed4.map.setCenter( gmap\_m2116f802c131518defb1879bc5233ed4.positions[447] );
});
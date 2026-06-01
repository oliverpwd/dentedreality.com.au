---
title: ''
date: '2017-10-23T12:32:33+00:00'
format: image
service: instagram
tags:
- chromedevsummit
- jetpack
- wordpress
image: https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22710347_709592305897901_2542009753148588032_n.jpg?fit=640%2C640&ssl=1
---

[![At #chromedevsummit with @goldsounds. He'll be speaking later about PWAs and #WordPress via #Jetpack](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22710347_709592305897901_2542009753148588032_n.jpg?fit=640%2C640&ssl=1)](https://dentedreality.com.au/2017/10/23/at-chromedevsummit-with-goldsounds-hell-be-speaking-later-about-pwas-and-wordpress-via-jetpack/) 

[![At #chromedevsummit with @goldsounds. He'll be speaking later about PWAs and #WordPress via #Jetpack](https://i1.wp.com/dentedreality.com.au/wp-content/uploads/2017/10/22710347_709592305897901_2542009753148588032_n.jpg?fit=640%2C640&ssl=1)](https://www.instagram.com/p/BamcfFsBien/)

At #chromedevsummit with @goldsounds. He’ll be speaking later about PWAs and #WordPress via #Jetpack





* #[chromedevsummit](https://dentedreality.com.au/tags/chromedevsummit/)
* #[jetpack](https://dentedreality.com.au/tags/jetpack/)
* #[wordpress](https://dentedreality.com.au/tags/wordpress/)

Posted on [Instagram](https://www.instagram.com/p/BamcfFsBien/) [12:32 pm, October 23, 2017](https://dentedreality.com.au/2017/10/23/at-chromedevsummit-with-goldsounds-hell-be-speaking-later-about-pwas-and-wordpress-via-jetpack/ "12:32 pm") 
jQuery(document).ready(function(){
var gmap\_m05762764a86af7c695fe8d385ee0385c = {
positions : {
440 : new google.maps.LatLng( '37.784916242722', '-122.40201715675' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m05762764a86af7c695fe8d385ee0385c' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m05762764a86af7c695fe8d385ee0385c.positions ) {
gmap\_m05762764a86af7c695fe8d385ee0385c.bounds.extend( gmap\_m05762764a86af7c695fe8d385ee0385c.positions[m] );
}
// Render markers
for ( var m in gmap\_m05762764a86af7c695fe8d385ee0385c.positions ) {
gmap\_m05762764a86af7c695fe8d385ee0385c.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m05762764a86af7c695fe8d385ee0385c.map,
position : gmap\_m05762764a86af7c695fe8d385ee0385c.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m05762764a86af7c695fe8d385ee0385c.map.setCenter( gmap\_m05762764a86af7c695fe8d385ee0385c.positions[440] );
});
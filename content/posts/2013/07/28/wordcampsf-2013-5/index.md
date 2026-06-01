---
title: WordCampSF, 2013
date: '2013-07-28T07:54:08+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440403152_4a2e2c9c13_o.jpg?resize=607%2C813
---

[![WordCampSF, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440403152_4a2e2c9c13_o.jpg?resize=607%2C813)](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-5/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-5/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440403152/) [7:54 am, July 28, 2013](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-5/ "7:54 am") 
jQuery(document).ready(function(){
var gmap\_m644e8e41785a0c98e81dc2ceb72b99e6 = {
positions : {
868 : new google.maps.LatLng( '37.784166', '-122.397334' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m644e8e41785a0c98e81dc2ceb72b99e6' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.positions ) {
gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.bounds.extend( gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.positions[m] );
}
// Render markers
for ( var m in gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.positions ) {
gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.map,
position : gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.map.setCenter( gmap\_m644e8e41785a0c98e81dc2ceb72b99e6.positions[868] );
});
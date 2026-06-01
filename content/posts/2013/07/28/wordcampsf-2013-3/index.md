---
title: WordCampSF, 2013
date: '2013-07-28T09:16:45+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440404834_510345332d_o.jpg?resize=607%2C452
---

[![WordCampSF, 2013](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9440404834_510345332d_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-3/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-3/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9440404834/) [9:16 am, July 28, 2013](http://dentedreality.com.au/2013/07/28/wordcampsf-2013-3/ "9:16 am") 
jQuery(document).ready(function(){
var gmap\_mc07ccd43eab205b098a2225b9d7c199a = {
positions : {
291 : new google.maps.LatLng( '37.784333', '-122.397501' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_mc07ccd43eab205b098a2225b9d7c199a' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_mc07ccd43eab205b098a2225b9d7c199a.positions ) {
gmap\_mc07ccd43eab205b098a2225b9d7c199a.bounds.extend( gmap\_mc07ccd43eab205b098a2225b9d7c199a.positions[m] );
}
// Render markers
for ( var m in gmap\_mc07ccd43eab205b098a2225b9d7c199a.positions ) {
gmap\_mc07ccd43eab205b098a2225b9d7c199a.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_mc07ccd43eab205b098a2225b9d7c199a.map,
position : gmap\_mc07ccd43eab205b098a2225b9d7c199a.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_mc07ccd43eab205b098a2225b9d7c199a.map.setCenter( gmap\_mc07ccd43eab205b098a2225b9d7c199a.positions[291] );
});
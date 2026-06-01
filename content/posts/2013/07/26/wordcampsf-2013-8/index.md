---
title: WordCampSF, 2013
date: '2013-07-26T11:12:33+00:00'
format: image
tags:
- automattic
- sanfrancisco
- wcsf
- wcsf2013
- wordcamp
- wordpress
image: http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437616895_d868827eef_o.jpg?resize=607%2C452
---

[![WordCampSF, 2013](http://i0.wp.com/dentedreality.com.au/wp-content/uploads/2013/07/9437616895_d868827eef_o.jpg?resize=607%2C452)](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-8/) 
# [WordCampSF, 2013](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-8/)

I attended, spoke at, and organized the Contributor Day for WordCamp San Francisco 2013. This is my eigth WCSF ![:)](http://i0.wp.com/dentedreality.com.au/wp-includes/images/smilies/icon_smile.gif?w=607)





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[sanfrancisco](http://dentedreality.com.au/tags/sanfrancisco/)
* #[wcsf](http://dentedreality.com.au/tags/wcsf/)
* #[wcsf2013](http://dentedreality.com.au/tags/wcsf2013/)
* #[wordcamp](http://dentedreality.com.au/tags/wordcamp/)
* #[wordpress](http://dentedreality.com.au/tags/wordpress/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/9437616895/) [11:12 am, July 26, 2013](http://dentedreality.com.au/2013/07/26/wordcampsf-2013-8/ "11:12 am") 
jQuery(document).ready(function(){
var gmap\_m51945a0ffe7a4b0972d1045bc2df07a5 = {
positions : {
87 : new google.maps.LatLng( '37.768166', '-122.393' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m51945a0ffe7a4b0972d1045bc2df07a5' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.positions ) {
gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.bounds.extend( gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.positions[m] );
}
// Render markers
for ( var m in gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.positions ) {
gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.map,
position : gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.map.setCenter( gmap\_m51945a0ffe7a4b0972d1045bc2df07a5.positions[87] );
});
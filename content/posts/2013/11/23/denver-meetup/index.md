---
title: Denver Meetup
date: '2013-11-23T16:12:56+00:00'
format: image
service: flickr
tags:
- automattic
- colorado
- Denver
- meetup
- mercury
- vision:outdoor=0875
- vision:sky=0685
- vision:sunset=0713
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291550044_46d61990e7_o.jpg?resize=607%2C809
---

[![Denver Meetup](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2013/11/12291550044_46d61990e7_o.jpg?resize=607%2C809)](http://dentedreality.com.au/2013/11/23/denver-meetup/) 
# [Denver Meetup](http://dentedreality.com.au/2013/11/23/denver-meetup/)

Team Mercury meetup (and a few days after) in Denver, Colorado.





* #[automattic](http://dentedreality.com.au/tags/automattic/)
* #[colorado](http://dentedreality.com.au/tags/colorado/)
* #[Denver](http://dentedreality.com.au/tags/denver/)
* #[meetup](http://dentedreality.com.au/tags/meetup/)
* #[mercury](http://dentedreality.com.au/tags/mercury/)
* #[vision:outdoor=0875](http://dentedreality.com.au/tags/visionoutdoor0875/)
* #[vision:sky=0685](http://dentedreality.com.au/tags/visionsky0685/)
* #[vision:sunset=0713](http://dentedreality.com.au/tags/visionsunset0713/)

Posted on [Flickr](http://www.flickr.com/photos/borkazoid/12291550044/) [4:12 pm, November 23, 2013](http://dentedreality.com.au/2013/11/23/denver-meetup/ "4:12 pm") 
jQuery(document).ready(function(){
var gmap\_m0e589f2338ceb47d3b4602a111ee6e54 = {
positions : {
501 : new google.maps.LatLng( '39.7123', '-104.991692' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m0e589f2338ceb47d3b4602a111ee6e54' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m0e589f2338ceb47d3b4602a111ee6e54.positions ) {
gmap\_m0e589f2338ceb47d3b4602a111ee6e54.bounds.extend( gmap\_m0e589f2338ceb47d3b4602a111ee6e54.positions[m] );
}
// Render markers
for ( var m in gmap\_m0e589f2338ceb47d3b4602a111ee6e54.positions ) {
gmap\_m0e589f2338ceb47d3b4602a111ee6e54.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m0e589f2338ceb47d3b4602a111ee6e54.map,
position : gmap\_m0e589f2338ceb47d3b4602a111ee6e54.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m0e589f2338ceb47d3b4602a111ee6e54.map.setCenter( gmap\_m0e589f2338ceb47d3b4602a111ee6e54.positions[501] );
});
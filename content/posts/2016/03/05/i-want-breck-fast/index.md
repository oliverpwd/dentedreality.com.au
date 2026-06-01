---
title: ''
date: '2016-03-05T07:45:09+00:00'
format: image
service: instagram
image: http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12383467_189988891372953_440187917_n.jpg?fit=640%2C640
---

[![I want Breck...fast.](http://i1.wp.com/dentedreality.com.au/wp-content/uploads/2016/03/12383467_189988891372953_440187917_n.jpg?fit=640%2C640)](http://dentedreality.com.au/2016/03/05/i-want-breck-fast/) 

I want Breck…fast.





Posted on [Instagram](https://www.instagram.com/p/BCkz5SNCmFA/) [7:45 am, March 5, 2016](http://dentedreality.com.au/2016/03/05/i-want-breck-fast/ "7:45 am") 
jQuery(document).ready(function(){
var gmap\_m82e2ebf47685db4342f30f8297cdbd23 = {
positions : {
503 : new google.maps.LatLng( '39.4811395', '-106.066706' )
},
bounds : new google.maps.LatLngBounds(), // empty for now, we'll dynamically extend it later
map : new google.maps.Map(
document.getElementById( 'gmap\_m82e2ebf47685db4342f30f8297cdbd23' ),
{
mapTypeId: google.maps.MapTypeId.ROADMAP,
center: new google.maps.LatLng( 0, 0 ),
zoom: 16 // Seems to be a good zoom for a single point
}
),
markers : {},
}; // end of gmap
// Extend the bounds of interest based on our positions
for ( var m in gmap\_m82e2ebf47685db4342f30f8297cdbd23.positions ) {
gmap\_m82e2ebf47685db4342f30f8297cdbd23.bounds.extend( gmap\_m82e2ebf47685db4342f30f8297cdbd23.positions[m] );
}
// Render markers
for ( var m in gmap\_m82e2ebf47685db4342f30f8297cdbd23.positions ) {
gmap\_m82e2ebf47685db4342f30f8297cdbd23.markers[m] = new google.maps.Marker( {
clickable: true,
map : gmap\_m82e2ebf47685db4342f30f8297cdbd23.map,
position : gmap\_m82e2ebf47685db4342f30f8297cdbd23.positions[m]
} );
}
// Redraw map to fit our new marker-based bounds
gmap\_m82e2ebf47685db4342f30f8297cdbd23.map.setCenter( gmap\_m82e2ebf47685db4342f30f8297cdbd23.positions[503] );
});
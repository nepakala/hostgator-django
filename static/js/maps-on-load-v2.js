var test = "";

d3.json("http://tools.newbreedmarketing.com/static/data/us-states.topojson", function(data) {
    geoJson = data;
    stateFeatures = topojson.feature(geoJson,geoJson.objects.states).features;
    plot();
});

var figure = d3.select("#usmapdiv");
var geoJson;
var projection;

var plot = function() {
    /* 
       plot the state map!

       drawMap(figure,geoJson);
       -figure is a d3 selection
       -geoJson is the loaded us-states file
       -stateHapps is the loaded csv (state,val)
    */

    //Width and height
    var w = parseInt(figure.style('width'));
    var h = w*650/900;

    // remove an old figure if it exists
    figure.select(".canvas").remove();

    //Create SVG element
    var canvas = figure
	.append("svg")
	.attr("class", "map canvas")
	.attr("id", "mapsvg")
	.attr("width", w)
	.attr("height", h);
    
    //Define map projection
    projection = d3.geo.albersUsa()
	.translate([w/2, h/2])
	.scale(w*1.3);
    //.scale(1000);

    //Define path generator
    var path = d3.geo.path()
	.projection(projection);

    stateFeatures = topojson.feature(geoJson,geoJson.objects.states).features;

    //Bind data and create one path per GeoJSON feature
    var states = canvas.selectAll("path")
	.data(stateFeatures);
    
    states.enter()
	.append("path")
	.attr("d", function(d,i) { return path(d.geometry); } )
	.attr("id", function(d,i) { return d.properties.name; } )
    // .attr("class",function(d,i) { return "state map "+d.properties.name[0]+d.properties.name.split(" ")[d.properties.name.split(" ").length-1]+" "+"q"+classColor(sortedStateList[i])+"-8"; } )
    // .on("mousedown",state_clicked)
    // .on("mouseover",state_hover)
    // .on("mouseout",state_unhover);
        .style({
            "fill": "#A0AAB2",
            "stroke-width": "3px",
            "stroke": "#e7ecec",
        });

    states.exit().remove();

    states
	.attr("stroke","black")
	.attr("stroke-width",".7");

    function state_clicked(d,i) { 

    }

    function state_hover(d,i) { 

    }

    function state_unhover(d,i) { 

    }

//     <style type="text/css">
//         .st0{fill-rule:evenodd;clip-rule:evenodd;fill:#AD1F2B;}
// </style>
// <g id="sun">
//         <path class="st0" d="M32,15.7c-8.8,0-16,7.3-16,16.3c0,9,7.2,16.3,16,16.3S48,41,48,32C48,23,40.8,15.7,32,15.7z M62.5,26.4
//                 c-3.2-0.8-7.7-2.6-9.5-5.7c-1.8-3.2-1-8-0.1-11.2c0.5-1.8,0-2.3-1.7-1.4c-2.9,1.4-7.5,3.1-10.9,1.8c-3.4-1.3-5.9-5.5-7.2-8.5
//                 c-0.8-1.7-1.4-1.7-2.2,0c-1.3,3-3.8,7.2-7.2,8.5c-3.4,1.3-8-0.4-10.9-1.8c-1.7-0.8-2.2-0.4-1.7,1.4c0.9,3.2,1.7,8-0.1,11.2
//                 c-1.8,3.2-6.3,4.9-9.5,5.7c-1.8,0.5-1.9,1.1-0.4,2.2c2.7,1.9,6.4,5.1,7,8.7c0.6,3.6-1.7,7.9-3.6,10.6c-1.1,1.5-0.8,2.1,1.1,1.9
//                 c3.2-0.3,8.1-0.3,10.9,2.1c2.8,2.4,3.7,7.2,3.9,10.5c0.1,1.9,0.8,2.1,2.1,0.8c2.3-2.4,6-5.5,9.6-5.5s7.4,3.1,9.6,5.5
//                 c1.3,1.4,1.9,1.1,2.1-0.8c0.2-3.3,1.1-8.1,3.9-10.5c2.8-2.4,7.6-2.4,10.9-2.1c1.9,0.2,2.2-0.4,1.1-1.9c-1.9-2.7-4.3-7-3.6-10.6
//                 c0.6-3.6,4.3-6.8,7-8.7C64.5,27.5,64.4,26.8,62.5,26.4z M32,50.3c-9.9,0-17.9-8.2-17.9-18.3c0-10.1,8-18.3,17.9-18.3
//                 c9.9,0,17.9,8.2,17.9,18.3C49.9,42.1,41.9,50.3,32,50.3z"/>
// </g>

    // d3.xml("http://tools.newbreedmarketing.com/static/data/sun-icon.svg", "image/svg+xml", function(xml) {
    //     canvas.appendChild(xml.documentElement);
    // });
    var sun_path = "M32,15.7c-8.8,0-16,7.3-16,16.3c0,9,7.2,16.3,16,16.3S48,41,48,32C48,23,40.8,15.7,32,15.7z M62.5,26.4c-3.2-0.8-7.7-2.6-9.5-5.7c-1.8-3.2-1-8-0.1-11.2c0.5-1.8,0-2.3-1.7-1.4c-2.9,1.4-7.5,3.1-10.9,1.8c-3.4-1.3-5.9-5.5-7.2-8.5c-0.8-1.7-1.4-1.7-2.2,0c-1.3,3-3.8,7.2-7.2,8.5c-3.4,1.3-8-0.4-10.9-1.8c-1.7-0.8-2.2-0.4-1.7,1.4c0.9,3.2,1.7,8-0.1,11.2c-1.8,3.2-6.3,4.9-9.5,5.7c-1.8,0.5-1.9,1.1-0.4,2.2c2.7,1.9,6.4,5.1,7,8.7c0.6,3.6-1.7,7.9-3.6,10.6c-1.1,1.5-0.8,2.1,1.1,1.9c3.2-0.3,8.1-0.3,10.9,2.1c2.8,2.4,3.7,7.2,3.9,10.5c0.1,1.9,0.8,2.1,2.1,0.8c2.3-2.4,6-5.5,9.6-5.5s7.4,3.1,9.6,5.5c1.3,1.4,1.9,1.1,2.1-0.8c0.2-3.3,1.1-8.1,3.9-10.5c2.8-2.4,7.6-2.4,10.9-2.1c1.9,0.2,2.2-0.4,1.1-1.9c-1.9-2.7-4.3-7-3.6-10.6c0.6-3.6,4.3-6.8,7-8.7C64.5,27.5,64.4,26.8,62.5,26.4z M32,50.3c-9.9,0-17.9-8.2-17.9-18.3c0-10.1,8-18.3,17.9-18.3c9.9,0,17.9,8.2,17.9,18.3C49.9,42.1,41.9,50.3,32,50.3z";
    function spin(selection, duration) {
        selection.transition()
            .ease("linear")
            .duration(duration)
            .attrTween("transform", function() {
                return d3.interpolateString("scale(.25) rotate(0 32 32)", "scale(.25) rotate(360 32 32)");
            });

        setTimeout(function() { spin(selection, duration); }, duration);
    }
 
    canvas.append("g")
        .attr({"id": "sun",
               "transform": function(d,i) { return "translate("+(projection(locations[0])[0]-8)+","+(projection(locations[0])[1]-30)+")"; },
              })
        .append("path")
        .attr({"class": "st0",
               "d": sun_path,
              })
        .style({"fill-rule":"evenodd","clip-rule":"evenodd","fill":"#AD1F2B",})
        .call(spin,9000);
    
    canvas.selectAll("circle.installations")
        .data(locations)
        .enter()
        .append("circle")
        .attr({
            "cx": function(d,i) { return projection(d)[0]; },
            "cy": function(d,i) { return projection(d)[1]; },
            "r": 5,
            "fill": "#AD1F2B",
        })
        .on("mouseover",function(d,i) { d3.select(this).transition().attr("r",10); })
        .on("mouseout",function(d,i) { d3.select(this).transition().attr("r",5); })
        .on("mousedown",function(d,i) {
            console.log('#location'+i);
            $.magnificPopup.open({
                items: {
                    // src: '<div class="white-popup-block">Dynamically created popup</div>',
                    src: '#location'+i,
                    // type: 'inline'
                },
                // You may add options here, they're exactly the same as for $.fn.magnificPopup call
                // Note that some settings that rely on click event (like disableOn or midClick) will not work here
            }, 0);
            // alert(i);
        });
    

    // function resizemap() {
    //     w = parseInt(figure.style('width'));
    //     h = w*650/900;
    //     projection.translate([w/2, h/2]).scale(w*1.3);
    //     canvas.selectAll("path").attr("d",path);
    //     canvas.attr("width",w).attr("height",h);
    // };

    // d3.select(window).on("resize.map",resizemap);

};









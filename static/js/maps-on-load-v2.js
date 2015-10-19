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

    canvas.selectAll("circle.installations")
        .data(locations)
        .enter()
        .append("circle")
        .attr({
            "cx": function(d,i) { return projection(d)[0]; },
            "cy": function(d,i) { return projection(d)[1]; },
            "r": 5,
            "fill": "red",
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









//window.addEventListener( "load", makeTree );
function makeTree(data) {

    var response_data = JSON.parse(data);
    response_data = JSON.parse(response_data);
    console.log(response_data);

    var nodes = d3.hierarchy(response_data, d=>d.children);                //<1>
    d3.tree().size( [800,400] )( nodes );                     //<2>



    var g = d3.select( "#tree" ).append( "g" )                //<3>
        .attr( "transform", "translate(25, 25)" );

    var lnkMkr = d3.linkVertical().x( d=>d.x ).y( d=>d.y );   //<4>
    g.selectAll( "path" ).data( nodes.links() ).enter()       //<5>
        .append( "path" ).attr( "d", d=>lnkMkr(d) )
        .attr( "stroke", "blue" ).attr( "fill", "none" );

    g.selectAll("circle").data( nodes.descendants() ).enter() //<6>
        .append("circle").attr( "r", 8 )
        .attr( "cx", d=>d.x ).attr( "cy", d=>d.y )

     

    console.log(g.selectAll(".node"))
}


$(function(){
  plotConceptMap();
});
function plotConceptMap()
{
  d3.json("/downloads/files/collaboration.json", function(dataJson) {
    var plot = new ConceptMap("graph", "graph-info", dataJson);
  });
}

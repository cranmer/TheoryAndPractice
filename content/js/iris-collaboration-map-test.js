$(function(){
  plotCollaborationMap();
});
function plotCollaborationMap()
{
  d3.json("/downloads/files/test.json", function(dataJson) {
      var plot = new CollaborationMap("graph", "graph-info", dataJson);
  });
}

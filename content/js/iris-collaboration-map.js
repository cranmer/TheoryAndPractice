$(function(){
  plotCollaborationMap();
});
function plotCollaborationMap()
{
  d3.json("/downloads/files/collaboration-iris.json", function(dataJson) {
    var plot = new CollaborationMap("graph", "graph-info", dataJson);
  });
}

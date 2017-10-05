import bpy
from ... base_types import AnimationNode

class SeparateMeshNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SeparateMeshNode"
    bl_label = "Separate Mesh"

    def create(self):
        self.newInput("Mesh", "Mesh", "meshData", dataIsModified = True)
        self.newOutput("Vector List", "Vertex Locations", "vertexLocations")
        self.newOutput("Edge Indices List", "Edges Indices", "edgesIndices")
        self.newOutput("Polygon Indices List", "Polygons Indices", "polygonsIndices")

    def execute(self, meshData):
        return meshData.vertices, meshData.edges, meshData.polygons

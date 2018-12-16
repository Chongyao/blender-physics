bl_info = {
    "name" : "FLIP Fluids",
    "description": "A FLIP Fluid Simulation Tool for Blender",
    "author" : "Ryan Guy <ryan.l.guy[at]gmail.com>, Dennis Fassbaender <info[at]df-videos.de>",
    "version" : (0, 0, 1),
    "blender" : (2, 7, 8),
    "location" : "Properties > Physics > Marvel Physics",
    "warning" : "Still developing",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Animation"
}
import bpy

from . import(
    ui
)

def register():
    ui.register()

def unregister():
    ui.unregister()

bl_info = {
    "name": "Dopesheet. Select related groups",
    "author": "Artem Poletsky",
    "version": (1, 0, 0),
    "blender": (2, 82, 0),
    "location": "Dope sheet > Select > Select related groups",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}


import bpy


class SelectRelatedGroups(bpy.types.Operator):
    """Select related groups"""
    bl_idname = "action.select_related_groups_operator"
    bl_label = "Select related groups"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.object
        action = obj.animation_data.action

        for g in action.groups :
            for channel in g.channels :   # channel is fcurve
                for p in channel.keyframe_points :
                    if p.select_control_point :
                        g.select = True
                        continue
                    
        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    layout.separator()

    layout.operator_context = "INVOKE_DEFAULT"
    layout.operator(SelectRelatedGroups.bl_idname, text=SelectRelatedGroups.bl_label)

def register():
    bpy.utils.register_class(SelectRelatedGroups)
    
    bpy.types.DOPESHEET_MT_select.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SelectRelatedGroups)
    
    bpy.types.DOPESHEET_MT_select.remove(menu_func)


if __name__ == "__main__":
    register()

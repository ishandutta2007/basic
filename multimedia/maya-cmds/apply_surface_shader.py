# Last updated: 08-Apr-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# To create and apply a surface shader (with shader group)

# ALL YOU NEED TO DO:
# Provide the following:
#   obj = object name on which to apply the shader
#   shnm = name of the shader
#   sgnm = name of the shader group
# Mention material type in shadingNode command

# WARNING: this removes current selection if any

import maya.cmds as cmds

obj = 'mysphere0'
shnm = 'lambert0'
sgnm = 'lambert0SG'

cmds.sets(renderable = True, noSurfaceShader = True, empty = True, name = sgnm)
shm = cmds.shadingNode('lambert', asShader = 1, name = shnm)
cmds.connectAttr(shnm + '.outColor', sgnm + '.surfaceShader')
cmds.select(obj)
cmds.hyperShade(assign = shm)
cmds.select(obj, deselect = True)

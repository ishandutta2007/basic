# Last updated: 24-Mar-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# To make material fade in and out at specified frame ranges

# ALL YOU NEED TO DO:
# Call fadeinout() function with:
#   mtr = material
#   fr = list of frame numbers in the format [[f0, f1], [f2, f3], ...]
#   pc = 
# An undoappear() function is provided which deletes all the keys
#   provided in the same fr

import maya.cmds as cmds

def appear(mat, fr):
    cmds.setKeyframe(obj, time = 0, attribute = 'visibility', value = 0)
    for f in fr:
        cmds.setKeyframe(obj, time = f[0], attribute = 'visibility', value = 1)
        cmds.setKeyframe(obj, time = f[1], attribute = 'visibility', value = 0)

# To remove all visibility keys set between f0 and f1
def undoappear(obj, fr):
    cmds.cutKey(obj, time = (0, 0), attribute = 'visibility')

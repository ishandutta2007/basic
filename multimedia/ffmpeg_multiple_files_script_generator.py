# Last updated: 25-Apr-2022
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Code to write ffmpeg script that can work on several files
# on which same operations need to be applied. This can be useful
# in encoding TV episodes

# ALL YOU NEED TO DO
# Specify following inputs:
#   bfln = output script filename that will contain ffmpeg commands (str)
#   ffaddr = location of ffmpeg, if it is in path simply use ffmpeg (str)
#   destination = path of folder where output media will be written, make
#                 sure it ends with / or \, leave blank to use current folder (str)
#   fyls = list of input files to be encoded (list of str)
#   ffops = ffmpeg options, check below for some help on what options to use (str)
#   nms = new names of output files, set '' to use original names (str or list of str)
#   nmprfx = prefix to use for new names, set as (c0, n, c1) where c0 and c1 are prefix and suffix
#            of numbering that starts from n, set n=-1 to ignore this option (list or tuple)

# ffmpeg options
# check https://ffmpeg.org/ffmpeg.html for detailed explanations
# or check ffmpeg_basic_encoding_commands.md for some options that I've used

import math
import glob

# INPUT
bfln = 'ffmpeg_encoder.bat'    # filename in which ffmpeg commands will be written
ffaddr = '"C:\\ffmpeg\\bin\\ffmpeg.exe"'    # location of ffmpeg
destination = 'E:\\Videos\\'    # path of folder where output media files will be written
fyls = ['a.mp4', 'b.mp4', 'c.mp4']    # glob.glob('path-to-folder-of-input-files\\*.mp4')
ffops = '-vcodec libx264 -acodec aac -preset veryslow'    # options for ffmpeg
nms = ['x', 'y', 'z']    # new names of output media files (without extension)
nmprfx = ('', 0, '. ')    # prefix numbering of output media files
ext = 'mkv'    # extension for all output media files

nf = len(fyls)
if type(nms) == str:    # If nms=='', new names are set to original names
    nms = []
    for i in range(nf):
        islsh = max(fyls[i].rfind('/'), fyls[i].rfind('\\'))
        idot = fyls[i].rfind('.')
        nms.append(fyls[i][islsh+1:idot] + '.' + ext)
else:    # Adding extension ext to new names
    nms = [nm + '.' + ext for nm in nms]
if nmprfx[1] > -1:    # Prefix numbering added to new names
    nz = 1 + int(math.log10(nf + nmprfx[1] - 1))
    nms = [nmprfx[0] + str(i+nmprfx[1]).zfill(nz) + nmprfx[2] + nms[i] for i in range(len(nms))]
print('Names of new files will be:')
for nm in nms:
    print(nm)
bfl = open(bfln, 'w')
for i in range(nf):
    bfl.write(ffaddr + ' -i "' + fyls[i] + '" ' + ffops + ' "' + destination + nms[i] + '"\n')
bfl.close()
print('check and manually run ' + bfln)

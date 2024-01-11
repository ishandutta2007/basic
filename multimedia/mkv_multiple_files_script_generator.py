# Last updated: 25-Apr-2022
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Code to write mkvmerge script that can work on several files
# on which same operations need to be applied. This can be useful
# in muxing TV episodes

# ALL YOU NEED TO DO
# Specify following inputs:
#   bfln = output script filename that will contain mkvmerge command (str)
#   mmaddr = location of mkvmerge, if it is in path simply use mkvmerge (str)
#   destination = path of folder where output media will be written, make
#                 sure it ends with / or \, leave blank to use current folder (str)
#   fyls = list of input files to be muxed, use append to add different sets of files,
#          all sets should have same number of files (list of list of str)
#   mmgops = mkvmerge global options, check below for some help on what options to use (str)
#   mmiops = mkvmerge options for each set of input files, check below for some help on
#            what options to use. its size should be same as fyls (list or tuple)
#   nms = new names of output files, set '' to use original names (str or list of str)
#   nmprfx = prefix to use for new names, set as (c0, n, c1) where c0 and c1 are prefix and suffix
#            of numbering that starts from n, set n=-1 to ignore this option (list or tuple)

# mkvmerge options
# check https://mkvtoolnix.download/doc/mkvmerge.html for detailed explanations

# Each str in mmiops will give mkvmerge input file options to that set of files
# Inclusion/exclusion of tracks:
#   -s 2, only uses subtitle track 2
#   -a hin,eng only uses hindi and english audio tracks
#   -a 2,3,4, only uses audio tracks 2,3,4
#   -a !1, uses all audio tracks except 1
#   Track IDs of streams can be checked using mkvmerge --identify filename (I think  MediaInfo shows +1),
#   they are usually 0 for video, 1 onwards for audio and later for subtitles
#   use -a for audio, -s for subtitle, -d for video, -m for attachments
# To exclude all tracks of particular type:
#   --no-audio, --no-video, --no-subtitles, --no-chapters, --no-attachments, --no-global-tags
# Language tag of tracks can be set using:
#   --language 0:eng, sets language eng for track ID 0
# To include chapters file for each input file, load chapters
#   files in fyls and set '--chapters' in corresponding mmiops

# In global options mmgops, track order can be defined as:
#   --track-order 0:0,0:2,1:4, sets first track of output
#   file as first track from first input file, then next track is
#   third track from first input file, then next track is fifth track
#   from second file. order of other tracks is automatically decided
#   after ordering these

import math
import glob

# INPUT
bfln = 'matroska_muxer.bat'
mmaddr = '"C:\\Program Files\\MKVToolNix\\mkvmerge.exe"'
destination = ''    # path of folder where output media files will be written, ending with slash
fyls = []
fyls.append(['a.mp4', 'b.mp4', 'c.mp4'])    # glob.glob('path-to-folder-of-input-files\\*.mp4')
fyls.append(['a.srt', 'b.srt', 'c.srt'])    # glob.glob('path-to-folder-of-input-files\\Subs\\*.srt')
mmgops = '--track-order 0:1,0:0,1:0'
mmiops = ('-a hin -s 2', '')
nms = ['x', 'y', 'z']    # new names of output media files (without extension)
nmprfx = ('', 1, '. ')
ext = 'mkv'    # use mka for audio files

nf = len(fyls)
nf0 = len(fyls[0])
if type(nms) == str:    # If nms=='', new names are set to original names
    nms = []
    for i in range(nf0):
        islsh = max(fyls[0][i].rfind('/'), fyls[0][i].rfind('\\'))
        idot = fyls[0][i].rfind('.')
        nms.append(fyls[0][i][islsh+1:idot] + '.' + ext)
else:    # Adding extension ext to new names
    nms = [nm + '.' + ext for nm in nms]
if nmprfx[1] > -1:    # Prefix numbering added to new names
    nz = 1 + int(math.log10(nf0 + nmprfx[1] - 1))
    nms = [nmprfx[0] + str(i+nmprfx[1]).zfill(nz) + nmprfx[2] + nms[i] for i in range(len(nms))]
print('Names of new files will be:')
for nm in nms:
    print(nm)
bfl = open(bfln, 'w')
for i in range(nf0):
    bfl.write(mmaddr + ' -o "' + destination + nms[i] + '" ' + mmgops)
    for k in range(nf):
        bfl.write(' ' + mmiops[k] + ' "' + fyls[k][i] + '"')
    bfl.write('\n')
bfl.close()
print('check and manually run ' + bfln)

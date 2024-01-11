# Last updated: 23-Apr-2022
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Code to write ffmpeg script that combines several images and
# audios into single video file. This can be useful to convert a
# presentation and recorded audios into video.

# ALL YOU NEED TO DO
# Specify following inputs:
#   bfln = output script filename that will contain ffmpeg command (str)
#   ffaddr = location of ffmpeg, if it is in path simply use ffmpeg (str)
#   ifyls = list of images (list of str)
#   afyls = list of audios (list of str)
#   vfln = output video filename (str)

# NOTES
# Images are assumed to be of same attributes (like dimensions)
# One audio file is assumed to run with one image file, in order
# The ffmpeg options can be changed, currently they feature:
#   -preset veryslow for best compression
#   x264 and aac codecs, but some other like vp9, av1 and opus might be better
#   -b:a set audio bitrate to 64kbps
#   -r 2 sets video to 2 frames per second
#   -ar 44100 sets audio sample rate to 44.1kHz
# Recording audios might not have balanced volumes, so audio is encoded again
#   using dynaudnorm filter, though I'm not sure how well it works

import platform
import glob

# INPUT
bfln = 'ffmpeg_videomaker.bat'
ffaddr = '"C:\\ffmpeg\\bin\\ffmpeg.exe"'
ifyls = glob.glob('*.png')
afyls = glob.glob('*.ogg')
vfln = 'out.mp4'

n = len(ifyls)
bfl = open(bfln, 'w')
bfl.write(ffaddr)
for i in range(n):
    bfl.write(' -i ' + ifyls[i] + ' -i ' + afyls[i])
bfl.write(' -filter_complex "')
for i in range(n):
    bfl.write('[{}:0][{}:0]'.format(2*i, 2*i+1))
bfl.write('concat=n={}:v=1:a=1[outv][outa]"'.format(n))
bfl.write(' -r 2 -c:v libx264 -pix_fmt yuv420p -preset veryslow -tune stillimage -c:a aac -b:a 320k -map "[outv]" -map "[outa]" tmp_' + vfln + '\n')
bfl.write(ffaddr + ' -i tmp_' + vfln + ' -preset veryslow -c:v copy -c:a aac -ar 44100 -b:a 64k -filter:a dynaudnorm ' + vfln + '\n')
if platform.system() == 'Windows':
    bfl.write('del tmp_' + vfln + '\n')
else:
    bfl.write('rm tmp_' + vfln + '\n')
bfl.close()

print('manually run', bfln, 'to make video')

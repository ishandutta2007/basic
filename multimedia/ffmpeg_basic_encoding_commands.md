Last updated: 07-May-2023

Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)

Source: https://github.com/udy11, https://gitlab.com/udy11

This document is compilation of commands that I often use in encoding media files using [ffmpeg](https://ffmpeg.org/). Check official documents to customize as per your requirements.

### **The Basic Syntax**
All commands have a basic structure:
```
ffmpeg -i input_file_name -ffmpeg-options output_file_name
```
Here, `ffmpeg` can be replaced with full path of executable like `\usr\bin\ffmpeg` or `C:\ffmpeg\bin\ffmpeg.exe`. `input_file_name` and `output_file_name` can be given with full path. Multiple input files can be loaded using `-i` multiple times. Use double quotes if there is space in filenames.

### **General Help**
1. `-vn`, `-an`, `-sn`, `-map_chapters -1`, `-map_metadata -1` to exclude all video, audio, subtitle, chapters, metadata respectively. Use `-vcodec copy` and `-acodec copy` to copy video and audio streams without encoding.
2. Use `-preset veryslow` for best compression, but encoding will take long time.
3. If encoding from a 10-bit video to video playable in old TVs or players, its chroma sampling needs to be changed, use `-pix_fmt yuv420p` option.
4. To include only specific tracks, use `-map n:s:t` syntax, where `n` is input file number (`0` for first file), `s` is stream type (`v` for video, `a` for audio, `s` for subtitle), `t` is track number. Ignore `:t` to include all tracks of that type. For example, to only include first video, third audio and first two subtitle tracks from one input file, use `-map 0:v:0 -map 0:a:2 -map 0:s:0 -map 0:s:1`.
5. To include streams by specific attributes, for example, to include the video track and all hindi language audio tracks, use `-map 0:v:0 -map 0:a:m:language:hin`. Similarly, use `-` before `0:a:m:language:hin` to include all audio except the ones with hindi language.
6. To trim media, use `-ss start_time` before `-i` and `-t duration` after `input_file_name`, for example: `ffmpeg -ss 00:01:23.965 -i ifl.mp4 -t 00:02:00 -vcodec copy -acodec copy ofl.mkv` cuts the video from 00:01:23.965 with duration 2 minutes. If both audio and video are not re-encoded, then trimming is done by keyframes, which can be pre-identified in a media player. Ignore `-t` option to go till the end of the media.
7. To crop video starting from coordinates `x,y`, width `w` (right of `x`) and height `h` (down of `y`) use option `-filter:v "crop=x:y:w:h"`. `0,0` is the top-left corner.
8. To split the file in segments of equal durations, use `-f segment -segment_time 00:10:00 -reset_timestamps 1` and provide output filename template lik `vid%02d.mp4` (so output files will be vid00.mp4, vid01.mp4, ...).

### **Encoding video with libsvtav1**
Check [ffmpeg guide](https://trac.ffmpeg.org/wiki/Encode/AV1) for encoding with AV1. Lower `crf` basically represents better video quality, 22-30 should be good enough for general purpose. `preset` is a tradeoff between encoding speed and compression efficiency, 6-8 should be good enough, go lower to improve compression but encoding may take very long. `tune=0` turns on PSNR, though I'm not exactly sure when it is useful.
```
ffmpeg -i input_file_name -vcodec libsvtav1 -crf 24 -preset 6 -svtav1-params tune=0 -acodec copy output_file_name
```

### **Encoding audio with flac**
Following copies video and encodes audio with flac with best compression.
```
ffmpeg -i input_file_name -vcodec copy -acodec flac -compression_level 12 output_file_name
```

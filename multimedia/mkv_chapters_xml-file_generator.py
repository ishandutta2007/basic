# Last updated: 23-Apr-2022
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Code to generate xml attachment file to specify chapters in mkv/mka file using ordered chapters
# Check this for more details: https://matroska.org/technical/chapters.html

# ALL YOU NEED TO DO:
# Call function mkchap with following inputs:
#   t0s = Starting times of all chapters (list)
#   t1s = Ending times of all chapters (list)
#   ordered = sets EditionFlagOrdered, forces media to play in order of chapters (bool, optional)
#   chtitles = chapter titles (list/str, optional)
#   chlangs = chapter languages (list/str, optional)
#   ofln = output xml file name (str, optional)
# Output is file generated with name ofln

# NOTE:
# Time format in t0s and t1s should be valid, precision of seconds can only be upto nanoseconds (9 digits after decimal)
# Chapter language tags in chlangs should be valid
# Chapter titles and languages are optional
# If chlangs is type str, same language is applied to all chapters; same for chtitles but it'll usually be desirable to have different titles
# EditionUID and ChapterUID are useful in linking different files, they should be unique for which 64-bit random integers are used
# ChapterFlagHidden and ChapterFlagEnabled are used in hiding and disabling/enabling a chapter, better to leave them as they are
# Use mkvmerge to attach the generated xml file while muxing mkv/mka file

import random

def mkchap(t0s, t1s, ordered = False, chtitles = '', chlangs = '', ofln = 'chapters.xml'):
    ofl = open(ofln, 'w', encoding = 'utf-8')
    ofl.write('<?xml version="1.0" encoding="UTF-8"?>\n\n')
    ofl.write('<Chapters>\n')
    ofl.write('  <EditionEntry>\n')
    ofl.write('    <EditionUID>{}</EditionUID>\n'.format(random.getrandbits(64)))
    ofl.write('    <EditionFlagOrdered>{}</EditionFlagOrdered>\n'.format(int(ordered)))

    n = len(t0s)
    if type(chtitles) == str:
        chts = [chtitles for i in range(n)]
    else:
        chts = chtitles
    if type(chlangs) == str:
        chls = [chlangs for i in range(n)]
    else:
        chls = chlangs

    for i in range(n):
        ofl.write('\n    <ChapterAtom>\n')
        ofl.write('      <ChapterUID>{}</ChapterUID>\n'.format(random.getrandbits(64)))
        ofl.write('      <ChapterTimeStart>{}</ChapterTimeStart>\n'.format(t0s[i]))
        ofl.write('      <ChapterTimeEnd>{}</ChapterTimeEnd>\n'.format(t1s[i]))
        if chts[i] != '':
            ofl.write('      <ChapterDisplay>\n')
            ofl.write('        <ChapterString>{}</ChapterString>\n'.format(chts[i]))
            if chls[i] != '':
                ofl.write('        <ChapterLanguage>{}</ChapterLanguage>\n'.format(chls[i]))
            ofl.write('      </ChapterDisplay>\n')
        ofl.write('      <ChapterFlagHidden>0</ChapterFlagHidden>\n')
        ofl.write('      <ChapterFlagEnabled>1</ChapterFlagEnabled>\n')
        ofl.write('    </ChapterAtom>\n')

    ofl.write('\n  </EditionEntry>\n')
    ofl.write('</Chapters>\n')
    ofl.close()

if __name__ == '__main__':
    t0s = ['00:00:00',
           '00:01:32.5508842',
           '00:02:00']
    t1s = ['00:01:32.5508842',
           '00:02:00',
           '00:03:22.834967443']
    cht = ['Intro', '日本語', 'Outro']
    chl = ['eng', 'ja', 'eng']
    ofln = 'chapters.xml'

    mkchap(t0s, t1s, ordered = False, chtitles = cht, chlangs = chl, ofln = ofln)

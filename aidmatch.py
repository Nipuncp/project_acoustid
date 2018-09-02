from __future__ import print_function
# This file is part of pyacoustid.
# Copyright 2011, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""Example script that identifies metadata for files specified on the
command line.
"""
import acoustid
import sys
import os
# API key for this demo script only. Get your own API key at the
# Acoustid Web for your application.
# http://acoustid.org/
API_KEY = 'cSpUJKpD'


# Python 2/3 Unicode compatibility: this `print_` function forces a
# unicode string into a byte string for printing on Python 2, avoiding
# errors in the process, and does nothing on Python 3, where
# stdout/stderr are text streams (and there's not much we can do about
# that).
if sys.version_info[0] < 3:
    def print_(s):
        print(s.encode(sys.stdout.encoding, 'replace'))
else:
    def print_(s):
        print(s)

path = "/home/dayscholars/Desktop"
def aidmatch(filename):
    try:
        results = acoustid.match(API_KEY, filename)
    except acoustid.NoBackendError:
        print("chromaprint library/tool not found", file=sys.stderr)
        sys.exit(1)
    except acoustid.FingerprintGenerationError:
        print("fingerprint could not be calculated", file=sys.stderr)
        sys.exit(1)
    except acoustid.WebServiceError as exc:
        print("web service request failed:", exc.message, file=sys.stderr)
        sys.exit(1)
    #print(results)
    #first = True
    for score, rid, title, artist in results:
         return artist, title

def file_rename(file_path, meta):
    if not os.path.isdir(path +'/'+meta[0]):
        os.mkdir(os.path.join(path, meta[0]))
    os.rename(file_path, '/home/dayscholars/Desktop/'+meta[0]+'/'+meta[1]+'.mp3')

def list_mp3(d_path):
    s = []
    for file in os.listdir(d_path):
        if file.endswith(".mp3"):
            s.append(os.path.join(d_path, file))   
    #print(s)
    return s

        
if __name__ == '__main__':
    print("Welcome. This is a program for sorting and renaming mp3 files bu using acoustid web service")
    print("Enter the directory path for which you want to sort and rename mp3s")
    directory_path = input("-->") 
   # directory_path = "/home/dayscholars/Desktop/lyceaum_exrecises/project_acoustic/pyacoustid"
    mp3_files = list_mp3(directory_path)
    for i in mp3_files:
        #s = mp3_files.pop()
        t = aidmatch(i)
        if t:
            print(i, t)
            file_rename(i, t)
        else:
            print(i + " not found in database")
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import struct
from fuzzywuzzy import fuzz

if sys.version_info >= (3,0):
    import urllib.request
    from xmlrpc.client import ServerProxy, Error
else: # python2
    import urllib2
    from xmlrpclib import ServerProxy, Error
	
server = ServerProxy('http://api.opensubtitles.org/xml-rpc')

def superPrint(priority, title, message):
    """Print messages through terminal, zenity or kdialog"""
    if gui == 'gnome':
        if title:
            subprocess.call(['zenity', '--' + priority, '--title=' + title, '--text=' + message])
        else:
            subprocess.call(['zenity', '--' + priority, '--text=' + message])
    else:
        # Clean up formating tags from the zenity messages
        message = message.replace("\n\n", "\n")
        message = message.replace("<i>", "")
        message = message.replace("</i>", "")
        message = message.replace("<b>", "")
        message = message.replace("</b>", "")
        message = message.replace('\\"', '"')
        
        # Print message
        print(">> " + message)

def hashFile(path):
    """Produce a hash for a video file: size + 64bit chksum of the first and 
    last 64k (even if they overlap because the file is smaller than 128k)"""
    try:
        longlongformat = 'Q' # unsigned long long little endian
        bytesize = struct.calcsize(longlongformat)
        format = "<%d%s" % (65536//bytesize, longlongformat)
        
        f = open(path, "rb")
        
        filesize = os.fstat(f.fileno()).st_size
        hash = filesize
        
        if filesize < 65536 * 2:
            print "File size error while generating hash for this file:\n" + path
            sys.exit(0)
        
        buffer = f.read(65536)
        longlongs = struct.unpack(format, buffer)
        hash += sum(longlongs)
        
        f.seek(-65536, os.SEEK_END) # size is always > 131072
        buffer = f.read(65536)
        longlongs = struct.unpack(format, buffer)
        hash += sum(longlongs)
        hash &= 0xFFFFFFFFFFFFFFFF
        
        f.close()
        returnedhash = "%016x" % hash
        return returnedhash
    
    except IOError:
        print "Input/Output error while generating hash for this file: " + path

def mkScore(a, b):
	return fuzz.ratio(a, b)

def main(args):
	try:
		session = server.LogIn(args['username'], args['password'], 'en', 'opensubtitles-download 3.2')
	except:
		print "cant connect"
		sys.exit(0)
		
	if session['status'] != '200 OK':
		print "Opensubtitles.org servers refused the connection: " + session['status'] + ".\n\nPlease check:\n- Your Internet connection status\n- www.opensubtitles.org availability\n- Your 200 downloads per 24h limit"
		sys.exit(1)
	
	filePath = args['path']
	videoHash = hashFile(filePath)
	videoSize = os.path.getsize(filePath)
	fileName = os.path.basename(os.path.splitext(filePath)[0])
	
	print "=====================================\nFileName: " + fileName + "\nPath: " + filePath + "\n====================================="
	
	try:
		data = server.SearchSubtitles(session['token'], [{'moviehash':videoHash, 'moviebytesize':str(videoSize)}])
	except Exception:
		print "Unable to reach opensubtitles.org servers!"

	if data:
		score = []
		for a in data['data']:
			MovieReleaseName = a['MovieReleaseName'].strip()
			SubFileName = os.path.splitext(a['SubFileName'])[0].strip()
			MovieReleaseNameScore = mkScore(fileName, MovieReleaseName)
			SubFileNameScore = mkScore(fileName, SubFileName)

			if MovieReleaseNameScore > SubFileNameScore:
				score.append([MovieReleaseNameScore, MovieReleaseName])
			else:
				score.append([SubFileNameScore, SubFileName])
		
		newscore = []	
		for i in score:
			if i not in newscore:
				newscore.append(i)
			else:
				for j in newscore:
					if i[1] == j[1]:
						j[0] += 2

		for s in sorted(newscore, reverse=True):
			print s[1] + " (Score: " + str(s[0]) + ")"
	else:
		print "Found no matches for " + fileName
	
	if session['token']:
		server.LogOut(session['token'])

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Lookup (orginal) filenames using hashed values on Opensubtitles.com')
	parser.add_argument('-user','--username', help='Opensubtitles username', required=True)
	parser.add_argument('-pass','--password', help='Opensubtitles password', required=True)
	parser.add_argument('-p','--path', help='Absolute path to media fule', required=True)
	args = vars(parser.parse_args())
	
	main(args)
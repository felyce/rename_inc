#!/usr/bin/python
# -*- coding:utf-8; mode: python-mode -*-

# First Write:2009/6/30
# Last Change:2009/07/16 21:38:30.

import os
import sys
sys.path.append('~/Python/lib')

import util

class Rename_inc(object):

    def __init__(self, param):

        self.argv, self.file_list = util.getParam( param )

# incremant start number
        self.start = 0

# Pre word
        self.header = ""

# tail word
        self.tail = ""

# ext
        self.ext = ""

# this is name of file.
# if re_name is None, using unchanged name.
# -s or --start, re_name became incremented number.
# -n or --name, re_name become Parameter.
        self.re_name = ""

        if not len( self.file_list ):
            _help()

        # Parameter '-s' and '--start' are number of first
        if '-s' in self.argv:
            self.start = self.argv['-s']
        elif '--start' in self.argv:
            self.start = self.argv['--start']

        # header word
        elif '--header' in self.argv:
            self.header = self.argv['--header']

        # tail word
        elif '--tail' in self.argv:
            self.tail = self.argv['--tail']
        
        if '--ext' in self.argv:
            self.ext = self.argv['--ext']

        if '-n' in self.argv:
            self.re_name = self.argv['-n']
        elif '--name' in self.argv:
            self.re_name = self.argv['--name']

        if '-h' in self.argv:
            _help()
        elif '--help' in self.argv:
            _help()

        if self.start and self.re_name:
            print 'Can not Set Parameter same time.You MUST choice -s[--start] or -n[--name].'
            sys.exit()


    def run(self):

        for i in range( len( self.file_list ) ):
            name, ext = os.path.splitext( self.file_list[i] )

            # first, self.ext is none.
            # second, --ext param.
            # last, if self.ext is none(no parameter), set current ext.
            if not self.ext:
                # file have ext.
                if ext:
                    self.ext = ext
                # don't have ext.
                else:
                    pass

            # if start is empty?
            if self.start:
                # at first, re_name is none.
                # next, -n or --name option.
                # at last, belong. no change name.
                if self.re_name:
                    self.re_name = self.file_list[i]
            else:
                self.re_name = str( i + self.start )

#            print "header:%s\nre_name:%s\ntail:%s\next:%s" % \
#                    (self.header, self.re_name, self.tail, self.ext)

            os.rename( self.file_list[i] ,"%s%s%s%s" % ( self.header,
                                        self.re_name,
                                        self.tail,
                                        self.ext ) 
                                        #str( self.start )
                                        )

def _help():
    print """
    rename_inc [option] File...

    if You don't set -n or --name option,
                    This script rename NUMBER.

    option
    -h or --help
        this Text.

    -s or --start
        To use rename string number.
        Start number.
            -s 10
            10, 11, 12...

    --header
        Add words of front of rename string.

    --tail
        Append words of end of rename string.
    
    --ext
        Rename ext.

    -n or --name 
        Rename Name.
        Don't use -s[--start] option.
    """
    
    sys.exit()

def _main():
    rename_inc = Rename_inc(sys.argv[1:])
    rename_inc.run()

if __name__ == '__main__':
    if len( sys.argv ) == 1:
        print ( 'less parameter' )
        _help()

    _main()


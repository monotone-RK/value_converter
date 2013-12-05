#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************/
# Value Converter Written in Python Ver:1.0             2013.12.05 monotone-RK/
#*****************************************************************************/
import sys
from optparse import OptionParser


def usage():
    print "## Value Converter Written in Python"
    print "## Date:2013.12.05"
    print "## Usage: python valconv.py [options] value\n"
    print """Options:
  -h, --help     show this help message and exit
  -v, --version  Show the version
      --dec2bin  conversion format: dec -> bin
      --dec2oct  conversion format: dec -> oct
      --dec2hex  conversion format: dec -> hex
      --bin2oct  conversion format: bin -> oct
      --bin2dec  conversion format: bin -> dec
      --bin2hex  conversion format: bin -> hex
      --oct2bin  conversion format: oct -> bin
      --oct2dec  conversion format: oct -> dec
      --oct2hex  conversion format: oct -> hex
      --hex2bin  conversion format: hex -> bin
      --hex2oct  conversion format: hex -> oct
      --hex2dec  conversion format: hex -> dec"""


def version():
    print "Value Converter Written in Python v1.0  last upated:2013.12.05"


def valueconverter():
    if options.dec2bin:
        print "conversion format: dec -> bin"
        print "%s -> %s" % (args[0], bin(int(args[0])))
        sys.exit()
    elif options.dec2oct:
        print "conversion format: dec -> oct"
        print "%s -> %s" % (args[0], oct(int(args[0])))
        sys.exit()
    elif options.dec2hex:
        print "conversion format: dec -> hex"
        print "%s -> %s" % (args[0], hex(int(args[0])))
        sys.exit()
    elif options.bin2oct:
        print "conversion format: bin -> oct"
        print "%s -> %s" % (args[0], oct(int(args[0], 2)))
        sys.exit()
    elif options.bin2dec:
        print "conversion format: bin -> dec"
        print "%s -> %s" % (args[0], str(int(args[0], 2)))
        sys.exit()
    elif options.bin2hex:
        print "conversion format: bin -> hex"
        print "%s -> %s" % (args[0], hex(int(args[0], 2)))
        sys.exit()
    elif options.oct2bin:
        print "conversion format: oct -> bin"
        print "%s -> %s" % (args[0], bin(int(args[0], 8)))
        sys.exit()
    elif options.oct2dec:
        print "conversion format: oct -> dec"
        print "%s -> %s" % (args[0], str(int(args[0], 8)))
        sys.exit()
    elif options.oct2hex:
        print "conversion format: oct -> hex"
        print "%s -> %s" % (args[0], hex(int(args[0], 8)))
        sys.exit()
    elif options.hex2bin:
        print "conversion format: hex -> bin"
        print "%s -> %s" % (args[0], bin(int(args[0], 16)))
        sys.exit()
    elif options.hex2oct:
        print "conversion format: hex -> oct"
        print "%s -> %s" % (args[0], oct(int(args[0], 16)))
        sys.exit()
    elif options.hex2dec:
        print "conversion format: hex -> dec"
        print "%s -> %s" % (args[0], str(int(args[0], 16)))
        sys.exit()
    else:
        print "Please input an option(conversion format) you want"
        sys.exit()

optparser = OptionParser()
optparser.add_option("-v", "--version", action="store_true", dest="version",
                     default=False, help="Show the version")
optparser.add_option("--dec2bin", action="store_true", dest="dec2bin",
                     default=False, help="conversion format: dec -> bin")
optparser.add_option("--dec2oct", action="store_true", dest="dec2oct",
                     default=False, help="conversion format: dec -> oct")
optparser.add_option("--dec2hex", action="store_true", dest="dec2hex",
                     default=False, help="conversion format: dec -> hex")
optparser.add_option("--bin2oct", action="store_true", dest="bin2oct",
                     default=False, help="conversion format: bin -> oct")
optparser.add_option("--bin2dec", action="store_true", dest="bin2dec",
                     default=False, help="conversion format: bin -> dec")
optparser.add_option("--bin2hex", action="store_true", dest="bin2hex",
                     default=False, help="conversion format: bin -> hex")
optparser.add_option("--oct2bin", action="store_true", dest="oct2bin",
                     default=False, help="conversion format: oct -> bin")
optparser.add_option("--oct2dec", action="store_true", dest="oct2dec",
                     default=False, help="conversion format: oct -> dec")
optparser.add_option("--oct2hex", action="store_true", dest="oct2hex",
                     default=False, help="conversion format: oct -> hex")
optparser.add_option("--hex2bin", action="store_true", dest="hex2bin",
                     default=False, help="conversion format: hex -> bin")
optparser.add_option("--hex2oct", action="store_true", dest="hex2oct",
                     default=False, help="conversion format: hex -> oct")
optparser.add_option("--hex2dec", action="store_true", dest="hex2dec",
                     default=False, help="conversion format: hex -> dec")
(options, args) = optparser.parse_args()

if options.version:
    version()
    sys.exit()

if len(args) == 0:
    usage()
    sys.exit()

if len(args) != 1:
    print "Error! The number of arguments is wrong"
    sys.exit()

if __name__ == "__main__":
    valueconverter()

#!/usr/bin/env python

# Copyright 2007, Michael J. Harms
# This program is distributed under General Public License v. 3.  See the file
# COPYING for a copy of the license.

__description__ = \
"""
pdb_experiment.py

Extracts data about experimental procedure used to generate structure.
"""
__author__ = "Michael J. Harms"
__date__ = "080128"

from pdbtools.helper import cmdline
from pdbtools import exper

def main():
    """
    Function to call if run from command line.
    """
    cmdline.initializeParser(__description__,__date__)

    file_list, options = cmdline.parseCommandLine()

    out = []
    for pdb_file in file_list:

        f = open(pdb_file,'r')
        pdb = f.readlines()
        f.close()

        exp_data = exper.pdbExperiment(pdb)

        pdb_id = pdb_file[:pdb_file.index(".pdb")]
        pdb_id = os.path.split(pdb_id)[-1]

        out.append("%30s%s" % (pdb_id,exp_data))

    out = ["%10i%s\n" % (i,x) for i, x in enumerate(out)]
    out.insert(0,"%10s%30s%48s%40s%5s%10s%10s%10s\n" % (" ","pdb","protein",
               "organism","exp","res","r_value","r_free"))

    print "".join(out)


# If run from command line...
if __name__ == "__main__":
    main()

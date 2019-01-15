
import sys
import os

sitepath = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, sitepath)

from gevent.monkey import patch_all
patch_all()

from lg import app as application

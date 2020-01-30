import os
from avalon.vendor.Qt import QtWidgets
import avalon.api
import avalon.tvpaint

def main():
    # For the GUI-tools to work best, this should now become a QT-app:
    QT_APP = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    avalon.api.install(avalon.tvpaint)


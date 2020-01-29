import os
from avalon.vendor.Qt import QtWidgets
import avalon.api
import avalon.tvpaint
from pico import PicoApp
import importlib
from werkzeug.serving import run_simple
from werkzeug.wsgi import SharedDataMiddleware
from multiprocessing import Process


def start_picoserver():

    # load our module for pico (in the same folder as this script)
    modulepath = os.path.join(os.path.dirname(__file__), "tvp_pico.py")
    spec = importlib.util.spec_from_file_location("tvpaint", modulepath)
    tvpico = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tvpico)

    # lauch picoserver
    picoserver = PicoApp()
    picoserver.register_module(tvpico)

    # Although I want to use the pico-funcionality(the @expose-decoratorstuff)
    # I don't want to up the port in case of an exception.. so calling werkzeug
    # myself:
    picoserver = SharedDataMiddleware(picoserver, {'/': 'static'})
    run_simple('127.0.0.1', 4242, picoserver, use_debugger=False, use_reloader=False, threaded=False)

    # Old:
    # pico.server.run_app(picoserver, ip='127.0.0.1', port=4242, use_debugger=false,
    #                    use_reloader=false, threaded=false)



def main():
    # For the GUI-tools to work best, this should now become a QT-app:
    QT_APP = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    avalon.api.install(avalon.tvpaint)

    # start picoserver
    start_picoserver()

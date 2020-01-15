import avalon.api
import avalon.tvpaint
import pico.server
from pico import PicoApp
import importlib
import subprocess


def register():
    avalon.api.install(avalon.tvpaint)
    modulepath = "/home/kaspar/PROJECTS/avalon-core/setup/tvpaint/tvp_pico.py"
    spec = importlib.util.spec_from_file_location("tvpaint", modulepath)
    tvpico = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tvpico)

    app = PicoApp()
    app.register_module(tvpico)
    pico.server.run_app(app, use_reloader=False, threaded=False)


# test:
if __name__ == "__main__":
    register()


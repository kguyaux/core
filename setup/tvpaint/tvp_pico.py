"""
THis is the module that contains the methods that are called by the picoserver
that open a specific avaloon-tool(gui).
If you let this register this with the pico-app:
    app = PicoApp()
    app.register_module(<this module>)
    etc.

.. then it all gets loaded, and we have a litte webserver(api) that runs these
methods when they are called by requesting their URL

"""



from avalon.vendor.Qt import QtWidgets
from avalon.tools import contextmanager
from avalon.tools import loader
from avalon.tools import workfiles
from avalon.tools import publish
from avalon.tools import creator

import sys
import socket
import pyblish.api
import pico
import pytvpaint.functions as tvp

HOST = '127.0.0.1'  # The server's hostname or IP address
TVPLISTENERPORT = 8906        # The port used by the server
QT_APP = QtWidgets.QApplication.instance()

@pico.expose()
def openworkfiles():
    try:
        # url: `http://localhost:4242/api/context?project=jakub_projectx&asset=shot02&task=rotopaint&app=premiere`
        workfiles.show(debug=False)
        QT_APP.exec() # we are & should be, using the main-QT-application!
    except Exception as e:
        print(e)

    tvp.send_finish()
    return "Done"



@pico.expose()
def openloader():
    loader.show(debug=False)
    QT_APP.exec() # we are & should be, using the main-QT-application!
    tvp.send_finish()
    return "Done"


@pico.expose()
def opencreator():
    creator.show()
    QT_APP.exec() # we are & should be, using the main-QT-application!
    tvp.send_finish()
    return "Done"


@pico.expose()
def openpublish():
    # url: `http://localhost:4242/api/context?project=jakub_projectx&asset=shot02&task=rotopaint&app=premiere`
    publish.show()
    QT_APP.exec() # we are & should be, using the main-QT-application!
    tvp.send_finish()
    return "Done"

"""
@pico.expose()
def set_context(project, asset, task, app):
    # url: `http://localhost:4242/api/context?project=jakub_projectx&asset=shot02&task=rotopaint&app=premiere`
    
    os.environ["AVALON_PROJECT"] = project
    avalon.update_current_task(task, asset, app)
    project_code = pype.get_project_code()
    pype.set_project_code(project_code)
    hierarchy = pype.get_hierarchy()
    pype.set_hierarchy(hierarchy)
    fix_paths = {k: v.replace("\\", "/") for k, v in SESSION.items()
                 if isinstance(v, str)}
    SESSION.update(fix_paths)
    SESSION.update({"AVALON_HIERARCHY": hierarchy,
                    "AVALON_PROJECTCODE": project_code,
                    "current_dir": os.getcwd().replace("\\", "/")
                    })

    return SESSION
"""

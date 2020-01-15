from avalon.vendor.Qt import QtWidgets
from avalon.tools import contextmanager
from avalon.tools import workfiles

import sys
import socket
import pyblish.api
import pico

HOST = '127.0.0.1'  # The server's hostname or IP address
TVPLISTENERPORT = 8972        # The port used by the server
QT_APP = QtWidgets.QApplication.instance()


@pico.expose()
def openworkfiles():
    # url: `http://localhost:4242/api/context?project=jakub_projectx&asset=shot02&task=rotopaint&app=premiere`
    contextmanager.show()
    QT_APP.exec() # we are & should be, using the main-QT-application!
    workfiles.show(debug=True)
    QT_APP.exec() # we are & should be, using the main-QT-application!



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        msg = "set workfiles load_path <END>"
        s.connect((HOST, TVPLISTENERPORT))
        s.sendall(bytes(msg, encoding='ascii'))
        data = s.recv(1024)
        print('Received', str(data, encoding="utf-8"))
    return "Done"


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



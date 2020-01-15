from avalon.vendor.Qt import QtWidgets
from avalon.tools import contextmanager
from avalon.tools import workfiles
import sys
import socket
import pyblish.api
import pico

HOST = '127.0.0.1'  # The server's hostname or IP address
TVPLISTENERPORT = 8972        # The port used by the server


def _discover_gui():
    """Return the most desirable of the currently registered GUIs"""

    # Prefer last registered
    guis = reversed(pyblish.api.registered_guis())

    for gui in guis:
        try:
            gui = __import__(gui).show
        except (ImportError, AttributeError):
            continue
        else:
            return gui

    return None


def get_main_window():
    """Acquire Nuke's main window"""
    top_widgets = QtWidgets.QApplication.topLevelWidgets()
    name = "Foundry::UI::DockMainWindow"
    windows = [widget for widget in top_widgets if
                            widget.inherits("QMainWindow")]

    print("=====================================")
    print(top_widgets)


@pico.expose()
def openworkfiles():
    # url: `http://localhost:4242/api/context?project=jakub_projectx&asset=shot02&task=rotopaint&app=premiere`
    
    """
    app = QtWidgets.QApplication.instance()
    print("QTapp: ", str(app))

    if not app:
        print('creating new qapplication')
        app = QtWidgets.QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    """

    workfiles.show(debug=True)
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



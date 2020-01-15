"""Host API required for Work Files."""
#import tvpaint_avalon as tvpav
import socket
import os


HOST = '127.0.0.1'  # The server's hostname or IP address
TVPLISTENERPORT = 8972        # The port used by the server


def open_file(filepath):
    """To open a tvpaint-project we send a command to the TVPlistenerplugin
    The command sets a `tv_userstring`. Which can be read by 
    another TVPaint-function that probably is invoked by the user.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        msg = "set workfiles load_path \"%s\"" % filepath
        s.connect((HOST, TVPLISTENERPORT))
        s.sendall(bytes(msg, encoding='ascii'))
        data = s.recv(1024)
        print('Received', str(data, encoding="utf-8"))
    return True


def save_file(filepath):
    """Save a project to the avalonsilo.
    :filepath: the path of a local tvpaint-project
    :returns: destination-path if succeeded"""

    #path = filepath.replace("\\", "/")
    #nuke.scriptSaveAs(path)
    #nuke.Root()["name"].setValue(path)

    #nuke.Root()["project_directory"].setValue(os.path.dirname(path))
    #nuke.Root().setModified(False)
    #tvpav.save_file()


def current_file():
    """Return the path of the open scene file."""
    pass


def work_root():
    """Return the path of the workroot."""
    from avalon import api

    work_dir = api.Session["AVALON_WORKDIR"]
    scene_dir = api.Session.get("AVALON_SCENEDIR")
    if scene_dir:
        return str(Path(work_dir, scene_dir))
    return work_dir


def file_extensions():
    """Return the supported file extensions for tvpaint scene files."""
    return [".tvpp"]


def has_unsaved_changes():
    return False

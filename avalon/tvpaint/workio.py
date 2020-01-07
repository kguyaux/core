"""Host API required for Work Files."""
import tvpaint_avalon as tvpav


def open_file(filepath):
    """Open the scene file in tvpaint."""
    pass


def save_file(filepath):
    """Save a project to the avalonsilo.
    :filepath: the path of a local tvpaint-project
    :returns: destination-path if succeeded"""

    #path = filepath.replace("\\", "/")
    #nuke.scriptSaveAs(path)
    #nuke.Root()["name"].setValue(path)
    #nuke.Root()["project_directory"].setValue(os.path.dirname(path))
    #nuke.Root().setModified(False)

    tvpav.save_file()


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
    return True

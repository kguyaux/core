"""Pipeline integration functions."""
import sys

import pyblish.api
from avalon import api, schema
from ..lib import logger
from ..pipeline import AVALON_CONTAINER_ID

self = sys.modules[__name__]



def find_host_config(config):
    config_name = f"{config.__name__}.tvpaint"
    try:
        config = importlib.import_module(config_name)
    except ImportError as exc:
        if str(exc) != f"No module named '{config_name}'":
            raise
        config = None

    return config


def install(config):
    """Install TVPaint-specific functionality of avalon-core.

    It is called automatically when installing via `api.install(tvpaint)`.

    See the Maya equivalent for inspiration on how to implement this.

    """


    _set_project()
    pyblish.api.register_host("tvpaint")



def _set_project():
    """Sets the TVPproject project to the current Session's work directory.

    Returns:
        None

    """
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    sys.stdout.flush()
    workdir = api.Session["AVALON_WORKDIR"]

    try:
        os.makedirs(workdir)
    except OSError as e:
        # An already existing working directory is fine.
        if e.errno == errno.EEXIST:
            pass
        else:
            raise

    #cmds.workspace(workdir, openWorkspace=True)




def uninstall():
    """Uninstall all tha was installed

    This is where you undo everything that was done in `install()`.
    That means, removing menus, deregistering families and  data
    and everything. It should be as though `install()` was never run,
    because odds are calling this function means the user is interested
    in re-installing shortly afterwards. If, for example, he has been
    modifying the menu or registered families.

    """
    pyblish.api.deregister_host("tvpaint")


def _ls():
    containers = list()
    for identifier in (AVALON_CONTAINER_ID,
                       "pyblish.mindbender.container"):
        containers += lib.lsattr("id", identifier)
    return containers


def containerise(name,
                 namespace,
                 context,
                 loader=None,
                 data=None):
    """Bundle `node` into an assembly and imprint it with metadata

    Containerisation enables a tracking of version, author and origin
    for loaded assets.

    Arguments:
        node (nuke.Node): Nuke's node object to imprint as container
        name (str): Name of resulting assembly
        namespace (str): Namespace under which to host container
        context (dict): Asset information
        loader (str, optional): Name of node used to produce this container.

    Returns:
        node (nuke.Node): containerised nuke's node object

    """
    data = OrderedDict(
        [
            ("schema", "avalon-core:container-2.0"),
            ("id", AVALON_CONTAINER_ID),
            ("name", name),
            ("namespace", namespace),
            ("loader", str(loader)),
            ("representation", context["representation"]["_id"]),
        ],

        **data or dict()
    )

    lib.set_avalon_knob_data(node, data)

    return node


def ls():
    """List containers from active Maya scene

    This is the host-equivalent of api.ls(), but instead of listing
    assets on disk, it lists assets already loaded in Maya; once loaded
    they are called 'containers'

    """

    """
    container_names = _ls()

    has_metadata_collector = False
    config = find_host_config(api.registered_config())
    if hasattr(config, "collect_container_metadata"):
        has_metadata_collector = True

    for container in sorted(container_names):
        data = parse_container(container)

        # Collect custom data if attribute is present
        if has_metadata_collector:
            metadata = config.collect_container_metadata(container)
            data.update(metadata)

        yield data
    """
    yield { "id": "pyblish.avalon.container",
            "loader": "",
            "name": "modelDefault_01",
            "namespace": "Bruce_",
            "objectName": "Bruce_:rigDefault_CON",
            "representation": "59523f355f8c1b5f6c5e8348",
            "schema": "avalon-core:container-2.0"}



def load(asset, subset, version=-1, representation=None):
    """Load data into Maya

    This function takes an asset from the Loader GUI and
    imports it into Nuke.

    The function takes `asset`, which is a dictionary following the
    `asset.json` schema, a `subset` of the `subset.json` schema and
    an integer version number and a representation.

    Again, on terminology, see the Terminology chapter in the
    documentation, it'll have info on these for you.

    """

    return ""


def create(name, family, options=None):
    """Create new instance

    This function is called when a user has finished using the
    Creator GUI. It is given a (str) name, a (str) family and
    an optional dictionary of options. You can safely ignore
    the options for a first run and come back to it once
    everything works well.

    """

    return ""


def update(container, version=-1):
    """Update an existing `container` to `version`

    From the Container Manager, once a user chooses to
    update from one version to another, this function is
    called.

    It takes a `container`, which is a dictionary of the
    `container.json` schema, and an integer version.

    """


def remove(container):
    """Remove an existing `container` from Nuke scene

    In the Container Manager, when a user chooses to remove
    a container they've previously imported, this function is
    called.

    You'll need to ensure all nodes that cale along with the
    loaded asset is removed here.

    """

#def install(config):
#    """Install tvpaint-specific functionality of avalon-core.
#
#    This function is called automatically on calling `api.install(tvpaint)`.
#    """
#    pass
#
#
#def uninstall(config):
#    """Uninstall tvpaint-specific functionality of avalon-core.
#
#    This function is called automatically on calling `api.uninstall()`.
#
#    Args:
#        config: configuration module
#    """
#    pass
#
#
#def teardown():
#    """Remove integration"""
#    if not self._has_been_setup:
#        return
#
#    self._has_been_setup = False
#    logger.info("pyblish: Integration torn down successfully")
#
#
#
#
#def publish():
#    """Shorthand to publish from within host."""
#    import pyblish.util
#    return pyblish.util.publish()
#
#
#
#class Loader(api.Loader):
#    hosts = ["tvpaint"]
#
#    def __init__(self, context):
#        super().__init__(context)
#        self.fname = self.fname.replace(api.registered_root(), "$AVALON_PROJECTS")
#

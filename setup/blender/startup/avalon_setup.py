from avalon import api, blender


def main():
    """Register Avalon with Blender."""
    print("Registering Avalon...")
    api.install(blender)

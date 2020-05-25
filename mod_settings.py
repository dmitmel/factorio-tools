# https://wiki.factorio.com/Mod_settings_file_format
# https://forums.factorio.com/59851
# https://www.dropbox.com/sh/uscmj9y3cjfwpsr/AAD35_ZZu64EBi0awLA07fxga?dl=0
# https://github.com/credomane/factoriomodsettings/blob/master/src/FactorioModSettings.js

from pathlib import Path
import struct
import json
import property_tree


with open(Path.home() / ".factorio" / "mods" / "mod-settings.dat", "rb") as f:

    version_main, version_major, version_minor, version_developer = struct.unpack(
        "<HHHH", f.read(8)
    )

    always_false_flag = property_tree.read_bool(f)
    assert not always_false_flag

    deserialized_data = {
        "factorio_version": {
            "main": version_main,
            "major": version_major,
            "minor": version_minor,
            "developer": version_developer,
        },
        "data": property_tree.read(f),
    }

    print(json.dumps(deserialized_data, indent=2))

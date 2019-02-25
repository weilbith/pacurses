from constants.menu_names import MenuNames

from gui.menus.main import MainMenu
from gui.menus.volume import VolumeMenu
from gui.menus.mute import MuteMenu
from gui.menus.help import HelpMenu


_menu_mapping = {
    MenuNames.MAIN: MainMenu,
    MenuNames.VOLUME: VolumeMenu,
    MenuNames.MUTE: MuteMenu,
    MenuNames.HELP: HelpMenu,
}


def get_menu(name):
    if name not in _menu_mapping.keys():
        raise Exception("Invalid menu name: {0}".format(name))

    return _menu_mapping[name]

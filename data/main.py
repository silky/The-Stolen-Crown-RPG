from data.states.main_menu import main_menu
from data.states import shop, levels, battle
from . import setup, tools
from . import constants as c


TOWN = 'town'
MAIN_MENU = 'main menu'
CASTLE = 'castle'
HOUSE = 'house'
INN = 'Inn'
ARMOR_SHOP = 'armor shop'
WEAPON_SHOP = 'weapon shop'
MAGIC_SHOP = 'magic shop'
POTION_SHOP = 'potion shop'
PLAYER_MENU = 'player menu'
OVERWORLD = 'overworld'
BROTHER_HOUSE = 'brotherhouse'
BATTLE = 'battle'


def main():
    """Add states to control here"""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {MAIN_MENU: main_menu.Menu(),
                  TOWN: levels.LevelState(TOWN),
                  CASTLE: levels.LevelState(CASTLE),
                  HOUSE: levels.LevelState(HOUSE),
                  OVERWORLD: levels.LevelState(OVERWORLD, True),
                  BROTHER_HOUSE: levels.LevelState(BROTHER_HOUSE),
                  INN: shop.Inn(),
                  ARMOR_SHOP: shop.ArmorShop(),
                  WEAPON_SHOP: shop.WeaponShop(),
                  MAGIC_SHOP: shop.MagicShop(),
                  POTION_SHOP: shop.PotionShop(),
                  BATTLE: battle.Battle()
                  }

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()
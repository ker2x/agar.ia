"""https://github.com/Viliami/agario/blob/master/agar.py"""

import agaria


if __name__ == '__main__':
    print("Starting Agar.IA")
    game = agaria.Agaria(rendering=True)
    a = game.newPlayer()
    f = game.newFood()

    while game.is_running:
        game.update()
        game.render()
        obs = game.observation(a)

import BlackJackModel
import BlackJackView
import BlackJackController


def main():
    gameobject = BlackJackController.Game()
    viewobject = gameobject.view
    number_players = viewobject.number_of_players_prompt()
    name_players = viewobject.names_of_players(number_players)
    gameobject.get_players(name_players)
    gameobject.spawn_dealer()
    gameobject.turn_loop()



if __name__ == '__main__':
    main()

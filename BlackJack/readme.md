# Blackjack
_Students work as a group of to implement a kid-friendly version of Blackjack, or 21._

## Requirements
- Supports 1 - 5 players
- Uses 6 decks
- Keep track of number of hands each player has won
- Dealer is a Robot and always goes last
- The design of the program should leverage MVC
- Test Driven Development should be used for creation of the game, with all tests kept in the test folder
- Documentation of your functions and tests should be generated and live in the docs folder

### Rules of Kid-Friendly 21:
- No betting
- Aim of the 21 Card Game is to get 21 or as close to as possible.
- Number cards have their face value, jacks, kings and queens are worth 10. Ace can be either 1 or 11 and the player who holds the ace gets to choose the value of the card.
- The dealer and all other players have two cards. With the exception of the dealer the players have their cards face up. - The dealer has one card up and one card face down.
- The dealer goes to each player one at a time. The player needs to decide if they want another card (hit) or will sit on what they have. You can have as many cards as you like as long as you don’t go over 21.
- The dealer does this with every player. Players are not competing against each other, but against the dealer.
- The dealer then turns over their other card and needs to decide what to do. If the dealer has 16 or under then they must take another card.
- If the dealer has 21 (Ace and a ten value card) the dealer wins.
- If the dealer goes bust then everyone else wins.
- We reshuffle the deck of cards after every game.

import numpy as np


class BJGame:
    deck_cards_names = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    def __init__(self, n_decks):
        self.n_decks = n_decks
        self.deck = {x: 4 * self.n_decks for x in self.deck_cards_names if x != '10'}
        self.deck['10'] = 16 * self.n_decks

    def deal(self):
        probabilities = self.probs().values()
        selected_card = self.deck_cards_names[
            np.random.choice(len(self.deck_cards_names), p=np.array(list(probabilities)))]
        self.deck[selected_card] -= 1
        return selected_card

    def probs(self):
        number_of_cards = sum(self.deck.values())
        if number_of_cards == 0:
            raise ValueError("Deck empty, need to shuffle")
        return {card_name: nums / number_of_cards for card_name, nums in self.deck.items()}

    def shuffle(self):
        self.deck = {x: 4 * self.n_decks for x in self.deck_cards_names if x != '10'}
        self.deck['10'] = 16 * self.n_decks


if __name__ == '__main__':
    bjgame = BJGame(6)
    for x in range(1000):
        print(bjgame.deal())
        print(bjgame.probs())

    ###### Check probabilities ######
    # new_deck = {x: 0 for x in bjgame.deck_cards_names if x != '10'}
    # new_deck['10'] = 0
    # iterations = 500000
    # for x in range(iterations):
    #     new_deck[bjgame.deal()] += 1
    # print(bjgame.probs())
    # print({card_name: nums / iterations for card_name, nums in new_deck.items()})

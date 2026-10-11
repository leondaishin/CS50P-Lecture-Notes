import random
#importing random stuff from defined list that will come now.

cards = ["jack", "queen", "king", "ace"]

def main(): 
    # good for DEBUGGING the program: 
    # random.seed(0)

    # chooses ONE choice 
    # print(random.choice(cards))

    # choose multiple choice
    # but an element can come twice 
    # weights makes the probability to get the elements costum
    print(random.choices(cards, weights=[20, 10, 50, 20], k=2))

    # without replacement so (ziehen ohne zurücklegen)
    # print(random.sample(cards, k=2))

main()
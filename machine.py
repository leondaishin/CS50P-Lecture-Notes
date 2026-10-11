emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":-)"
    say("Oh, hi! How are you?")



def say(phrase):
    print(phrase + " " + emoticon)


main()


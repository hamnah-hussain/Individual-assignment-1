import random

#list of verbs
good_verbs = ["change", "sing", "hug", "play", "work", "run", "dance", "sleep", "eat", "walk", "talk"]
bad_verbs = ["fight", "bicker", "yell", "complain", "scream", "argument", "lie", "cheat", "murder", "leave"]
greeting = ["hello", "hi", "hello there", "well hello there", "well hello", "hi there", "well hi there"]

#randomizes the verbs
random_verb_good = random.choice(good_verbs)
random_verb_bad = random.choice(bad_verbs)

#The sensitive friend
def Al(a, b=None):
    b = random_verb_good
    if a in greeting:
        return "\nAl:" + "Hello my friend :)"

    elif a in good_verbs:
        return "\nAl: " + random.choice(["I would love to {}! Especially with my friends".format(a),
                                           "{} sounds like fun! I love trying new things.".format(a+"ing"),
                                           "Why not!"])

    elif a in bad_verbs:
        return "\nAl: " + random.choice(["That is not somehting I like to do",
                                           "Can you not suggest {} again?".format(a+"ing"),
                                           "I love my friends! I can't do that to them. Let's {} instead".format(b)])

    else:
        return "\nAl: " + "Oh, I don't understand what you are trying to say."


#The mischievous friend
def Carter(a, b=None):
    b = random_verb_bad
    if a in greeting:
        return "\nCarter:" + "Wassup"

    elif a in good_verbs:
        return "\nCarter: " + random.choice(["Doesn't sound like fun.",
                                           "Why can't we {} instead".format(b),
                                           "Your grandma sucks"])

    elif a in bad_verbs:
        return "\nCarter: " + random.choice(["Yeeeeeees",
                                           "I love {}".format(a+"ing"),
                                           "{} would probably make Al cry.".format(a.capitalize()+"ing")])

    else:
        return "\nCarter: " + "At least pick a better word"

#The responsible friend
def Bob(a, b=None):
    b = random_verb_good
    if a in greeting:
        return "\nBob:" + "Hello"

    elif a in good_verbs:
        return "\nBob: " + random.choice(["Sounds good.".format(a),
                                        "{} sounds safe.".format(a+ "ing"),
                                        "Of course"])

    elif a in bad_verbs:
        return "\nBob: " + random.choice(["I don't like doing that.",
                                        "I don' fell like {} is very safe, maybe we should {} instead".format(a+ "ing", b),
                                        "I think I'm going to drop it for this time"])

    else:
        return "\nBob: " + "Maybe you should pick another word."

#The funny friend
def Carlos(a, b=None):
    if a in greeting:
        return "\nCarlos:" + "Yo yo yo"

    elif a in good_verbs:
        return "\nCarlos: " + random.choice(["{} sounds awesome".format(a.capitalize()+"ing"),
                                            "Yo MAMA is {}".format(a+ "ing"),
                                            "Dude {} sounds sick".format(a+ "ing")])

    elif a in bad_verbs:
        return "\nCarlos: " + random.choice(["That is not somehting I like to do",
                                            "You're sick bro {} is not cool".format(a + "ing"),
                                            "Be careful Al is gonna shit his pants."])
    else:
        return "\nCarlos: " + "Bro, your mom doesn't know that word"
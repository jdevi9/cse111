from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest
import random

prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

single_determiners = ["the", "one"]
plural_determiners = ["some", "many"]

single_nouns = ["adult", "bird", "boy", "car", "cat",
                 "child", "dog", "girl", "man", "woman"]
plural_nouns = ["adults", "birds", "boys", "cars", "cats",
                 "children", "dogs", "girls", "men", "women"]

tenses = ["present", "past", "future"]



def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #1. test single nouns.
    single_nouns = ["adult", "bird", "boy", "car", "cat",
                 "child", "dog", "girl", "man", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns
    
    #2. test plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
                 "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    paTense = "past"
    preTense = "present"
    futTense = "future"
    #1. test past verbs
    past_verbs = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(1, paTense)
        assert word in past_verbs

    #2. test present verbs if grammatical number is 1
    present_verbs_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        word = get_verb(1, preTense)
        assert word in present_verbs_1

    #3. test present verbs if grammatical number is 2
    present_verbs_2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        word = get_verb(2, preTense)
        assert word in present_verbs_2
    
    #4 test future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1, futTense)
        assert word in future_verbs

def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    quantity =  random.randint(1, 2)
    phrase = get_prepositional_phrase(quantity)
    phrase_check = phrase.split()
    assert phrase_check[0] in prepositions
    assert phrase_check[1] in single_determiners or plural_determiners
    assert phrase_check[2] in single_nouns or plural_nouns
    
    


pytest.main(["-v", "--tb=line", "-rN", __file__]) 

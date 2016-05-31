# bogglesolver
A solver for various-dimension Boggle™ boards, allowing for an arbitrary dictionary.

The input board consists of a small NxN text file consisting of the
letters.  Using "q" will place the "qu".

Usage:

    $ cat board.txt
    rhre
    ypcs
    wnsn
    tego
    $ ./boggle.py board.txt
    ...
    $ ./boggle.py board.txt upgoer_five_dictionary.txt
    press (length: 5, score: 2) at [(2, 2), (3, 1), (4, 1), (4, 2), (3, 3)]
    wet (length: 3, score: 1) at [(1, 3), (2, 4), (1, 4)]
    went (length: 4, score: 1) at [(1, 3), (2, 4), (2, 3), (1, 4)]
    new (length: 3, score: 1) at [(2, 3), (2, 4), (1, 3)]
    set (length: 3, score: 1) at [(3, 3), (2, 4), (1, 4)]
    sent (length: 4, score: 1) at [(3, 3), (2, 4), (2, 3), (1, 4)]
    son (length: 3, score: 1) at [(3, 3), (4, 4), (4, 3)]
    song (length: 4, score: 1) at [(3, 3), (4, 4), (4, 3), (3, 4)]
    nose (length: 4, score: 1) at [(4, 3), (4, 4), (3, 3), (2, 4)]
    ten (length: 3, score: 1) at [(1, 4), (2, 4), (2, 3)]
    get (length: 3, score: 1) at [(3, 4), (2, 4), (1, 4)]
    once (length: 4, score: 1) at [(4, 4), (4, 3), (3, 2), (4, 1)]

On Windows with Python pre-installed, it would be invoked as

    C:\Temp> python boggle.py board.txt valid_words.txt
    
Output includes the word, the word-length & score (based on the 4x4 rules),
as well as the path to traverse to find the word in question:

Be aware that output is unsorted and multiple paths may produce the same word, so the output can include duplicates.


# bogglesolver
A solver for various-dimension Boggle™ boards, allowing for an arbitrary dictionary

Usage:

    $ cat board.txt
    rhre
    ypcs
    wnsn
    tego
    $ ./boggle.py board.txt
    ...
    $ ./boggle.py board.txt upgoer_five_dictionary.txt
    ...

On Windows with Python pre-installed, it would be invoked as

   C:\Temp> python boggle.py board.txt
    
Output includes the word-length score, the word, as well as the path to traverse to find the word in question:

    5 press at [(2, 2), (3, 1), (4, 1), (4, 2), (3, 3)]
    3 wet at [(1, 3), (2, 4), (1, 4)]
    4 went at [(1, 3), (2, 4), (2, 3), (1, 4)]
    3 new at [(2, 3), (2, 4), (1, 3)]
    ...

Be aware that output is unsorted and multiple paths may produce the same word, so the output can include duplicates.

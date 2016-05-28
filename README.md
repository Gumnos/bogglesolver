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

Note that a word may appear multiple times in the output as produced by different paths.

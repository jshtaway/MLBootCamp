#### Pair Problem #1

Given a string, write a function to reverse it. Do this using a loop, if possible.

    reverseString('abcdef') will return 'fedcba'
    reverseString('moon') will return 'noom'

#### Pair Problem #2

Sal's classroom has a bag of alphabet magnets. She wants to know if she can spell her friend's name using the letters in the bag. Write a function that will take a list of alphabets and a name and print out yes if the name can be spelled and no otherwise.

    CanYouSpell(['y','n','p','g','n','l'],"lynn") would print YES
    CanYouSpell(['y','n','p','g','l'],"lynn") would print NO

When you are done, submit to the Slack channel.

#### Extra Challange

running the following inside a jupyter notebook will download a list of english words:
```
!wget -O enable1.txt https://github.com/dolph/dictionary/blob/master/enable1.txt?raw=true
english_words = set([word.strip() for word in open('enable1.txt').readlines()])
```
Can you write a function that will find **all** english words you can spell from a list of letters

    CheatAtScrabble(['T','C','A']) => ['CAT','ACT']

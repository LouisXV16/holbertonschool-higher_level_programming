The ``text_indentation`` module
===============================

Using ``text_indentation``
--------------------------

Importing function from the module:
    >>> text_indentation = __import__('text_indentation').text_indentation

Text with punctuation
    >>> text_indentation("Hello. How are you? I am fine.")
    Hello.

    How are you?

    I am fine.

Text with spaces after punctuation
    >>> text_indentation("Hello.   How are you?  I am fine.  ")
    Hello.

    How are you?

    I am fine.

Text with multiple sentences
    >>> text_indentation("This is a test: it should work. Indeed, it does?")
    This is a test:

    it should work.

    Indeed, it does?

Empty string
    >>> text_indentation("")
    (prints nothing)

Text without punctuation
    >>> text_indentation("Hello there")
    Hello there

Text is not a string (integer)
    >>> text_indentation(123)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

Text is not a string (list)
    >>> text_indentation(["Hello", "world"])
    Traceback (most recent call last):
        ...
    TypeError: text must be a string


import pytest

from lab2.solver.task1 import amount_of_sentences
from lab2.solver.task1 import amount_of_non_declarative_sentences
from lab2.solver.task1 import average_len_of_sent
from lab2.solver.task1 import average_word_len


def test_am_of_sent1():
    assert amount_of_sentences(
        "Deborah D.K. was angry at her son. Her son didn't listen to her. Her son was 16 yr. old.") == 3


def test_am_of_sent2():
    assert amount_of_sentences("") == 0


def test_am_of_sent3():
    assert amount_of_sentences(
        "The letter, dated 3rd Jan. was written by Crossley A.A. and the landlord of Mr. and Mrs. Smith, on behalf of Crossley's wife.") == 1


def test_am_of_non_dec_sent1():
    assert amount_of_non_declarative_sentences("Do you like water? Yes, sure") == 1


def test_am_of_non_dec_sent2():
    assert amount_of_non_declarative_sentences("") == 0


def test_am_of_non_dec_sent3():
    assert amount_of_non_declarative_sentences("Kendal asked what time it was. "
                                               "Robert De Niro’s character Travis Bickle famously asks, “Are you talkin’ to me?” "
                                               "It’s hard to pick just one, but my favorite Taylor Swift song is “… Ready for It?” "
                                               "Adelina wanted to become a doctor after watching the anime Cells at Work! "
                                               "They spent the day cleaning their living room, kitchen, bedroom, etc.") == 3


def test_av_len_of_sent1():
    assert average_len_of_sent("Kendal asked what time is it? They spent the day cleaning their living room, kitchen, bedroom, etc.") == 39


def test_av_len_of_sent2():
    assert average_len_of_sent("") == 0


def test_av_len_of_sent3():
    assert average_len_of_sent("Apple. Carrot. Cucumber. Tomato. Banana.") == 6.2


def test_av_word_len1():
    assert average_word_len("Apple. Carrot. Cucumber. Tomato. Banana.") == 6.2


def test_av_word_len2():
    assert average_word_len("") == 0


def test_av_word_len3():
    assert average_word_len("Her son A1B2C3 didn't listen to her. Her son was 16 yr. old.") == 37 / 11

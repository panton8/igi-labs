import pytest

from lab2.solver.task1 import amount_of_sentences


def test_am_of_sent1():
    assert amount_of_sentences("Deborah D.K. was angry at her son. Her son didn't listen to her. Her son was 16 yr. old.") == 3


def test_am_of_sent2():
    assert amount_of_sentences("") == 0


def test_am_of_sent3():
    assert amount_of_sentences("The letter, dated 3rd Jan. was written by Crossley A.A. and the landlord of Mr. and Mrs. Smith, on behalf of Crossley's wife.") == 1

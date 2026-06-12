"""
Autograder tests for Problem Set 5 — Recursion & HTTP / APIs

Each test class tests either a custom class or a required function.
Tests run independently so students receive per-component feedback.

To run locally:
    pytest .github/python_tests/test_problem_set_5.py -v
"""

import copy
import os
import pytest
from conftest import load_student_module, assert_has_function
from random import randint
from unittest.mock import Mock

# ---------------------------------------------------------------------------
# Path to the student's submission (relative to the repo root)
# ---------------------------------------------------------------------------
_SOLUTION_MODE = os.environ.get("SOLUTION_MODE", "").lower() == "true"

STUDENT_FILE = (
    "Python/Weekly Problem Sets/Problem Set 5 solution.py"
    if _SOLUTION_MODE
    else "Python/Weekly Problem Sets/Problem Set 5 starter.py"
)


# ---------------------------------------------------------------------------
# Shared fixture — loads the student module once per test session
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def student():
    return load_student_module(STUDENT_FILE, "student_ps5")


class TestRecursiveSquares:
    """Tests for problem 1, recursive squares"""

    def test_recursive_squares_exists(self, student):
        assert_has_function(student, "recursive_squares")

    def test_squares_empty_list(self, student):
        assert (
            student.recursive_squares(0) == []
        ), "When n = 0, the list should be empty"

    def test_squares_single(self, student):
        assert student.recursive_squares(1) == [1], "When n = 1, the list should be [1]"

    def test_squares_example(self, student):
        assert student.recursive_squares(5) == [
            1,
            4,
            9,
            16,
            25,
        ], "Failed the example of n=5"

    def test_squares_random(self, student):
        for i in range(5):
            n = randint(5, 15)
            ans = student.recursive_squares(n)
            assert len(ans) == n, f"Given n={n}, there should be {n} elements"
            assert ans[-1] == n**2, f"The last element for n={n} should be {n ** 2}"

    def test_squares_recursion(self, student):
        """Verify that recursive_squares() is implemented recursively by counting function calls"""
        n = 5
        expected_result = [1, 4, 9, 16, 25]

        # Track the number of times the function is called
        call_count = 0
        original_func = student.recursive_squares

        def wrapper(num):
            nonlocal call_count
            call_count += 1
            return original_func(num)

        # Temporarily replace the function with our wrapper
        student.recursive_squares = wrapper

        try:
            result = student.recursive_squares(n)
            assert (
                result == expected_result
            ), f"recursive_squares({n}) should return {expected_result}"

            # For n=5, recursion should call the function at least n+1 times
            # (for n=5, 4, 3, 2, 1, 0)
            expected_calls = n
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.recursive_squares = original_func


class TestPalindromeChecker:
    """Tests for problem 1, palindrome checker"""

    def test_palindrome_checker_exists(self, student):
        assert_has_function(student, "palindrome_checker")

    def test_palindrome_empty_string(self, student):
        assert student.palindrome_checker("") == True, "An empty string is a palindrome"

    def test_palindrome_examples(self, student):
        assert student.palindrome_checker("bacon") == False, "Bacon is not a palindrome"
        assert student.palindrome_checker("radar") == True, "Radar is a palindrome"

    def test_palindrome_even_length(self, student):
        for test_case, expected_result in {
            "leer": False,
            "noon": True,
            "deed": True,
            "fear": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_odd_length(self, student):
        for test_case, expected_result in {
            "vader": False,
            "radar": True,
            "level": True,
            "paper": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_sentences(self, student):
        cases = {
            "A man, a plan, a canal: Panama": False,
            "Able was I ere I saw Elba": True,
            "Eva, can I see bees in a cave?": False,
        }
        for test_case, expected_result in {
            "leer": False,
            "noon": True,
            "deed": True,
            "fear": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_recursion(self, student):
        """Verify that palindrome_checker() is implemented recursively by counting function calls"""
        test_string = "radar"
        expected_result = True

        # Track the number of times the function is called
        call_count = 0
        original_func = student.palindrome_checker

        def wrapper(s):
            nonlocal call_count
            call_count += 1
            return original_func(s)

        # Temporarily replace the function with our wrapper
        student.palindrome_checker = wrapper

        try:
            result = student.palindrome_checker(test_string)
            assert (
                result == expected_result
            ), f"palindrome_checker('{test_string}') should return {expected_result}"

            # For a string of length n, recursion should call the function at least ceil(n/2) + 1 times
            # (checking pairs until reaching base case)
            expected_calls = len(test_string) // 2
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.palindrome_checker = original_func


class TestListLength:
    """Tests for problem 1, flatten"""

    def test_length_exists(self, student):
        assert_has_function(student, "length")

    def test_length_empty_list(self, student):
        assert student.length([]) == 0, "Empty list length should be 0"

    def test_length_example_list(self, student):
        test_data = [1, 2, 3]
        expected_value = 3
        assert (
            student.length(test_data) == 3
        ), f"{test_data} should have length {expected_value}"

    def test_length_nested_list(self, student):
        test_data = [1, [15, 25], 3]
        expected_value = 3
        assert (
            student.length(test_data) == 3
        ), f"{test_data} should have length {expected_value}"

    def test_length_recursion(self, student):
        """Verify that length() is implemented recursively by counting function calls"""
        test_data = [1, 2, 3]
        expected_value = 3

        # Track the number of times the function is called
        call_count = 0
        original_length = student.length

        def wrapper(lst):
            nonlocal call_count
            call_count += 1
            return original_length(lst)

        # Temporarily replace the function with our wrapper
        student.length = wrapper

        try:
            result = student.length(test_data)
            assert (
                result == expected_value
            ), f"{test_data} should have length {expected_value}"

            # For a list of length n, recursion should call the function n+1 times
            # (once for each element + one final call with empty list)
            expected_calls = len(test_data)
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.length = original_length


@pytest.mark.challenge
class TestFlatten:
    """Tests for problem 1, flatten"""

    def test_flatten_exists(self, student):
        assert_has_function(student, "flatten")

    def test_flatten_empty(self, student):
        assert student.flatten([]) == [], "Empty list should be an empty list"

    def test_flatten_example(self, student):
        test_data = [1, [2, 3], [4], 5]
        expected_value = [1, 2, 3, 4, 5]
        assert (
            student.flatten(test_data) == expected_value
        ), f"{test_data} should return {expected_value}"

    def test_flatten_double(self, student):
        test_data = [1, [2, 3, [35]], [4], 5]
        expected_value = [1, 2, 3, 35, 4, 5]
        assert (
            student.flatten(test_data) == expected_value
        ), f"{test_data} should return {expected_value}"

    def test_flatten_more(self, student):
        test_cases = (
            ([[], [4], 5], [4, 5]),
            ([[1, 2], 3, 4], [1, 2, 3, 4]),
            ([[[1, 2], [3, 4]], 5, [6]], [1, 2, 3, 4, 5, 6]),
        )

        for test, ans in test_cases:
            assert student.flatten(test) == ans, f"{test} should return {ans}"

    def test_flatten_recursino(self, student):
        test_data = [1, [2, 3], [4], 5]
        expected_value = [1, 2, 3, 4, 5]

        # Track the number of times the function is called
        call_count = 0
        original_fn = student.flatten

        def wrapper(lst):
            nonlocal call_count
            call_count += 1
            return original_fn(lst)

        # Temporarily replace the function with our wrapper
        student.flatten = wrapper

        try:
            result = student.flatten(test_data)
            assert (
                result == expected_value
            ), f"{test_data} should return {expected_value}"

            # For a list of length n, recursion should call the function n+1 times
            # (once for each element + one final call with empty list)
            expected_calls = len(test_data)
            assert call_count >= 3, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.flatten = original_fn


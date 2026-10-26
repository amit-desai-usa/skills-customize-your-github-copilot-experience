# 📘 Assignment: Testing Python Applications with pytest

## 🎯 Objective

Practice writing automated tests with pytest to check Python functions, uncover bugs, and improve program reliability. You will test a small gradebook module, then fix defects revealed by your tests.

## 📝 Tasks

### 🛠️ Write Your First Tests

#### Description
Create a file named `test_gradebook.py` and write tests for the functions in `starter-code.py`. Rename the starter file to `gradebook.py` so pytest can import it.

#### Requirements
Completed program should:

- Install pytest if needed with `python -m pip install pytest`
- Test `calculate_average()` with a list of scores and with an empty list
- Use clear test names and assert the expected return values
- Run the tests with `python -m pytest`


### 🛠️ Test Results and Boundary Cases

#### Description
Add tests for finding the highest score and selecting passing scores. Include a score exactly equal to the pass mark to check the boundary behavior.

#### Requirements
Completed program should:

- Test `highest_score()` with scores whose minimum and maximum differ
- Test `passing_scores()` with scores below, at, and above the default pass mark
- Verify the returned values and order, not just that the functions run
- Confirm that at least one test fails against the starter code


### 🛠️ Fix Bugs and Verify the Suite

#### Description
Use the failing tests to find and correct the intentional defects in the starter module. Rerun the complete test suite after making changes.

#### Requirements
Completed program should:

- Correct the behavior of `highest_score()` and `passing_scores()` without weakening the tests
- Pass all tests when run with `python -m pytest`
- Add one additional test case of your choice and confirm it passes
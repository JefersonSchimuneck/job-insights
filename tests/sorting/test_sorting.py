import pytest
from src.sorting import sort_by

mocked_jobs = [
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
    {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
    {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
]


def test_sort_by_criteria():
    sort_by(mocked_jobs, "min_salary")
    assert mocked_jobs == [
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
    ]

    sort_by(mocked_jobs, "max_salary")
    assert mocked_jobs == [
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
    ]

    sort_by(mocked_jobs, "date_posted")
    assert mocked_jobs == [
        {"min_salary": 2, "max_salary": 4, "date_posted": "2020-03-01"},
        {"min_salary": 3, "max_salary": 5, "date_posted": "2020-02-01"},
        {"min_salary": 1, "max_salary": 6, "date_posted": "2020-01-01"},
    ]

    with pytest.raises(ValueError):
        sort_by(mocked_jobs, "invalid_criteria")

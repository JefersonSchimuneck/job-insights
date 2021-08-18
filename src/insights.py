from src.jobs import read
from src.utils import get_unique_key_values


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs_dict = read(path)

    unique_job_types = get_unique_key_values("job_type", jobs_dict)

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    filtered_jobs_by_type = list(
        filter(lambda job: job["job_type"] in job_type, jobs)
    )

    return filtered_jobs_by_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """

    jobs_dict = read(path)

    unique_industries = get_unique_key_values("industry", jobs_dict)

    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_jobs_by_industry = list(
        filter(lambda job: job["industry"] in industry, jobs)
    )

    return filtered_jobs_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs_dict = read(path)

    unique_salaries = get_unique_key_values("max_salary", jobs_dict)

    salaries_to_int = [
        int(salary) for salary in unique_salaries if salary.isdigit()
    ]

    max_salary = max(salaries_to_int)

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_dict = read(path)

    unique_salaries = get_unique_key_values("min_salary", jobs_dict)

    salaries_to_int = [
        int(salary) for salary in unique_salaries if salary.isdigit()
    ]

    min_salary = min(salaries_to_int)

    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("min_salary and max_salary must be provided")

    elif not (
        isinstance(job["min_salary"], int)
        and
        isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be integers")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greater than max_salary")

    elif not isinstance(salary, int):
        raise ValueError("salary must be an integer")

    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs_by_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs_by_salary.append(job)
        except ValueError:
            pass

    return filtered_jobs_by_salary

import pandas as pd
import random
from faker import Faker

fake = Faker()
random.seed(42)

job_titles = ["Data Analyst", "Data Scientist", "ML Engineer", "BI Analyst", "Data Engineer", "Analytics Intern"]
companies = [fake.company() for _ in range(100)]
locations = ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune", "Gurgaon", "Remote"]
skills = ["Python", "SQL", "Excel", "Power BI", "Tableau", "Machine Learning", "Statistics", "Communication"]
experience_levels = ["Internship", "Entry Level", "Mid Level", "Senior Level"]

salary_map = {
    "Internship": (1, 2),
    "Entry Level": (3, 6),
    "Mid Level": (6, 12),
    "Senior Level": (12, 25)
}

def generate_job_entry():
    title = random.choice(job_titles)
    company = random.choice(companies)
    city = random.choice(locations)
    posted_date = fake.date_between(start_date='-30d', end_date='today')
    experience = (
        "Internship" if "Intern" in title else
        random.choices(
            population=["Entry Level", "Mid Level", "Senior Level"],
            weights=[0.5, 0.3, 0.2]
        )[0]
    )
    salary_range = salary_map[experience]
    salary_min = random.randint(salary_range[0], salary_range[1] - 1)
    salary_max = random.randint(salary_min + 1, salary_range[1])

    return {
        "title": title,
        "company": company,
        "location": city,
        "posted_date": posted_date,
        "experience_level": experience,
        "skills": ", ".join(random.sample(skills, k=random.randint(3, 5))),
        "salary_lpa_min": salary_min,
        "salary_lpa_max": salary_max,
        "job_link": fake.url(),
        "scraped_at": fake.date_time_this_month()
    }

job_data = [generate_job_entry() for _ in range(501)]
df = pd.DataFrame(job_data)
df.to_csv("linkedin_data_jobs_with_salary.csv", index=False)
print("✅ Dataset saved to linkedin_data_jobs_with_salary.csv")

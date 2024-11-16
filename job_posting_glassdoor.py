import re


class Job_Posting_Glassdoor:
    def __init__(self, title, location, skills,type, seniority_level, remote, est_salary = '', description =''):
        self.title = title
        self.location = location
        self.skill = skills
        self.type = type
        self.seniority_level = seniority_level
        self.est_salary = est_salary
        self.remote = remote
        self.description = description



def CheckForSkill(descriptions: list):
    skills = []
    searchable_skills = [
        'Python', 'JS', 'Java', 'Javascript', 'C++', 'Azure', 'AWS', 'Rest API', 'React', 'HTML',
        'CSS', 'Golang', 'Go', 'SQL', 'Docker', 'Kubernetes', 'Git', 'Node.js', 'TypeScript',
        'Angular', 'Django', 'Flask', 'Ruby', 'PHP', 'Kotlin', 'Swift', 'GraphQL', 'Firebase',
        'Terraform', 'Machine Learning', 'Data Science', 'NoSQL', 'JavaScript Frameworks',
        'Vue', 'Svelte', 'Android Development', 'iOS Development', 'DevOps', 'CI/CD'
    ]

    # Iterate over each description in the list
    for desc in descriptions:
        # Loop through each skill in searchable_skills
        for skill in searchable_skills:
            # Use regex to search for the skill as a whole word, case-insensitive
            if re.search(rf'\b{skill}\b', desc, re.IGNORECASE):
                if skill not in skills:  # Optional: avoid duplicates
                    skills.append(skill)

    return skills



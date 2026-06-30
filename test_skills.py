# test_skills.py

from app.services.skill_service import SkillService

text = """
Python
Java
Machine Learning
AWS
Git
FastAPI
React
MySQL
"""

skills = SkillService.extract_skills(text)

print(skills)
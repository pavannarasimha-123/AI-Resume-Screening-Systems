import re

from app.utils.skills import SKILLS


class SkillService:

    @staticmethod
    def extract_skills(text: str):

        if not text:
            return []

        text = text.lower()

        found_skills = []

        for skill in SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):

                found_skills.append(skill)

        return sorted(set(found_skills))
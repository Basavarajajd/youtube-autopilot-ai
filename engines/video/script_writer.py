"""
Script Writer AI
Turns topics into YouTube scripts
"""

from core.logger import logger
from datetime import datetime


class ScriptWriterAI:
    def __init__(self):
        logger.info("✍️ ScriptWriter AI ready")

    # --------------------------------------------------

    def generate_script(self, topic: str) -> dict:
        logger.info(f"📝 Writing script for: {topic}")

        script = {
            "title": self.generate_title(topic),
            "hook": self.generate_hook(topic),
            "intro": self.generate_intro(topic),
            "main": self.generate_main(topic),
            "outro": self.generate_outro(topic),
            "created_at": str(datetime.now())
        }

        logger.info("✅ Script generated")
        return script

    # --------------------------------------------------

    def generate_title(self, topic):
        return f"{topic} (Full Guide)"

    def generate_hook(self, topic):
        return f"What if I told you {topic.lower()} could change your future?"

    def generate_intro(self, topic):
        return (
            f"In this video, we dive deep into {topic.lower()} "
            "and show real strategies that beginners can follow."
        )

    def generate_main(self, topic):
        points = [
            f"Step 1 — Understanding {topic}",
            f"Step 2 — Tools you need",
            f"Step 3 — Real examples",
            f"Step 4 — Mistakes to avoid",
            f"Step 5 — Action plan"
        ]
        return "\n".join(points)

    def generate_outro(self, topic):
        return (
            "If this video helped you, subscribe for more AI-generated content. "
            "See you in the next video!"
        )

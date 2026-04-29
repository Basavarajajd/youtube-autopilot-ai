"""
Trend Fusion AI
Generates viral video topics from niche
"""

import random
from core.logger import logger


class TrendFusionAI:
    def __init__(self):
        logger.info("🔥 TrendFusion AI ready")

        # seed patterns (later from APIs + scraping)
        self.patterns = [
            "Nobody is talking about {}",
            "Top 5 {} in 2026",
            "I tried {} for 30 days",
            "The dark side of {}",
            "{} that actually works",
            "Beginner guide to {}",
            "Avoid these {} mistakes",
            "How I made money using {}",
        ]

    def generate_topics(self, niche: str, count: int = 5):
        logger.info(f"🔎 Generating topics for niche: {niche}")
        topics = []

        for _ in range(count):
            pattern = random.choice(self.patterns)
            topic = pattern.format(niche)
            topics.append(topic)

        logger.info(f"✅ Generated {len(topics)} topics")
        return topics

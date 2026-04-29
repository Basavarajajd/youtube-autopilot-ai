"""
Decision Engine
Chooses what the AI should do based on data & rules
"""

import random
from core.logger import logger


class DecisionEngine:
    """
    Makes strategic decisions for the autopilot
    """

    def __init__(self):
        logger.info("🧠 Decision Engine ready")

        # Initial niche pool (later comes from DB + analytics)
        self.niches = [
            "AI tools",
            "Make money online",
            "Tech news",
            "YouTube growth",
            "Passive income",
            "Crypto education",
            "Motivation",
        ]

    # --------------------------------------------------
    # PICK NICHE
    # --------------------------------------------------
    def choose_niche(self):
        niche = random.choice(self.niches)
        logger.info(f"🎯 Selected niche: {niche}")
        return niche

    # --------------------------------------------------
    # VIDEO COUNT PER DAY
    # --------------------------------------------------
    def videos_to_create(self):
        count = random.randint(1, 3)
        logger.info(f"🎬 Videos to create today: {count}")
        return count

    # --------------------------------------------------
    # SHORTS COUNT
    # --------------------------------------------------
    def shorts_to_create(self):
        count = random.randint(2, 5)
        logger.info(f"⚡ Shorts to create today: {count}")
        return count

from core.logger import logger
from ai_brain.memory import BrainMemory

# Engines
from engines.trends.trend_fusion_ai import TrendFusionAI
from engines.video.script_writer import ScriptWriterAI


def run_autopilot():
    logger.info("🤖 YOUTUBE AUTOPILOT STARTED")

    # Initialize brain
    brain = BrainMemory()

    # Initialize engines
    trend_ai = TrendFusionAI()
    script_ai = ScriptWriterAI()

    # ---------------------------------------------------
    # STEP 1 — Get Trends
    # ---------------------------------------------------
    topics = trend_ai.generate_topics("AI tools")
    selected_topic = topics[0]

    logger.info(f"🔥 Selected topic: {selected_topic}")

    brain.save("last_topic", selected_topic)

    # ---------------------------------------------------
    # STEP 2 — Generate Script
    # ---------------------------------------------------
    script = script_ai.generate_script(selected_topic)

    brain.save("last_script", script)

    logger.info("🎬 Video script ready!")

    print("\n============================")
    print("TITLE:", script["title"])
    print("HOOK:", script["hook"])
    print("============================")


if __name__ == "__main__":
    run_autopilot()

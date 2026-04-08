from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "AI-music-recommender-main"))

from env import MusicEnv
from agent import QLearningAgent

# Disable automatic redirect on trailing slash to avoid GET redirect causing 405
app = FastAPI(title="AI Music Recommender Inference API", redirect_slashes=False)

# Global env/agent state
_env = MusicEnv()
_agent = QLearningAgent(actions=_env.get_actions(), username="inference_user")


@app.post("/openenv/reset")
@app.post("/openenv/reset/")
async def reset_env():
    """Reset the environment and agent state."""
    global _env, _agent
    _env = MusicEnv()
    _agent = QLearningAgent(actions=_env.get_actions(), username="inference_user")
    return JSONResponse(
        status_code=200,
        content={"status": "ok", "message": "Environment reset successfully."}
    )


@app.get("/openenv/state")
async def get_state(mood: str = "Happy", time_of_day: str = "Morning", last_genre: str = "None"):
    """Get the current environment state."""
    state = _env.get_state(mood, time_of_day, last_genre)
    return {"state": state}


@app.post("/openenv/recommend")
async def recommend(mood: str = "Happy", time_of_day: str = "Morning",
                    last_genre: str = "None", language: str = "Hindi"):
    """Get song recommendations for a given mood/time/language."""
    from recommend import Recommender
    recommender = Recommender(
        data_path=os.path.join(
            os.path.dirname(__file__), "AI-music-recommender-main", "data", "songs.csv"
        )
    )
    state = _env.get_state(mood, time_of_day, last_genre)
    action = _agent.choose_action(state)
    songs = recommender.recommend_songs(mood, action, language, n=3)
    return {"state": state, "genre": action, "songs": songs}


@app.get("/health")
async def health():
    return {"status": "healthy"}

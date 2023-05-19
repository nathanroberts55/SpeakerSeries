import pynecone as pc

class SpeakerseriesConfig(pc.Config):
    pass

config = SpeakerseriesConfig(
    app_name="Nate Roberts | Speaker Series",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3001
)
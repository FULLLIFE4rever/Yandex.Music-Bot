from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):

    TG_TOKEN: SecretStr = None
    BOT_NAME: str = None
    BOT_FIRST_NAME: str = None

    @property
    def tg_token(self):
        return self.TG_TOKEN

    @property
    def bot_info(self):
        return self.BOT_FIRST_NAME, self.BOT_NAME

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

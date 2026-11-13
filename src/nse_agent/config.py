"""Application configuration and safety validation."""

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        extra="ignore",
        case_sensitive=False,
    )

    # NSE MCP
    nse_mcp_url: str | None = None
    nse_mcp_transport: str | None = None

    # Telegram
    telegram_bot_token: str | None = None
    telegram_chat_id: str | None = None

    # Scanner controls
    scanner_enabled: bool = False
    telegram_alerts_enabled: bool = False

    # Swing trading
    min_holding_sessions: int = Field(default=3, ge=1, le=30)
    max_holding_sessions: int = Field(default=15, ge=1, le=60)

    # Risk controls
    risk_per_trade_pct: float = Field(default=1.0, gt=0, le=5)
    daily_loss_limit_pct: float = Field(default=2.0, gt=0, le=10)
    max_open_positions: int = Field(default=5, ge=1, le=20)

    # Mandatory safety restrictions
    paper_trading_only: bool = True
    live_order_execution: bool = False

    @model_validator(mode="after")
    def validate_safety_rules(self):
        if self.min_holding_sessions > self.max_holding_sessions:
            raise ValueError(
                "Minimum holding sessions cannot exceed maximum."
            )

        if self.paper_trading_only is not True:
            raise ValueError(
                "This application must remain paper-trading only."
            )

        if self.live_order_execution is not False:
            raise ValueError(
                "Live order execution is permanently disabled."
            )

        if self.telegram_alerts_enabled and not (
            self.telegram_bot_token and self.telegram_chat_id
        ):
            raise ValueError(
                "Telegram alerts require a bot token and chat ID."
            )

        return self


def get_settings() -> Settings:
    """Return validated application settings."""
    return Settings()
  

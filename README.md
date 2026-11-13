# NSE MCP Trading Research Agent

An Indian equity swing-trading research and paper-trading system using NSE MCP as its market-data integration.

## Project Objectives

- Scan eligible NSE cash-equity stocks.
- Identify swing-trading opportunities over 3–15 trading sessions.
- Evaluate breakout and retest setups.
- Identify trend-continuation opportunities.
- Detect volatility contraction patterns (VCP).
- Rank relative-strength leaders.
- Evaluate support pullbacks and reversals.
- Generate research alerts through Telegram.
- Maintain a paper-trading journal.
- Backtest and validate strategies.

## Architecture

- Market data: NSE MCP only.
- Analysis: Python, Pandas and NumPy.
- Configuration: Environment variables.
- Notifications: Telegram Bot API.
- Storage: SQLite.
- Automation: GitHub Actions.
- Testing: Pytest.

## Research-Only Restrictions

This project is strictly for research and paper trading.

- No broker API integration.
- No live order placement.
- No automated execution.
- No claims of guaranteed returns.
- No fabricated or assumed market prices.
- Stale or incomplete market data must stop the scan.

## Risk Management Defaults

| Setting | Default |
|---|---:|
| Risk per trade | 1% |
| Daily loss limit | 2% |
| Maximum open positions | 5 |
| Holding period | 3–15 sessions |

These are configurable research defaults, not recommendations.

## Data Validation

Before generating any candidate, the system must validate:

- Data source and retrieval timestamp.
- Symbol and exchange.
- Trading session/date.
- Missing and duplicate records.
- OHLCV consistency.
- Data freshness.

## Development Status

Initial repository setup.

NSE MCP tool discovery and schema validation must be completed before implementing market-data calls.

## Safety

Scanner and Telegram notifications remain disabled by default until configuration and validation are complete.

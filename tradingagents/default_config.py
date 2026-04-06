import os


def _env(*names: str, default: str | None = None) -> str | None:
    """Return the first non-empty environment variable from names."""
    for name in names:
        value = os.getenv(name)
        if value:
            return value
    return default


DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": _env("TRADINGAGENTS_LLM_PROVIDER", "LLM_PROVIDER", default="ollama"),
    "deep_think_llm": _env(
        "TRADINGAGENTS_DEEP_THINK_LLM",
        "OLLAMA_DEEP_MODEL",
        default="qwen3:latest",
    ),
    "quick_think_llm": _env(
        "TRADINGAGENTS_QUICK_THINK_LLM",
        "OLLAMA_QUICK_MODEL",
        default="qwen3:latest",
    ),
    "backend_url": _env(
        "TRADINGAGENTS_BACKEND_URL",
        "OLLAMA_BASE_URL",
        default="http://localhost:11434/v1",
    ),
    # Provider-specific thinking configuration
    "google_thinking_level": None,      # "high", "minimal", etc.
    "openai_reasoning_effort": None,    # "medium", "high", "low"
    "anthropic_effort": None,           # "high", "medium", "low"
    # Output language for analyst reports and final decision
    # Internal agent debate stays in English for reasoning quality
    "output_language": "English",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Data vendor configuration
    # Category-level configuration (default for all tools in category)
    "data_vendors": {
        "core_stock_apis": "yfinance",       # Options: alpha_vantage, yfinance
        "technical_indicators": "yfinance",  # Options: alpha_vantage, yfinance
        "fundamental_data": "yfinance",      # Options: alpha_vantage, yfinance
        "news_data": "yfinance",             # Options: alpha_vantage, yfinance
    },
    # Tool-level configuration (takes precedence over category-level)
    "tool_vendors": {
        # Example: "get_stock_data": "alpha_vantage",  # Override category default
    },
}

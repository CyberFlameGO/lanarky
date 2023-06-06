from enum import Enum


class StreamingMode(str, Enum):
    """Streaming modes for LangchainRouter."""

    OFF = "off"
    TEXT = "text"
    JSON = "json"


class LLMCacheMode(str, Enum):
    """LLM cache modes for LangchainRouter."""

    OFF = "off"
    IN_MEMORY = "in_memory"
    REDIS = "redis"
    GPTCACHE = "gptcache"

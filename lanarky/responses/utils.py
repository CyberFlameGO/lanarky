import logging
from functools import wraps

import aiohttp

logger = logging.getLogger(__name__)


def openai_aiosession(func):
    """Decorator to set openai.aiosession for StreamingResponse."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            import openai  # type: ignore
        except ImportError:
            raise ImportError(
                "openai is not installed. Install it with `pip install 'lanarky[openai]'`."
            )

        openai.aiosession.set(aiohttp.ClientSession())
        logger.debug(f"opeanai.aiosession set: {openai.aiosession.get()}")

        try:
            await func(*args, **kwargs)
        finally:
            await openai.aiosession.get().close()
            logger.debug(f"opeanai.aiosession closed: {openai.aiosession.get()}")

    return wrapper

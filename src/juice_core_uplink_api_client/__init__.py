"""A client library for accessing Juice Core Uplink API"""

import importlib

__version__ = importlib.metadata.version("juice_core_uplink_api_client")

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)

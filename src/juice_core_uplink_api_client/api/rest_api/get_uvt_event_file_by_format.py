from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.uvt_event_file import UvtEventFile
from ...types import Response


def _get_kwargs(
    format_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/rest_api/uvt_event_file{format_}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list["UvtEventFile"] | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UvtEventFile.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list["UvtEventFile"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list["UvtEventFile"]]:
    """Retrieve the uvt file sources

     List all the uvt file sources

    Args:
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UvtEventFile']]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> list["UvtEventFile"] | None:
    """Retrieve the uvt file sources

     List all the uvt file sources

    Args:
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UvtEventFile']
    """

    return sync_detailed(
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list["UvtEventFile"]]:
    """Retrieve the uvt file sources

     List all the uvt file sources

    Args:
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UvtEventFile']]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> list["UvtEventFile"] | None:
    """Retrieve the uvt file sources

     List all the uvt file sources

    Args:
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UvtEventFile']
    """

    return (
        await asyncio_detailed(
            format_=format_,
            client=client,
        )
    ).parsed

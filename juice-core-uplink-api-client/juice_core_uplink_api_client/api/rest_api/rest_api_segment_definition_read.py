from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.segment_definition import SegmentDefinition
from ...types import Response


def _get_kwargs(
    mnemonic: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/rest_api/segment_definition/{mnemonic}/".format(client.base_url, mnemonic=mnemonic)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, SegmentDefinition]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SegmentDefinition.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, SegmentDefinition]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mnemonic: str,
    *,
    client: Client,
) -> Response[Union[Any, SegmentDefinition]]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SegmentDefinition]]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mnemonic: str,
    *,
    client: Client,
) -> Optional[Union[Any, SegmentDefinition]]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SegmentDefinition]
    """

    return sync_detailed(
        mnemonic=mnemonic,
        client=client,
    ).parsed


async def asyncio_detailed(
    mnemonic: str,
    *,
    client: Client,
) -> Response[Union[Any, SegmentDefinition]]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SegmentDefinition]]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mnemonic: str,
    *,
    client: Client,
) -> Optional[Union[Any, SegmentDefinition]]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SegmentDefinition]
    """

    return (
        await asyncio_detailed(
            mnemonic=mnemonic,
            client=client,
        )
    ).parsed

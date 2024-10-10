from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.segment_definition import SegmentDefinition
from ...types import Response


def _get_kwargs(
    mnemonic: str,
    format_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/rest_api/segment_definition/{mnemonic}{format_}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SegmentDefinition | None:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.OK:
        response_200 = SegmentDefinition.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SegmentDefinition]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mnemonic: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SegmentDefinition]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SegmentDefinition]]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mnemonic: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SegmentDefinition | None:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SegmentDefinition]
    """

    return sync_detailed(
        mnemonic=mnemonic,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    mnemonic: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SegmentDefinition]:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SegmentDefinition]]
    """

    kwargs = _get_kwargs(
        mnemonic=mnemonic,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    mnemonic: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SegmentDefinition | None:
    """Retrieve the segment definition identified by the mnemonic

     List all segment definition

    Args:
        mnemonic (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SegmentDefinition]
    """

    return (
        await asyncio_detailed(
            mnemonic=mnemonic,
            format_=format_,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.plan import Plan
from ...types import Response


def _get_kwargs(
    id: str,
    format_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/rest_api/plan/{id}{format_}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Plan | None:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = Plan.from_dict(response.json())

        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Plan]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Plan]:
    """Delete a plan

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Plan | None:
    """Delete a plan

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Plan]
    """

    return sync_detailed(
        id=id,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Plan]:
    """Delete a plan

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    format_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Plan | None:
    """Delete a plan

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Plan]
    """

    return (
        await asyncio_detailed(
            id=id,
            format_=format_,
            client=client,
        )
    ).parsed

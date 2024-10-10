from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_scenario import DetailedScenario
from ...types import Response


def _get_kwargs(
    id: str,
    format_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/rest_api/detailed_scenario/{id}{format_}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DetailedScenario | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = DetailedScenario.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DetailedScenario]:
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
) -> Response[Any | DetailedScenario]:
    """Retrieve a detailed scenario

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DetailedScenario]]
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
) -> Any | DetailedScenario | None:
    """Retrieve a detailed scenario

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DetailedScenario]
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
) -> Response[Any | DetailedScenario]:
    """Retrieve a detailed scenario

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DetailedScenario]]
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
) -> Any | DetailedScenario | None:
    """Retrieve a detailed scenario

     Retrieve, update or delete a segmentation instance.

    Args:
        id (str):
        format_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DetailedScenario]
    """

    return (
        await asyncio_detailed(
            id=id,
            format_=format_,
            client=client,
        )
    ).parsed

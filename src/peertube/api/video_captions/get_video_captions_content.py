"""Get video captions content as text."""

from uuid import UUID

import httpx

from peertube.api.video_captions.get_video_captions import (
    sync as get_video_captions_sync,
)
from peertube.client import AuthenticatedClient, Client
from peertube.types import UNSET, Unset


def get_video_captions_content(
    client: AuthenticatedClient | Client,
    id: UUID | int | str,
    language_filter: str | None = "en",
    *,
    x_peertube_video_password: Unset | str = UNSET,
) -> str:
    """Get the content of video captions as a string.

    This function wraps get_video_captions to retrieve caption metadata,
    then downloads the VTT file content for the specified language.

    Args:
        client: PeerTube client instance
        id: Video identifier
        language_filter: Language code to filter captions (default: "en")
        x_peertube_video_password: Video-related parameter

    Returns:
        The VTT file content as a string

    Raises:
        ValueError: If no captions are available or specified language not found
        httpx.HTTPError: For network-related issues when downloading captions
        UnicodeDecodeError: If VTT content cannot be decoded as UTF-8
    """
    # Get caption metadata
    captions_response = get_video_captions_sync(
        client=client, id=id, x_peertube_video_password=x_peertube_video_password
    )

    if captions_response is None or not captions_response.data:
        msg = "No captions available for this video"
        raise ValueError(msg)

    # Find caption matching the language filter
    selected_caption = None

    if language_filter is not None:
        # Filter by specific language
        for caption in captions_response.data:
            if (
                caption.language is not UNSET
                and caption.language.id is not UNSET
                and caption.language.id == language_filter
            ):
                selected_caption = caption
                break

    # Fallback to first available caption if no language match or no filter
    if selected_caption is None:
        if language_filter is not None:
            # Specific language requested but not found
            available_langs = []
            for caption in captions_response.data:
                if caption.language is not UNSET and caption.language.id is not UNSET:
                    available_langs.append(caption.language.id)

            msg = f"Caption language '{language_filter}' not found. Available languages: {available_langs}"
            raise ValueError(msg)
        else:
            # No language filter, use first available
            selected_caption = captions_response.data[0]

    # Extract URL - try additional_properties first, then caption_path
    caption_url = None

    if "fileUrl" in selected_caption.additional_properties:
        caption_url = selected_caption.additional_properties["fileUrl"]
    elif selected_caption.caption_path is not UNSET:
        # If caption_path is relative, construct full URL
        if selected_caption.caption_path.startswith("/"):
            caption_url = str(client.base_url).rstrip("/") + selected_caption.caption_path
        else:
            caption_url = selected_caption.caption_path

    if caption_url is None:
        msg = "Caption URL not found in response"
        raise ValueError(msg)

    # Download the VTT content
    httpx_client = client.get_httpx_client()

    try:
        response = httpx_client.get(caption_url)
        response.raise_for_status()

        # Decode as UTF-8 text
        return response.content.decode("utf-8")

    except httpx.HTTPError as exc:
        msg = f"Failed to download caption content from {caption_url}"
        raise httpx.HTTPError(msg) from exc
    except UnicodeDecodeError as exc:
        msg = "Failed to decode caption content as UTF-8"
        raise UnicodeDecodeError(exc.encoding, exc.object, exc.start, exc.end, msg) from exc

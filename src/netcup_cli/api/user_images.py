"""User images (S3) API - list, delete, get download URL."""

from .base import get_client


def user_images_list(user_id: int) -> list[dict]:
    """GET /api/v1/users/{userId}/images."""
    client = get_client()
    resp = client.get(f"/users/{user_id}/images")
    return resp.json()


def user_image_delete(user_id: int, key: str) -> None:
    """DELETE /api/v1/users/{userId}/images/{key}."""
    client = get_client()
    client.delete(f"/users/{user_id}/images/{key}")


def user_image_download_url(user_id: int, key: str) -> str | dict:
    """GET /api/v1/users/{userId}/images/{key} - Get presigned download URL. Returns URL string or full response."""
    client = get_client()
    resp = client.get(f"/users/{user_id}/images/{key}")
    data = resp.json()
    if isinstance(data, str):
        return data
    return data.get("presignedUrl", data) if isinstance(data, dict) else data

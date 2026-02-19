"""User ISOs (S3) API - list, delete, get download URL."""

from .base import get_client


def user_isos_list(user_id: int) -> list[dict]:
    """GET /api/v1/users/{userId}/isos."""
    client = get_client()
    resp = client.get(f"/users/{user_id}/isos")
    return resp.json()


def user_iso_delete(user_id: int, key: str) -> None:
    """DELETE /api/v1/users/{userId}/isos/{key}."""
    client = get_client()
    client.delete(f"/users/{user_id}/isos/{key}")


def user_iso_download_url(user_id: int, key: str) -> str | dict:
    """GET /api/v1/users/{userId}/isos/{key} - Get presigned download URL."""
    client = get_client()
    resp = client.get(f"/users/{user_id}/isos/{key}")
    data = resp.json()
    if isinstance(data, str):
        return data
    return data.get("presignedUrl", data) if isinstance(data, dict) else data

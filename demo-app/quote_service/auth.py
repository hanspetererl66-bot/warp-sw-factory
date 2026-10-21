"""Roles come from the X-Role request header (demo only, not real auth)."""

ROLES = {"sales", "manager"}


def role_from_headers(headers) -> str:
    role = (headers.get("X-Role") or "").lower()
    if role not in ROLES:
        raise PermissionError("unknown role")
    return role

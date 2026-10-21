#!/usr/bin/env bash
# Deploy hook. Replace the body with your target (Fly.io, Render, Vercel, ...).
# Usage: scripts/deploy.sh <environment> <sha>
set -euo pipefail
env_name="${1:?environment required}"
sha="${2:?sha required}"
: "${DEPLOY_TOKEN:?DEPLOY_TOKEN is not set}"
echo "TODO: deploy ${sha} to ${env_name} (wire to the real hosting target)"
exit 1

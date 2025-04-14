ARG TARGETPLATFORM
ARG BUILDPLATFORM

FROM --platform=$TARGETPLATFORM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  UV_SYSTEM_PYTHON=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY uv.lock pyproject.toml /app/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project && \
  rm -rf /root/.cache/uv

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen && \
  rm -rf /root/.cache/uv

CMD ["uv", "run", "main.py"]

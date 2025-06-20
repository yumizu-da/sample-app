FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

WORKDIR /workspace
ENV PATH="/root/.local/bin/:${PATH}"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --no-dev

FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

WORKDIR /workspace
ENV PATH="/root/.local/bin/:$PATH"

COPY --from=builder /root/.local/bin/uv /root/.local/bin/uv
COPY --from=builder /workspace/.venv /workspace/.venv

COPY ./ ./
EXPOSE 8080

CMD ["uv", "run", "--no-sync", "streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

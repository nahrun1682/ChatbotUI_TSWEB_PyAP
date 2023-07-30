# ---- Base Node ----
FROM python:3.10 AS base
WORKDIR /app
COPY pyproject.toml poetry.lock* ./

# ---- Dependencies ----
FROM base AS dependencies
RUN pip install poetry && poetry install --no-root

# ---- Copy Files/Build ----
FROM dependencies AS build
COPY ./ /app/
RUN poetry config virtualenvs.create false
RUN poetry install

# ---- Production ----
FROM python:3.10 as production
WORKDIR /app
RUN pip install poetry
COPY --from=dependencies /root/.cache /root/.cache
COPY --from=build /app/ ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

# Expose the port the app will run on
EXPOSE 8000

# Start the application
CMD ["poetry", "run", "python","app/main.py"]

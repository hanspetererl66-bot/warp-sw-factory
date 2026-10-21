FROM python:3.12-slim
WORKDIR /app
COPY quote_service ./quote_service
ENV PORT=8080
CMD ["python", "-m", "quote_service.server"]

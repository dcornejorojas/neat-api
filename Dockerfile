# pull official base image
FROM python:3.9 AS base

RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install -y --no-install-recommends make gcc

ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

WORKDIR /app
COPY . /app
RUN ls -la


# install system dependencies
RUN pip install --upgrade pip
RUN pip install Flask==2.0.3 \
  && pip install Flask-Cors==3.0.10 \
  && pip install Flask-SQLAlchemy==2.4.4 \
  && pip install Flask-APScheduler==1.12.1 \
  && pip install Jinja2==3.0.0 \
  && pip install opentelemetry-api==1.11.1 \
  && pip install opentelemetry-sdk==1.11.1 \
  && pip install opentelemetry-instrumentation-flask==0.30b1 \
  && pip install opentelemetry-instrumentation-requests==0.30b1 \
  && pip install python-memcached==1.59 \
  && pip install redis==3.5.3 \
  && pip install responses==0.22.* \
  && pip install requests==2.25.1 \
  && pip install pydantic \
  && pip install pylint \
  && pip install validators \
  && pip install waitress \
  && pip install Werkzeug \
  && pip install pytest \
  && pip install pytest-asyncio \
  && pip install pytest-cov

FROM base as release
WORKDIR /app
EXPOSE 5000

# RUN addgroup --system --gid 10001 appgroup \
#   && adduser --system --disabled-password --uid 10000 --shell /sbin/nologin --home /app --ingroup appgroup appuser \
#   && chown -R appuser:appgroup /app

USER 10000

CMD ["python", "-u", "./app.py"]

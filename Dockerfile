FROM python:3.11

WORKDIR /app

RUN useradd -m app
RUN chown -R app /app

USER app 
ENV PATH=/home/app/.local/bin:$PATH
COPY requirements.txt /app
RUN pip install --user -r requirements.txt
COPY --chown=app . /app

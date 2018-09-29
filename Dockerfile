FROM python:3

WORKDIR /srv/http/app
VOLUME /srv/http/app/inventory

CMD ["gunicorn", \
  "--bind=0.0.0.0:8000", \
  "--workers=4", \
  "--capture-output", \
  "--log-file=-" ,\
  "--access-logfile=-", \
  "app:app"]
EXPOSE 8000

RUN pip install --no-cache-dir gunicorn

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY library/ ./
COPY ansible.cfg ./library/
COPY templates/ ./templates/
COPY app.py ./

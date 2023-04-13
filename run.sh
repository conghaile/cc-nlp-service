source .env;
source /home/quandale/cc-nlp-service/venv/bin/activate;
flask --app server run -h localhost -p ${PORT};
docker build -t mimic container/.
docker run -it --name mimic_db -p 8000:8000 -v `pwd`/shared:/analysis/shared mimic

docker build -t mimicry_db container/.
docker run -it --name mimicry_db -p 8000:8000 -v `pwd`/shared:/analysis/shared mimic

docker build -t mimicry_db container/.
docker run -it --name mimicry_db -p 8282:8282 -v `pwd`/shared:/analysis/shared mimic

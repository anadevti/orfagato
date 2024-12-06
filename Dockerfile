FROM ubuntu:latest
LABEL authors="aninha"

ENTRYPOINT ["top", "-b"]
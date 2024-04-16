
docker build . --file Dockerfile --runtime nvidia -e DISPLAY=$DISPLAY --tag bloodtroller/sistemska-administracija:latest
docker push bloodtroller/sistemska-administracija:latest
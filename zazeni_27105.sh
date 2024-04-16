docker rm docker_image > /dev/null 2>&1
docker run --privileged --name "docker_image" -ti bloodtroller/sistemska-administracija
docker rm docker_image
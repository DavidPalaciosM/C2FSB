# Docker Desktop

# usage
```
# remove
docker rm -f <container_id>
docker rmi <image_id>
# autoprune
docker system prune

# To trigger a space reclamation at any point, run the command:
docker run --privileged --pid=host docker/desktop-reclaim-space

# query the actual size of the file on the host from a terminal, run:
 cd ~/.docker/desktop/vms/0/data
 ls -klsh Docker.raw

# detailed space usage information by running:
docker system df -v
docker image ls
docker container ls -a

# storage
/var/lib/docker
```

## Recommended approach to install Docker Desktop on Debian:
	
```
# system has kvm?
lsmod | grep kvm
# user belongs kvm
sudo usermod -aG kvm $USER
# subgid subuid
grep "$USER" /etc/subuid >> /dev/null 2&>1 || (echo "$USER:100000:65536" | sudo tee -a /etc/subuid)
grep "$USER" /etc/subgid >> /dev/null 2&>1 || (echo "$USER:100000:65536" | sudo tee -a /etc/subgid)
```


### add gnome extension (tray notification)
https://extensions.gnome.org/extension/615/appindicator-support/

## Set up Docker’s package repository.
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

##  Download latest DEB package.
[used](https://desktop.docker.com/linux/main/amd64/docker-desktop-4.15.0-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64s://desktop.docker.com/linux/main/amd64/docker-desktop-4.15.0-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64)
##  Install the package with apt as follows:
```
sudo apt install docker-ce-cli docker-desktop docker-scan-plugin pass qrencode tree uidmap 
sudo apt-get update

# sudo apt-get install ./docker-desktop-<version>-<arch>.deb
sudo apt-get install ~/Downloads/docker-desktop-4.15.0-amd64.deb
# sudo dpkg -i <package.deb>
# sudo dpkg -i ./docker-desktop-4.15.0-amd64.deb

Related packages
  docker-ce-cli
  docker-desktop
  docker-scan-plugin
  pass
  qrencode
  tree
  uidmap
```

## manage your [credentials](https://docs.docker.com/desktop/get-started/#credentials-management-for-linux-users)
```
# generate or import gpg
gpg --generate-key
gpg --allow-secret-key-import --import private.key

# initialize pass
pass init public.key
```

# UNINSTALL all
```
sudo apt remove docker-desktop
rm -r $HOME/.docker/desktop
sudo rm /usr/local/bin/com.docker.cli
sudo apt purge docker-desktop
## preview or beta
~/.config/systemd/user/docker-desktop.service
~/.local/share/systemd/user/docker-desktop.service
```

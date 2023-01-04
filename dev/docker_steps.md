# Docker Desktop

## Recommended approach to install Docker Desktop on Debian:
	
```
# system has kvm?
lsmod | grep kvm
# user belongs kvm
sudo usermod -aG kvm $USER
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
 # sudo dpkg -i <package.deb>
 sudo dpkg -i ./docker-desktop-4.15.0-amd64.deb

docker-ce-cli
docker-desktop
docker-scan-plugin
pass
qrencode
tree
uidmap
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

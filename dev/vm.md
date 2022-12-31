# hyper-v
## requirements
- Windows 10 Pro, Enterprise, Education or Server edition. NOT Home edition!!!!
- A 64-bit processor with Second Level Address Translation (SLAT)
- CPU support for virtualization extensions and virtualization enabled in the system BIOS/EFI
- Minimum of 4 GB of memory, recommended 8 GB
- Minimum of 5 GB of disk space, recommended 15 GB 

## Installation
### Hyper-V Graphical Install
- Right click on the Windows Start button and select 'Apps and Features'
- Select 'Programs and Features' on the right under Related Settings
- Select 'Turn Windows Features on or off'
- Select 'Hyper-V' and click OK
- Restart when prompted

### Hyper-V PowerShell Install
- Open a PowerShell console as Administrator
- Run the following command: Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
- Restart when prompted 

# vm creation
## Ubuntu vm creation
0. create vm
- open "start menu" (press super or windows key)
- type "Hyper-V"
- click "Quick Create"
- click "Ubuntu 22.04 LTS"

1. configure
- on hyperv vm settings: select 1024 ram, 4 processors, no vm checkpoints, an accesible folder like ~/Documents/vm
- start the machine: selected resolution 1920x1080
- follow the on-screen startup config
- Name: fire, machineName: fireVM, user: fire, password: f
NOTE: Enabling auto-login for your Ubuntu user causes an issue that will block enhanced mode from successfully connecting. Please ensure auto-login is DISABLED.
- don't enable autopatch, telemetry
- enable location
- install updates
- remove from favorites sidebar all but nautilus, trashcan
- add terminal to favorites
- remove unused packages

2. Install c2f
```
$ sudo apt update
$ sudo apt install g++ libboost-all-dev libeigen3-dev python3-venv make git python3-tk

$ git clone https://github.com/fdobad/C2FSB
$ cd C2FSB
$ python3 -m venv pyenv
$ source pyenv/bin/activate
$ pip install -U -r requirements.txt

$ if [[ -d /usr/include/eigen3 ]]; then echo 'yes, continue'; else echo 'no, where is it? TODO!'; fi;
$ cd Cell2FireC
$ make
```

3. make desktop launcher
```
$ cd ~/Desktop
$ ln -s ~/C2FSB/dev/LaunchFireWindow.desktop .
```

4. exportar maquina virtual

## Windows vm with wsl creation

0. get vm image
- https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/
- click "Hyper-V (Gen2)"
- unzip

1. enable hyper-v
- open "start menu" (press super or windows key)
- type "Turn Windows features on or off"
- select "Hyper-V"
- click "ok"
- wait for installation, then reboot

2. create vm
- open "start menu" (press super or windows key)
- type "Hyper-V"
- click "Quick Create"
- click "Change Installation Source"
- click "Create Virtual Machine"

- rename virtual machine "VM"
- disable secure boot in vm settings, in uefi-bios?

3. enable ubuntu virtualization inside vm
- open "start menu" (press super or windows key)
- type "powershell"
- open "powershell" as administrator (2dary click on powershell icon to display option "Run as administrator")
- type "Set-VMProcessor -VMName VM -ExposeVirtualizationExtensions $true"

if failure, check: https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#error-0x80370102-the-virtual-machine-could-not-be-started-because-a-required-feature-is-not-installed

4. Run vm
- open "ubuntu on windows" from the taskbar
- configure UNIX username: "user", password: "p"

5. Install c2f
```
$ sudo apt update
$ sudo apt install g++ libboost-all-dev libeigen3-dev python3-venv make

$ git clone https://github.com/fdobad/C2FSB
$ cd C2FSB
$ python3 -m venv pyenv
$ source pyenv/bin/activate

$ if [[ -d /usr/include/eigen3 ]]; then echo 'yes, continue'; else echo 'no, where is it? TODO!'; fi;
$ cd Cell2FireC
$ make
```

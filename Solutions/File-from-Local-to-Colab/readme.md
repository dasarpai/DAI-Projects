wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

unzip ngrok-stable-linux-amd64.zip

docker run -it -e NGROK_AUTHTOKEN=2jJjT091qb1qksABahMqTA

# Transfer Files from local to colab using ngrok

Install ngrok on your local machine:

bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip

# Start ngrok:

bash
./ngrok http 8888

# Connect to the ngrok URL from Colab:
Use the public URL provided by ngrok to download files from your local machine to Colab.

python
!wget <ngrok-public-url>/path/to/your/file



### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
--2024-07-16 11:56:25--  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
Resolving bin.equinox.io (bin.equinox.io)... 52.202.168.65, 54.161.241.46, 54.237.133.81, ...
Connecting to bin.equinox.io (bin.equinox.io)|52.202.168.65|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13921656 (13M) [application/octet-stream]
Saving to: ‘ngrok-stable-linux-amd64.zip’

ngrok-stable-linux-amd64.zip  100%[=================================================>]  13.28M  4.14MB/s    in 4.5s

2024-07-16 11:56:31 (2.96 MB/s) - ‘ngrok-stable-linux-amd64.zip’ saved [13921656/13921656]

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ls
ngrok-stable-linux-amd64.zip  readme.md


D:\github\Solutions\File-from-Local-to-Colab>wsl

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ sudo apt install unzip
[sudo] password for hari:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  zip
The following NEW packages will be installed:
  unzip
0 upgraded, 1 newly installed, 0 to remove and 50 not upgraded.
Need to get 175 kB of archives.
After this operation, 386 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 unzip amd64 6.0-26ubuntu3.2 [175 kB]
Fetched 175 kB in 2s (80.2 kB/s)
Selecting previously unselected package unzip.
(Reading database ... 32522 files and directories currently installed.)
Preparing to unpack .../unzip_6.0-26ubuntu3.2_amd64.deb ...
Unpacking unzip (6.0-26ubuntu3.2) ...
Setting up unzip (6.0-26ubuntu3.2) ...
Processing triggers for man-db (2.10.2-1) ...

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ unzip ngrok-stable-linux-amd64.zip
Archive:  ngrok-stable-linux-amd64.zip
  inflating: ngrok

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ./ngrok http 8888
Usage of ngrok requires a verified account and authtoken.

Sign up for an account: https://dashboard.ngrok.com/signup
Install your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken

ERR_NGROK_4018


### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ vim ngrok.yml
### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ./ngrok http 8888
Preparing to unpack .../unzip_6.0-26ubuntu3.2_amd64.deb ...
Unpacking unzip (6.0-26ubuntu3.2) ...
Setting up unzip (6.0-26ubuntu3.2) ...
Processing triggers for man-db (2.10.2-1) ...
### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ unzip ngrok-stable-linux-amd64.zip
Archive:  ngrok-stable-linux-amd64.zip
  inflating: ngrok
### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ./ngrok http 8888
Usage of ngrok requires a verified account and authtoken.

Sign up for an account: https://dashboard.ngrok.com/signup
Install your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken

ERR_NGROK_4018


### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ !./ngrok authtoken 2j981ANvRPfUvfXHjMhH3OFuyVO_5NoBbZXbip5Cq2626X3iw
./ngrok http 8888 authtoken 2j981ANvRPfUvfXHjMhH3OFuyVO_5NoBbZXbip5Cq2626X3iw
Sign up for an account: https://dashboard.ngrok.com/signup
Install your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken

ERR_NGROK_4018


### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ls -l ngrok
-rwxrwxrwx 1 hari hari 30137501 Feb 10  2023 ngrok

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ chmod +x ngrok

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ sudo apt install net-tools
[sudo] password for hari:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  net-tools
0 upgraded, 1 newly installed, 0 to remove and 50 not upgraded.
Need to get 204 kB of archives.
After this operation, 819 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 net-tools amd64 1.60+git20181103.0eebece-1ubuntu5 [204 kB]
Fetched 204 kB in 2s (135 kB/s)
Selecting previously unselected package net-tools.
(Reading database ... 32540 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20181103.0eebece-1ubuntu5_amd64.deb ...
Unpacking net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Setting up net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Processing triggers for man-db (2.10.2-1) ...

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ netstat -an | grep 8888
tcp6       0      0 :::8888                 :::*                    LISTEN

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ mkdir old
### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ mv ngrok old
### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ ls
ngrok-stable-linux-amd64.zip  ngrok.yml  ngrok.zip  old  readme.md


### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ docker run -it -e NGROK_AUTHTOKEN=2jJjT091qb1qksABahMqTArBOGI_3c5rj6ymZZ1Wf2Da9hshr ngrok/ngrok http 80
Unable to find image 'ngrok/ngrok:latest' locally
latest: Pulling from ngrok/ngrok
0bc3020d05f1: Pull complete
bc43e81723d8: Pull complete
734ba79ea24c: Pull complete
3d971b9f5cc1: Pull complete
5d3c0d88f4d6: Pull complete
1d80241c79c8: Pull complete
0af772b69e49: Pull complete
47a8a5373497: Pull complete
5c9497e8d83e: Pull complete
Digest: sha256:7e726f8f404c12d858d66d1d676eaf12b6618072406b3160eb6cf6f7f7b34b40
Status: Downloaded newer image for ngrok/ngrok:latest
sion. Paid accounts are currently excluded from minimum agent version requirements. To begin handling traffic immediately without updating your agent, upgrade to a paid plan: https://dashboard.ngrok.com/billing/subscription.

ERR_NGROK_121

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ docker run -it -e NGROK_AUTHTOKEN=2jJjT091qb1qksABahMqTArBOGI_3c5rj6ymZZ1Wf2Da9hshr ngrok/ngrok http 8080

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ jupyter server list
Command 'jupyter' not found, but can be installed with:
sudo apt install jupyter-core

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$ sudo apt install jupyter-core
[sudo] password for hari:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-distutils python3-ipython-genutils python3-jupyter-core python3-lib2to3 python3-traitlets
Suggested packages:
  python3-pip
The following NEW packages will be installed:
  jupyter-core python3-distutils python3-ipython-genutils python3-jupyter-core python3-lib2to3 python3-traitlets
0 upgraded, 6 newly installed, 0 to remove and 50 not upgraded.
Need to get 344 kB of archives.
After this operation, 1841 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 python3-traitlets all 5.1.1-1 [81.2 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/universe amd64 python3-ipython-genutils all 0.2.0-5 [21.9 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-lib2to3 all 3.10.8-1~22.04 [77.6 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-distutils all 3.10.8-1~22.04 [139 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy/universe amd64 python3-jupyter-core all 4.9.1-1 [20.3 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/universe amd64 jupyter-core all 4.9.1-1 [4388 B]
Fetched 344 kB in 2s (149 kB/s)
Selecting previously unselected package python3-traitlets.
(Reading database ... 32589 files and directories currently installed.)
Preparing to unpack .../0-python3-traitlets_5.1.1-1_all.deb ...
Unpacking python3-traitlets (5.1.1-1) ...
Selecting previously unselected package python3-ipython-genutils.
Preparing to unpack .../1-python3-ipython-genutils_0.2.0-5_all.deb ...
Unpacking python3-ipython-genutils (0.2.0-5) ...
Selecting previously unselected package python3-lib2to3.
Preparing to unpack .../2-python3-lib2to3_3.10.8-1~22.04_all.deb ...
Unpacking python3-lib2to3 (3.10.8-1~22.04) ...
Selecting previously unselected package python3-distutils.
Preparing to unpack .../3-python3-distutils_3.10.8-1~22.04_all.deb ...
Unpacking python3-distutils (3.10.8-1~22.04) ...
Selecting previously unselected package python3-jupyter-core.
Preparing to unpack .../4-python3-jupyter-core_4.9.1-1_all.deb ...
Unpacking python3-jupyter-core (4.9.1-1) ...
Selecting previously unselected package jupyter-core.
Preparing to unpack .../5-jupyter-core_4.9.1-1_all.deb ...
Unpacking jupyter-core (4.9.1-1) ...
Setting up python3-ipython-genutils (0.2.0-5) ...
Setting up python3-traitlets (5.1.1-1) ...
Setting up python3-lib2to3 (3.10.8-1~22.04) ...
Setting up python3-distutils (3.10.8-1~22.04) ...
Setting up python3-jupyter-core (4.9.1-1) ...
Setting up jupyter-core (4.9.1-1) ...
Processing triggers for man-db (2.10.2-1) ...

### hari@Hari-MSI:/mnt/d/github/Solutions/File-from-Local-to-Colab$

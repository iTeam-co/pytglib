#!/usr/bin/bash

sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo add-apt-repository ppa:ubuntu-toolchain-r/test

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y alien libstdc++6 musl-dev libssl-dev openssl gcc clang zlib1g zlib1g-dev 
sudo apt install -y python3 python3-dev python3-apt python3.6 python3.6-dev
sudo apt install -y python3.7 python3.7-dev

sudo ln -s /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1

wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4.3_amd64.deb
alien -i libssl1.1_1.1.0g-2ubuntu4.3_amd64.deb.deb

wget https://www.openssl.org/source/openssl-1.1.1a.tar.gz --no-check-certificate
tar -zxf openssl-1.1.1a.tar.gz && cd openssl-1.1.1a
./config
make
make test
make install
sudo mv /usr/bin/openssl ~/tmp
sudo ln -s /usr/local/bin/openssl /usr/bin/openssl

sudo ldconfig

python3.6 -m pip install pytglib

python3.6 setup.py install

echo "Ready to go!"

#!/bin/bash

out_dir=$1

echo 'to be run with SUDO'

sudo apt-get update
sudo apt-get install gcc make build-essential python-dev git scons swig
sudo echo 'blacklist snd_bcm2835' > /etc/modprobe.d/snd-blacklist.conf

cd $out_dir

git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
sudo scons
cd python
sudo python setup.py build
sudo python setup.py install

sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py

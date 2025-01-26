latest 1/10/2025

Install Raspberry Pi OS using Raspberry Pi Imager https://www.raspberrypi.com/software/
Prepare micoreSD Card and adapter
Prepare the power bank/transformer for Raspberry Pi 4b
mouse, keyboard, microHDMI
Raspberry Pi OS (64-bit)
32GB SD Card

create Raspberry Pi account
use the same network then Raspberry Pi connect https://connect.raspberrypi.com/devices



sudo shutdown -h now

sudo apt update
sudo apt-get update
sudo apt upgrade

sudo apt update && sudo apt install --only-upgrade rpi-connect

sudo apt remove python3-rpi.gpio
sudo apt install python3-rpi-lgpio

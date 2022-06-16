# DO Setup (https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
apt update
apt upgrade

# Python Dependencies
apt install python3-pip
pip3 install numpy matplotlib scikit-learn biopython

# Git clone
git clone https://github.com/darmawanalbert/gassppi-benchmark.git

# MSMS
chmod 755 /root/gassppi-benchmark/msms/msms
sudo nano /etc/environment
# append /root/gassppi-benchmark/msms to PATH
source /etc/environment

nohup python3 run-benchmark.py &

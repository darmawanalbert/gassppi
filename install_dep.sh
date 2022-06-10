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

# Execute the benchmark
# Download from Google Colab
# Edit certain parts inside the file
# 1. Keep Global Variables, import warnings, and Class Residue chunk (delete the rest)
# 2. Change repository_path variable to "/root/gassppi-benchmark/"
# 3. Remove sample code -> is_same_residue, load_pdb, get_actual_interface, remove_hetatm_row, fitness_score
# 4. Remove tmalign_structural_alignment()
# 5. Remove PInet test set, generate template
# 6. Remove generate_pymol_script_file + all statistics
# 7. Remove draw_chart from verbose option (gass_ppi, dbd_sanity_test, dbd_all_templates)
# 8. Pick executables (e.g. sanity test only, etc)
# 9. Add time functionalities
# import time
# import math

# start_time = time.time()

# # Logic

# num_sec = int(time.time() - start_time)
# num_hours = math.floor(num_sec / (60 * 60))
# num_sec = num_sec % (60 * 60)
# num_minutes = math.floor(num_sec / 60)
# num_sec = num_sec % 60
# print("Executed in ", num_hours, "hours,", num_minutes, "minutes,", num_sec, "seconds")

nohup python3 run-benchmark.py &



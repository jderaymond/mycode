#!/usr/env/bin python3

import os
def main():
    home_dir = os.system("cd ~")
    install = os.system("sudo apt install sl")
    slappy = os.system("mkdir -p /home/student/mycode/slappy")
    mycode = os.system("cd ~/mycode/slappy/")
    text = os.system("touch /home/student/mycode/slappy/chad_stop_using_that_word.txt")

main()

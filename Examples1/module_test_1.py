import platform
import subprocess
import shutil

import matplotlib
import os
import sys

sys.path.append('../')
# from ore_examples_helper import OreExample

print(os.path.isfile("..\\App\\bin\\x64\\Release\\ore.exe"))

def print_on_console(line):
    print(line)
    sys.stdout.flush()


class OreExample(object):
    def __init__(self, dry=False):
        self.ore_exe = ""
        self.headlinecounter = 0
        self.dry = dry
        self.ax = None
        self.plot_name = ""
        self._locate_ore_exe()

    def _locate_ore_exe(self):
        if os.name == 'nt':
            if platform.machine()[-2:] == "64":
                if os.path.isfile("..\\App\\bin\\x64\\Release\\ore.exe"):
                    self.ore_exe = "..\\App\\bin\\x64\\Release\\ore.exe"
                elif os.path.isfile("..\\build\\App\\ore.exe"):
                    self.ore_exe = "..\\build\\App\\ore.exe"
                else:
                    print_on_console("ORE executable not found.")
                    quit()
            else:
                if os.path.isfile("..\\..\\App\\bin\\Win32\\Release\\ore.exe"):
                    self.ore_exe = "..\\..\\App\\bin\\Win32\\Release\\ore.exe"
                elif os.path.isfile("..\\..\\build\\App\\ore.exe"):
                    self.ore_exe = "..\\..\\build\\App\\ore.exe"
                else:
                    print_on_console("ORE executable not found.")
                    quit()
        else:
            if os.path.isfile("../../App/build/ore"):
                self.ore_exe = "../../App/build/ore"
            elif os.path.isfile("../../build/App/ore"):
                self.ore_exe = "../../build/App/ore"
            elif os.path.isfile("../../App/ore"):
                self.ore_exe = "../../App/ore"
            else:
                print_on_console("ORE executable not found.")
                quit()

    def print_headline(self, headline):
        self.headlinecounter += 1
        print_on_console('')
        print_on_console(str(self.headlinecounter) + ") " + headline)

    def get_times(self, output):
        print_on_console("Get times from the log file:")
        logfile = open(output)
        for line in logfile.readlines():
            if "ValuationEngine completed" in line:
                times = line.split(":")[-1].strip().split(",")
                for time in times:
                    print_on_console("\t" + time.split()[0] + ": " + time.split()[1])

    def run(self, xml):
        if not self.dry:
            if subprocess.call([self.ore_exe, xml]) != 0:
                print("raise exception")
                # raise Exception("Return Code was not Null.")



oreex = OreExample(sys.argv[1] if len(sys.argv)>1 else False)
oreex.print_headline("Run ORE to produce NPV cube and exposures")
oreex.run("Example_1/Input/ore.xml")
oreex.get_times("Example_1/Output/log.txt")


print("hello")


import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message.')
logging.warning('Another log message')

# from subprocess import Popen, PIPE

# process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print(stdout)

# import subprocess
# subprocess.call(["ls", "-l"])

# s = subprocess.check_output(["echo", "Hello World!"])
# print("s = " + s)

theproc = subprocess.Popen([sys.executable, "myscript.py"])
theproc.communicate()
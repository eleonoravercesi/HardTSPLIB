'''
Run concorde on the HardTSPLIB instances
Requires a working installation of concorde
@author E. Vercesi, S. Gualandi, M. Mastrolilli, L. M. Gambardella
'''

'''
Packages
'''
import argparse, os, subprocess

'''
Main
'''
if __name__ == "__main__":
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-concorde_path", type=str, help="Specify the path of the concorde executable")
    parser.add_argument("-instance", type=str,  help="TSP instance in TSPLIB format")
    parser.add_argument("-seed", type=int, help="Seed", default=42)
    args = parser.parse_args()
    concorde_path = args.concorde_path
    instance_path = args.instance
    seed = args.seed

    # Create a directory for the solution (if does not exist yes)
    try:
        os.makedirs('sol')
    except:
        pass

    # Create a directory where put all the intermediate files generated by concorde (if does not exists)
    try:
        os.makedirs('run')
    except:
        pass
    os.chdir("./run")


    # Set a name for the solution file (derived from the original name)
    solution_filename = "../sol/{}.sol".format(instance_path.split("/")[2].split(".")[0])

    # Add an extra-dot to the instance, as we are in the folder "run"
    instance_path = "." + instance_path

    # Run concorde on the specify instance
    subprocess.run("{}/concorde -x -s {} -o {} {}".format(concorde_path, seed, solution_filename, instance_path), shell=True)

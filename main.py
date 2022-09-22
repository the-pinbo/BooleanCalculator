import urp
import pcn
import bce


def run_cmd(in_file_path, out_file_path, command_file_path):
    calc = bce.BCE(in_file_path, out_file_path)
    calc.process(command_file_path)
    print("done")


if __name__ == "__main__":
    command_file_path = "./input/cmd1.txt"
    in_file_path = "./input"
    out_file_path = "./output"
    run_cmd(in_file_path, out_file_path, command_file_path)

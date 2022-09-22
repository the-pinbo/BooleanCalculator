import urp
import pcn
import bce


def compliment():
    filePath = r".\input\1.pcn"
    outFilePath = r".\output\1.pcn"
    numVars, cubes = pcn.parse(filePath=filePath)
    cubesNot = urp.complement(cubes)
    print(pcn.pcnToStr(cubesNot))
    pcn.write(cubesNot)


def run_cmd(in_file_path, out_file_path, command_file_path):
    calc = bce.BCE(in_file_path, out_file_path)
    calc.process(command_file_path)
    print("done")


if __name__ == "__main__":
    command_file_path = "./input/cmd1.txt"
    in_file_path = "./input"
    out_file_path = "./output"
    run_cmd(in_file_path, out_file_path, command_file_path)


# if __name__ == "__main__":
#     # this is for the compliment of a cube in PCN
#     compliment()

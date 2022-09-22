from itertools import islice
from itertools import chain


def parse(filePath):
    with open(filePath, "rb") as f:
        try:
            lines = iter(f)
            numVars = int(next(lines))
            cubeCount = int(next(lines))
            cubes = [None]*cubeCount

            for i in range(cubeCount):
                line = next(lines)
                cubes[i] = tuple(islice(map(int, line.split()), 1, None))

            return (numVars, tuple(cubes))

        except Exception as error:
            raise AssertionError("Bad pcn file {}".format(filePath)) from error


def findNumVars(cubes):
    return max(max(map(abs, cube)) for cube in cubes)


def pcn_to_str(cubes):
    repr = list()
    numVars = str(findNumVars(cubes))
    repr.append(numVars)
    numCubes = str(len(cubes))
    repr.append(numCubes)
    cubes = tuple(set(tuple(sorted(cube, key=abs)) for cube in cubes))
    for cube in cubes:
        repr.append(' '.join(map(str, chain((len(cube),), cube))))
    return "\n".join(repr)


def write_pcn(filePath, cubes):
    with open(filePath, "w") as f:
        f.write(pcn_to_str(cubes))

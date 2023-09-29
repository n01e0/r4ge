import r2pipe
import sys
from r4geHelper import *

r2proj = createR2Pipe()

if r2proj is None:
    print(colored("only callable inside a r2-instance", "red", attrs=["bold"]))
    exit(0)

def main(name, addr):
    addrs = [x['from'] for x in r2proj.cmdj(f'axtj @{addr}')]
    for i, addr in enumerate(addrs):
        r2proj.cmd(f'f {name}_{i} @{addr}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(colored("usage: python3 flagHelper.py <name> <addr>", "red", attrs=["bold"]))
        exit(0)
    main(sys.argv[1], sys.argv[2])

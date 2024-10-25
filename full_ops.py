# full_ops.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Brad Denby
# Other contributors: Josh Smith
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan')
n_wv = float('nan')

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
    ...
else:
    print(\
        'Usage: '\
            'python3 c_in n_wv ...'\
                )
    exit()

# write script below this line
adds=c_in*n_wv
muls=adds
c_out=c_in
divs=0
h_out=1
w_out=1

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
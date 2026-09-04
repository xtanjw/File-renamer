from pathlib import Path
import argparse
parser = argparse.ArgumentParser('Mass File Renamer')
parser.add_argument('-f','--folder', help='folder for files inside to rename. Both absolute and relative path are supported', required=True)
parser.add_argument('-e','--extension', help='What extension to look for', required=True)
parser.add_argument('-n', '--name', help='Template for rename. Use "#" to represent what will dynamically change. Eg: xyz# , #zyx , xyz#zyx. Do note that only the first occurange of # will be replaced', required=True)
parser.add_argument('-dn', '--dynnum', help='Replaces "#" with this, with the number given being used as the lower one. Default is 0', default=0, type=int)
parser.add_argument('-v','--verbose', help='See what file gets renamed to what', action='store_true')
args = parser.parse_args()
p = Path(args.folder)
extension = args.extension
name = args.name
dynnum = args.dynnum
verbose = args.verbose
basename = name[0:name.find('#')] + str(dynnum) + name[name.find('#') + 1:len(name)]
if p.is_absolute():
    for files in p.glob('*.' + extension):
        renamed = name[0:name.find('#')] + str(dynnum) + name[name.find('#')+1:len(name)] + '.' + extension
        files.rename(p / renamed)
        dynnum += 1
        if verbose:
            print(f'File "{files}" has been renamed to "{p / renamed}"')
else:
    for files in p.glob('*.' + extension):
        renamed = name[0:name.find('#')] + str(dynnum) + name[name.find('#') + 1:len(name)] + '.' + extension
        files.rename(p / renamed)
        dynnum += 1
        if verbose:
            print(f'File {files} has been renamed to {p / renamed}')
print('Done!')

import os
from os.path import abspath, join, getsize
import sys

if len(sys.argv) > 1:
    search_path = sys.argv[1]
else:
    search_path = "/workspaces/reporting-file-sizes"

for item in os.listdir(search_path):
  if os.path.isdir(item):
    print("This is a directory {0}".format(item))
  else:
    print("This is a file: {0}".format(item))


sizes = {}

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        #break

sorted_results = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_results[:20]:
    if sizes[path] >= 1024 ** 3:
      print("File with Path: {0}, has a size: {1} mb.".format(path, sizes[path]/ 1024 ** 3))
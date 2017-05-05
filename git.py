#!/usr/bin/env python

import git # pip install GitPython

repo = git.Repo(os.getcwd())
# git text line by line
diff_text = repo.git.diff('--staged', version_file_path).split('\n')
print diff_text

diff_files = repo.git.diff('--staged', '--name-only').split('\n')
print diff_files


pushd $(git rev-parse --show-toplevel)
tools/copy_openstack_code.sh
git add .;git add -u
git commit -m 'copy-code'
ctags -R --exclude=".tox" --exclude="test" --exclude="venv" --exclude="upstream"
# 'pycscope -R' cost too much time to index
pycscope $(find . -name "*.py" -not -path "*venv/*" -not -path "*tox/*" -not -path "*test/*" -not -path "*tempest/*" -not -path "*upstream/*")
popd

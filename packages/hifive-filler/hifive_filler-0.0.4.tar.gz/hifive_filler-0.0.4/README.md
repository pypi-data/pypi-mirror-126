# hifive_filler

This is a small program to take part in the Python Rush challenge in Piscine 101 of Tokyo42.

## Building && Deploying
- `python3 -m venv myenv`
- `source myenv/bin/activate`
- `pip install --upgrade setuptools`
- `pip install --upgrade build`
- `pip install --upgrade twine`
- `rm -rf dist/*`
- `python3 -m build`
- `twine upload dist/*`
- `deactivate`

### Deployment

To deploy this to PyPI an account is necessary. The login details will be queried upon executing `twine upload dist/*`.

## Installing && Executing (Example)
- `python3 -m venv liveenv`
- `source liveenv/bin/activate`
- `pip install --upgrade hifive_filler`
- `./resources/filler_vm -t 3 -p1 hifive_filler -p2 resources/players/carli.filler -f resources/maps/map00`
- `deactivate`

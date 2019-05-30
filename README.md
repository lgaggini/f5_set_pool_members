# f5_set_pool_members

python script to change the status of a pool members on F5 using the [F5 iControl® REST Python API](https://github.com/F5Networks/f5-common-python)

## Install
### Clone
```bash
git clone git@git.dadapro.net:lgaggini/f5_set_pool_members.git
```

### Requirements
```bash
pip install -r requirements.txt
```
## Configuration
Configure your credentials and your endpoint in a settings file which will be included.
```python
ENDPOINT='my.endpoint.it'
USER='myuser'
PASS='mypass'
```

## Usage

```bash
usage: f5_set_pool_members.py [-h] -p {popper-stag-priv-http} -s
                              {enabled,disabled,forced_offline} [-r]

enables, disables and forces offline f5 pools members

optional arguments:
  -h, --help            show this help message and exit
  -p {popper-stag-priv-http}, --pool {popper-stag-priv-http}
                        pool to work with
  -s {enabled,disabled,forced_offline}, --state {enabled,disabled,forced_offline}
                        pool to work with
  -r, --readonly        readonly mode for debug (default disabled)
```

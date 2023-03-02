
# Main Setup
## Step1: Basic Ubuntu Packages
```
$(SSH_CMD) -- 'bash -s' < /active/starter/ub1804/start.sh
```
**NOTES**
+ test oh my zsh manually


## Step2: Nopasswd & Useful Root Directory
```
$(SSH_CMD) -- 'sudo bash -s' < /active/starter/ub1804/qtwu.sh
```
**NOTES**
+ `/etc/sudoers` is involved, *it may corrupt the entire OS*


## Step3: Python
```
$(SSH_CMD) -- 'bash -s' < /active/starter/ub1804/python.sh
```
**NOTES**
+ pyenv without conda screwed for some reason, verify if everything is compiled
+ `/active` is added under python default path
+ Install "common" packages yourself


# Optional

## Jupyter
```
$(SSH_CMD) -- 'bash -s' < /active/starter/ub1804/optional/jupyter.sh
```
**NOTES**
+ Make sure the port is allowed at the cloud
+ Use a local library to generate hashed password
+ Enable jupyter plugins manually


## GPU
```
$(SSH_CMD) -- 'bash -s' < /active/starter/ub1804/optional/cuda.sh
```
**NOTES**
+ *Google cloud platform* only
+ It's simple, no UI
+ To test: `nvidia-smi`

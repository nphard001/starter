# Step1: Basic Ubuntu Packages
```
$(SSH_CPU0) -- 'bash -s' < /active/starter/ub1804/start.sh
```
> test oh my zsh manually


# Step2: Nopasswd & Useful Root Directory
```
$(SSH_CPU0) -- 'sudo bash -s' < /active/starter/ub1804/qtwu.sh
```


# Step3: Python
```
$(SSH_CPU0) -- 'bash -s' < /active/starter/ub1804/python.sh
```
**NOTES**
+ pyenv without conda screwed for some reason, verify if everything is compiled


# Step4: Jupyter
```
$(SSH_CPU0) -- 'bash -s' < /active/starter/ub1804/optional.sh
```
**NOTES**
+ make sure the port is allowed at the cloud
+ use a local library to generate hashed password


export NOPASSWD_USER=$1
echo "username = $NOPASSWD_USER"
echo "$NOPASSWD_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
custom_dir()
{
  mkdir /$1
  chown $NOPASSWD_USER /$1
}
custom_dir active
custom_dir dat
custom_dir tmp2

test (\
"$(python3 --version)"\
=\
"Python 3.5.3"\
&&\
echo "OK, python3==python3.5.3")
||\
echo "Not 3.5.3"
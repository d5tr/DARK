#!/bin/bash

#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root/DARK && sudo python3 DARK.py

else

echo 'you must be root ! '
echo 'use sudo'

fi

#!/usr/bin/env bash
#
# Script to execute the SIGHT Python Module
#

sight() {
    
    python ${project_path}/src/SIGHT.py $img ${project_path}/data/SIGHT_KnowledgeBase.txt
}

#
# Script to get the image name and replace any spaces in the name with underscore(_)
#

get_image() {

    img=`ls -t ${project_path}/image/*.png | head -1` # Get the latest png file showing up
    mv -v "$img" $(echo "$img" | tr ' ' '_') # Replace spaces with underscore (_)
    img=`ls -t ${project_path}/image/*.png | head -1` # Store the new name in the img variable

}

#
# Daemon Script to poll a directory; detect changes and act if there has been any new file
#

SIGHT_daemon() {

    chsum1=""
    # Starting the daemon

    while [[ true ]]
    do
        chsum2=`find ${project_path}/image/ -type f -name "*.png" -exec md5 {} + | awk '{print $1}' | sort | md5`

        if [[ $chsum1 != $chsum2 ]] ; then           
            #Run the program that processes the image here
            get_image
            echo $img
            sight
            chsum1=$chsum2
            #echo $chsum1 $chsum2
        fi
        sleep 3 # Sleep timer is 3 seconds which can be calibrated
        #echo "sleeping..."
    done

}

#
# Main Script
#

if [[ $# -ne 1 ]] ; then
    echo
    "
    Invalid number of arguments.
    One needed, $# supplied. 
    Exiting..."
    exit -1
fi

project_path=$1
mkdir ${project_path}/image/tmp
SIGHT_daemon


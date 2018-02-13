#!/bin/bash

PROJECT_FOLDER=~/Documents/Developer/Python/OttoBotDaemon
ARCHIVE=app.zip

VIRTUAL_ENV=/Users/drabekj/.virtualenvs/OttoBotDaemon
DEPENDENCIES=${VIRTUAL_ENV}/lib/python3.6/site-packages

# If the the archive file already exists cancel
if [ -f ${PROJECT_FOLDER}/${ARCHIVE} ]; then
    echo "Such file already exists!"
    exit
fi

# zip dependencies
cd ${DEPENDENCIES}
zip -r9 ${PROJECT_FOLDER}/${ARCHIVE} *
# zip function code
cd ${PROJECT_FOLDER}
zip -r9 ${ARCHIVE} lambda_function.py
zip -r9 ${ARCHIVE} storage
# zip config file
cd ${PROJECT_FOLDER}
zip -r9 ${ARCHIVE} rds_config.py

echo "Archive created"
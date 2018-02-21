#!/bin/bash

PROJECT_FOLDER=~/Documents/Developer/Python/Alexa/OttoBot/OttoBotStockScraper
ARCHIVE=app.zip
AWS_S3_BUCKET=s3://ottobotstockscraperdaemonbucket/

VIRTUAL_ENV=/Users/drabekj/.virtualenvs/OttoBotStockScraper
DEPENDENCIES=${VIRTUAL_ENV}/lib/python3.6/site-packages

# If the the archive file already exists cancel
if [ -f ${PROJECT_FOLDER}/${ARCHIVE} ]; then
    echo "Such file already exists!"

    if [ "$1" == "-d" ]; then
        echo "Deleting existing zip archive."
        rm ${PROJECT_FOLDER}/${ARCHIVE}
    else
        exit
    fi
fi

# zip dependencies
echo "Creating archive..."
cd ${DEPENDENCIES}
zip -r9 ${PROJECT_FOLDER}/${ARCHIVE} * > /dev/null
# zip function code
cd ${PROJECT_FOLDER}
zip -r9 ${ARCHIVE} lambda_function.py > /dev/null
zip -r9 ${ARCHIVE} storage > /dev/null
zip -r9 ${ARCHIVE} provider > /dev/null
echo "Archive created"

if [ "$2" == "-u" ]; then
    echo "Uploading archive to AWS S3"
    aws s3 cp ${ARCHIVE} ${AWS_S3_BUCKET}
fi

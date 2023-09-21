#!/bin/sh

while [ 1 ]; do
    echo ""
    echo "Commands: exit, read, add, remove."
    read -p 'command: ' command

    if [ $command == "exit" ]; then
        exit

    elif [ $command == "read" ]; then
        read -p 'file_path: ' file_path
        if [ ! -f $file_path ]; then
            echo "File not found!"
            continue
        fi
        cat $file_path

    elif [ $command == "add" ]; then
        read -p 'file_path: ' file_path
        if [ ! -f $file_path ]; then
            echo test >> $file_path
            if [ $? -ne 0 ] ; then
                echo "Directory the file is in was not found!"
                continue
            fi
            rm $file_path
        fi
        read -p 'str: ' str
        echo $str >> $file_path

    elif [ $command == "remove" ]; then
        read -p 'file_path: ' file_path
        if [ ! -f $file_path ]; then
            echo "File not found!"
            continue
        fi
        read -p 'line: ' line
        if [ "$(sed -n $line"p" $file_path)" == "" ]; then
            echo "Line not found!"
        fi
        sed -i $line'd' $file_path

    else
        echo "Command was not recognized"
    fi
done

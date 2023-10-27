#!/bin/bash

concat_two_strings() {
    string1=$1" "$2
    echo $string1
}

first_name='Trinity'
last_name="Vermuelen"

newFirst="Nico"
newLast="Watson"

concat_two_strings $first_name $last_name
concat_two_strings $newFirst $newLast 


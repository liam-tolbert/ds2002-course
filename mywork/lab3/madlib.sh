#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "Please give me an adjective: " ADJ1
read -p "Please give me a noun: " NOUN1
read -p "Please give me another adjective: " ADJ2
read -p "Please give me a verb: " VERB1
read -p "Please give me another noun: " NOUN2
read -p "Please give me a color: " COLOR1
read -p "Please give me an animal: " ANIMAL1
read -p "Please give me a verb ending in -ing: " VERB_ING1

echo "Once upon a time, there was a $ADJ1 $NOUN1 who lived in a $ADJ2 $NOUN2. Every day, they would $VERB1 while admiring the beautiful $COLOR1 sky. One day, they encountered a $ANIMAL1 $VERB_ING1 in the forest."

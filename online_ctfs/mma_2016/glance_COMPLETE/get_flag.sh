#!/bin/bash

convert glance*.gif frame%04d.png
convert frame*.png +append flag.png
eog flag.png
rm frame*.png

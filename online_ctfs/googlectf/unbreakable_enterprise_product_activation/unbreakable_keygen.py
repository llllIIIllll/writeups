#!/usr/bin/python

# Google CTF
# keygen for Unbreakable Enterprise Product Activation
serial = "###############"

# [ INDEXES ]												[ FAILURE CODE ]
indexes = [
[0x6042e6,0x6042de,0x6042c6,0x6042c8,0x6042c0],				# 0x0ff

# movzx      edx, byte [ds:0x6042e6]	// buffer[38]
# movzx      eax, byte [ds:0x6042de]	// buffer[30]
# movzx      ecx, byte [ds:0x6042c6]	// buffer[6]
# movzx      esi, byte [ds:0x6042c8]	// buffer[8]
# movzx      edi, byte [ds:0x6042c0]	// buffer[0]
# xor        eax, edx
# sub        eax, esi
# add        eax, ecx
# cmp        dil, al
# buffer[0] = ( buffer[30] ^ buffer[38] ) - buffer[8] + buffer[6];

[0x6042d3,0x6042d4,0x6042e6,0x6042ea,0x6042c1],				# 0x100

# movzx      eax, byte [ds:0x6042d3]	// buffer[19]
# movzx      edx, byte [ds:0x6042d4]	// buffer[20]
# movzx      ecx, byte [ds:0x6042e6]	// buffer[38]
# movzx      esi, byte [ds:0x6042ea]	// buffer[42]
# movzx      edi, byte [ds:0x6042c1]	// buffer[1]
# xor        eax, edx
# xor        eax, ecx
# xor        eax, esi
# cmp        dil, al
# buffer[1] = ( ( buffer[19] ^ buffer[20] ) ^ buffer[38] ) ^ buffer[42]

[0x6042e4,0x6042e3,0x6042d3,0x6042c3,0x6042ec,0x6042c2],	# 0x101

# movzx      eax, byte [ds:0x6042e4]	// buffer[36]
# movzx      edx, byte [ds:0x6042e3]	// buffer[35]
# movzx      ecx, byte [ds:0x6042d3]	// buffer[19]
# movzx      esi, byte [ds:0x6042c3]	// buffer[3]
# movzx      edi, byte [ds:0x6042ec]	// buffer[44]
# movzx      r8d, byte [ds:0x6042c2]	// buffer[2]
# add        eax, edx
# sub        eax, ecx
# sub        eax, esi
# sub        eax, edi
# cmp        r8b, al
# buffer[2] = ( buffer[36] + buffer[35] ) - buffer[19] - buffer[3] - buffer[44];

[0x6042e9,0x6042ca,0x6042ca,0x6042d1,0x6042d3,0x6042c3],	# 0x102

# movzx      eax, byte [ds:0x6042e9]	// buffer[41]
# movzx      edx, byte [ds:0x6042ca]	// buffer[10]
# movzx      ecx, byte [ds:0x6042ca]	// buffer[10]
# movzx      esi, byte [ds:0x6042d1]	// buffer[17]
# movzx      edi, byte [ds:0x6042d3]	// buffer[19]
# movzx      r8d, byte [ds:0x6042c3]	// buffer[3]
# sub        eax, edx
# sub        eax, ecx
# xor        eax, esi
# add        eax, edi
# cmp        r8b, al
# buffer[17] = (buffer[19] - buffer[3]) ^ ( ( buffer[41] - buffer[10] - buffer[10] );

[0x6042e1,0x6042d5,0x6042c4],								# 0x103

# movzx      eax, byte [ds:0x6042e1]	// buffer[33]
# movzx      ecx, byte [ds:0x6042d5]	// buffer[21]
# movzx      edx, byte [ds:0x6042c4]	// buffer[4]
# sub        eax, ecx
# cmp        dl, al

[0x6042e7,0x6042c8,0x6042c4,0x6042c4,0x6042c5],				# 0x104

# movzx      eax, byte [ds:0x6042e7] ; XREF=sub_400590+82
# movzx      edx, byte [ds:0x6042c8]
# movzx      ecx, byte [ds:0x6042c4]
# movzx      esi, byte [ds:0x6042c4]
# movzx      edi, byte [ds:0x6042c5]
# xor        eax, edx
# xor        eax, ecx
# xor        eax, esi
# cmp        dil, al

[0x6042d9,0x6042ca,0x6042e7,0x6042ce,0x6042c6],				# 0x105

# movzx      eax, byte [ds:0x6042d9] ; XREF=sub_400590+89
# movzx      edx, byte [ds:0x6042ca]
# movzx      ecx, byte [ds:0x6042e7]
# movzx      esi, byte [ds:0x6042ce]
# movzx      edi, byte [ds:0x6042c6]
# add        eax, edx
# sub        eax, ecx
# xor        eax, esi
# cmp        dil, al

[0x6042c1,0x6042cf,0x6042e0,0x6042c7],						# 0x106

# movzx      eax, byte [ds:0x6042c1] ; XREF=sub_400590+96
# movzx      edx, byte [ds:0x6042cf]
# movzx      esi, byte [ds:0x6042e0]
# movzx      ecx, byte [ds:0x6042c7]
# xor        eax, edx
# add        eax, esi
# cmp        cl, al

[0x6042c5,0x6042c5,0x6042c8,0x6042c8],						# 0x107

# movzx      eax, byte [ds:0x6042c5] ; XREF=sub_400590+103
# movzx      ecx, byte [ds:0x6042c5]
# movzx      esi, byte [ds:0x6042c8]
# movzx      edx, byte [ds:0x6042c8]
# add        eax, esi
# sub        eax, ecx
# cmp        dl, al

[0x6042c7,0x6042d8,0x6042c9],								# 0x108

# movzx      eax, byte [ds:0x6042c7] ; XREF=sub_400590+110
# movzx      ecx, byte [ds:0x6042d8]
# movzx      edx, byte [ds:0x6042c9]
# xor        eax, ecx
# cmp        dl, al

[0x6042d1,0x6042f1,0x6042c4,0x6042e0,0x6042ca],				# 0x109

# movzx      eax, byte [ds:0x6042d1] ; XREF=sub_400590+117
# movzx      edx, byte [ds:0x6042f1]
# movzx      ecx, byte [ds:0x6042c4]
# movzx      esi, byte [ds:0x6042e0]
# movzx      edi, byte [ds:0x6042ca]
# xor        eax, edx
# sub        eax, ecx
# add        eax, esi
# cmp        dil, al

[0x6042e6,0x6042ea,0x6042d1,0x6042c8,0x6042cb],				# 0x10a

# movzx      eax, byte [ds:0x6042e6] ; XREF=sub_400590+124
# movzx      edx, byte [ds:0x6042ea]
# movzx      ecx, byte [ds:0x6042d1]
# movzx      esi, byte [ds:0x6042c8]
# movzx      edi, byte [ds:0x6042cb]
# xor        eax, edx
# sub        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042c8,0x6042ce,0x6042cc],								# 0x10b

# movzx      eax, byte [ds:0x6042c8] ; XREF=sub_400590+131
# movzx      ecx, byte [ds:0x6042ce]
# movzx      edx, byte [ds:0x6042cc]
# add        eax, ecx
# cmp        dl, al

[0x6042d4,0x6042ed,0x6042cd],								# 0x10c

# movzx      eax, byte [ds:0x6042d4] ; XREF=sub_400590+138
# movzx      ecx, byte [ds:0x6042ed]
# movzx      edx, byte [ds:0x6042cd]
# add        eax, ecx
# cmp        dl, al

[0x6042d9,0x6042f0,0x6042d4,0x6042c9,0x6042ce],				# 0x10d

# movzx      eax, byte [ds:0x6042d9] ; XREF=sub_400590+145
# movzx      edx, byte [ds:0x6042f0]
# movzx      ecx, byte [ds:0x6042d4]
# movzx      esi, byte [ds:0x6042c9]
# movzx      edi, byte [ds:0x6042ce]
# sub        eax, edx
# xor        eax, ecx
# add        eax, esi
# cmp        dil, al

[0x6042d2,0x6042df,0x6042cf],								# 0x10e

# movzx      eax, byte [ds:0x6042d2] ; XREF=sub_400590+152
# movzx      ecx, byte [ds:0x6042df]
# movzx      edx, byte [ds:0x6042cf]
# sub        eax, ecx
# cmp        dl, al

[0x6042ee,0x6042d8,0x6042d0],								# 0x10f

# movzx      eax, byte [ds:0x6042ee] ; XREF=sub_400590+159
# movzx      ecx, byte [ds:0x6042d8]
# movzx      edx, byte [ds:0x6042d0]
# xor        eax, ecx
# cmp        dl, al

[0x6042c2,0x6042cd,0x6042ef,0x6042f2,0x6042ce,0x6042d1],	# 0x110

# movzx      eax, byte [ds:0x6042c2] ; XREF=sub_400590+166
# movzx      edx, byte [ds:0x6042cd]
# movzx      edi, byte [ds:0x6042ef]
# add        eax, edx
# add        edi, eax
# movzx      eax, byte [ds:0x6042f2]
# movzx      esi, byte [ds:0x6042ce]
# movzx      ecx, byte [ds:0x6042d1]
# xor        eax, esi
# xor        eax, edi
# cmp        cl, al

[0x6042ec,0x6042e4,0x6042c3,0x6042c0,0x6042d2],				# 0x111

# movzx      eax, byte [ds:0x6042ec] ; XREF=sub_400590+173
# movzx      edi, byte [ds:0x6042e4]
# movzx      esi, byte [ds:0x6042c3]
# movzx      edx, byte [ds:0x6042c0]
# movzx      ecx, byte [ds:0x6042d2]
# add        eax, edi
# add        eax, edx
# sub        eax, esi
# cmp        cl, al

[0x6042de,0x6042e9,0x6042d9,0x6042dc,0x6042d3],				# 0x112

# movzx      eax, byte [ds:0x6042de] ; XREF=sub_400590+180
# movzx      edx, byte [ds:0x6042e9]
# movzx      ecx, byte [ds:0x6042d9]
# movzx      esi, byte [ds:0x6042dc]
# movzx      edi, byte [ds:0x6042d3]
# xor        eax, edx
# sub        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042ec,0x6042d9,0x6042d4],								# 0x113

# movzx      eax, byte [ds:0x6042ec] ; XREF=sub_400590+187
# movzx      ecx, byte [ds:0x6042d9]
# movzx      edx, byte [ds:0x6042d4]
# xor        eax, ecx
# cmp        dl, al

[0x6042dc,0x6042d6,0x6042d5,0x6042e7,0x6042d9,0x6042d5],	# 0x114

# movzx      eax, byte [ds:0x6042dc] ; XREF=sub_400590+194
# movzx      edx, byte [ds:0x6042d6]
# add        edx, eax
# movzx      eax, byte [ds:0x6042d5]
# movzx      ecx, byte [ds:0x6042e7]
# movzx      esi, byte [ds:0x6042d9]
# movzx      edi, byte [ds:0x6042d5]
# xor        eax, ecx
# xor        eax, edx
# add        eax, esi
# cmp        dil, al

[0x6042ec,0x6042c4,0x6042cc,0x6042df,0x6042de,0x6042d6],	# 0x115

# movzx      eax, byte [ds:0x6042ec] ; XREF=sub_400590+201
# movzx      edx, byte [ds:0x6042c4]
# movzx      ecx, byte [ds:0x6042cc]
# movzx      esi, byte [ds:0x6042df]
# movzx      edi, byte [ds:0x6042de]
# movzx      r8d, byte [ds:0x6042d6]
# sub        eax, edx
# sub        eax, ecx
# xor        eax, esi
# sub        eax, edi
# cmp        r8b, al

[0x6042e0,0x6042ce,0x6042e7,0x6042d7],						# 0x116

# movzx      eax, byte [ds:0x6042e0] ; XREF=sub_400590+208
# movzx      edx, byte [ds:0x6042ce]
# movzx      esi, byte [ds:0x6042e7]
# movzx      ecx, byte [ds:0x6042d7]
# sub        eax, edx
# xor        eax, esi
# cmp        cl, al

[0x6042d5,0x6042d2,0x6042c0,0x6042d5,0x6042d8],				# 0x117

# movzx      eax, byte [ds:0x6042d5] ; XREF=sub_400590+215
# movzx      edx, byte [ds:0x6042d2]
# movzx      ecx, byte [ds:0x6042c0]
# movzx      esi, byte [ds:0x6042d5]
# movzx      edi, byte [ds:0x6042d8]
# xor        eax, edx
# xor        eax, ecx
# xor        eax, esi
# cmp        dil, al

[0x6042cc,0x6042d1,0x6042c4,0x6042cb,0x6042d2,0x6042d9],	# 0x118

# movzx      edx, byte [ds:0x6042cc] ; XREF=sub_400590+222
# movzx      eax, byte [ds:0x6042d1]
# movzx      ecx, byte [ds:0x6042c4]
# movzx      esi, byte [ds:0x6042cb]
# movzx      edi, byte [ds:0x6042d2]
# movzx      r8d, byte [ds:0x6042d9]
# xor        eax, edx
# add        ecx, edi
# add        eax, ecx
# sub        eax, esi
# cmp        r8b, al

[0x6042e0,0x6042ee,0x6042d4,0x6042f1,0x6042da],				# 0x119

# movzx      eax, byte [ds:0x6042e0] ; XREF=sub_400590+229
# movzx      edx, byte [ds:0x6042ee]
# xor        edx, eax
# movzx      eax, byte [ds:0x6042d4]
# movzx      esi, byte [ds:0x6042f1]
# movzx      ecx, byte [ds:0x6042da]
# add        eax, esi
# add        eax, edx
# cmp        cl, al

[0x6042e7,0x6042d9,0x6042e4,0x6042f0,0x6042db],				# 0x11a

# movzx      eax, byte [ds:0x6042e7] ; XREF=sub_400590+236
# movzx      edx, byte [ds:0x6042d9]
# movzx      ecx, byte [ds:0x6042e4]
# movzx      esi, byte [ds:0x6042f0]
# movzx      edi, byte [ds:0x6042db]
# add        eax, edx
# add        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042cf,0x6042ce,0x6042dc],								# 0x11b

# movzx      eax, byte [ds:0x6042cf] ; XREF=sub_400590+243
# movzx      ecx, byte [ds:0x6042ce]
# movzx      edx, byte [ds:0x6042dc]
# xor        eax, ecx
# cmp        dl, al

[0x6042e3,0x6042ea,0x6042c1,0x6042dd],						# 0x11c

# movzx      eax, byte [ds:0x6042e3] ; XREF=sub_400590+250
# movzx      ecx, byte [ds:0x6042ea]
# movzx      esi, byte [ds:0x6042c1]
# movzx      edx, byte [ds:0x6042dd]
# add        eax, esi
# sub        eax, ecx
# cmp        dl, al

[0x6042c8,0x6042df,0x6042de,0x6042d8,0x6042de],				# 0x11d

# movzx      eax, byte [ds:0x6042c8] ; XREF=sub_400590+257
# movzx      edx, byte [ds:0x6042df]
# movzx      ecx, byte [ds:0x6042de]
# movzx      esi, byte [ds:0x6042d8]
# movzx      edi, byte [ds:0x6042de]
# sub        eax, edx
# sub        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042d2,0x6042dd,0x6042cf,0x6042ea,0x6042df],				# 0x11e

# movzx      eax, byte [ds:0x6042d2] ; XREF=sub_400590+264
# movzx      edx, byte [ds:0x6042dd]
# movzx      ecx, byte [ds:0x6042cf]
# movzx      esi, byte [ds:0x6042ea]
# movzx      edi, byte [ds:0x6042df]
# add        eax, ecx
# sub        eax, edx
# xor        eax, esi
# cmp        dil, al

[0x6042cf,0x6042c5,0x6042ec,0x6042ce,0x6042e0],				# 0x11f

# movzx      eax, byte [ds:0x6042cf] ; XREF=sub_400590+271
# movzx      edi, byte [ds:0x6042c5]
# movzx      esi, byte [ds:0x6042ec]
# movzx      edx, byte [ds:0x6042ce]
# movzx      ecx, byte [ds:0x6042e0]
# add        eax, edi
# add        eax, edx
# sub        eax, esi
# cmp        cl, al

[0x6042ed,0x6042cf,0x6042d4,0x6042e0,0x6042e1],				# 0x120

# movzx      eax, byte [ds:0x6042ed] ; XREF=sub_400590+278
# movzx      edx, byte [ds:0x6042cf]
# movzx      ecx, byte [ds:0x6042d4]
# movzx      esi, byte [ds:0x6042e0]
# movzx      edi, byte [ds:0x6042e1]
# sub        eax, edx
# xor        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042e1,0x6042c3,0x6042d4,0x6042ca,0x6042e2],				# 0x121

# movzx      eax, byte [ds:0x6042e1] ; XREF=sub_400590+285
# movzx      edx, byte [ds:0x6042c3]
# movzx      ecx, byte [ds:0x6042d4]
# movzx      esi, byte [ds:0x6042ca]
# movzx      edi, byte [ds:0x6042e2]
# xor        eax, edx
# sub        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042c6,0x6042eb,0x6042ec,0x6042ec,0x6042c1,0x6042e3],	# 0x122

# movzx      eax, byte [ds:0x6042c6] ; XREF=sub_400590+292
# movzx      edx, byte [ds:0x6042eb]
# movzx      ecx, byte [ds:0x6042ec]
# movzx      esi, byte [ds:0x6042ec]
# sub        eax, edx
# xor        eax, ecx
# mov        edi, eax
# movzx      eax, byte [ds:0x6042c1]
# movzx      r8d, byte [ds:0x6042e3]
# sub        eax, esi
# add        eax, edi
# cmp        r8b, al

[0x6042d9,0x6042df,0x6042dc,0x6042f1,0x6042e4],				# 0x123

# movzx      eax, byte [ds:0x6042d9] ; XREF=sub_400590+299
# movzx      edx, byte [ds:0x6042df]
# movzx      ecx, byte [ds:0x6042dc]
# movzx      esi, byte [ds:0x6042f1]
# movzx      edi, byte [ds:0x6042e4]
# add        eax, edx
# sub        eax, ecx
# xor        eax, esi
# cmp        dil, al

[0x6042df,0x6042e2,0x6042e2,0x6042cb,0x6042e5],				# 0x124

# movzx      eax, byte [ds:0x6042df] ; XREF=sub_400590+306
# movzx      edx, byte [ds:0x6042e2]
# movzx      ecx, byte [ds:0x6042e2]
# movzx      esi, byte [ds:0x6042cb]
# movzx      edi, byte [ds:0x6042e5]
# xor        eax, edx
# sub        eax, ecx
# add        eax, esi
# cmp        dil, al

[0x6042e4,0x6042db,0x6042c5,0x6042ea,0x6042e6],				# 0x125

# movzx      eax, byte [ds:0x6042e4] ; XREF=sub_400590+313
# movzx      edx, byte [ds:0x6042db]
# movzx      ecx, byte [ds:0x6042c5]
# movzx      esi, byte [ds:0x6042ea]
# movzx      edi, byte [ds:0x6042e6]
# xor        eax, edx
# sub        eax, ecx
# add        eax, esi
# cmp        dil, al

[0x6042c8,0x6042e5,0x6042e7],								# 0x126

# movzx      eax, byte [ds:0x6042c8] ; XREF=sub_400590+320
# movzx      ecx, byte [ds:0x6042e5]
# movzx      edx, byte [ds:0x6042e7]
# xor        eax, ecx
# cmp        dl, al

[0x6042dc,0x6042c7,0x6042ec,0x6042ca,0x6042e8],				# 0x127

# movzx      eax, byte [ds:0x6042dc] ; XREF=sub_400590+327
# movzx      edx, byte [ds:0x6042c7]
# movzx      ecx, byte [ds:0x6042ec]
# movzx      esi, byte [ds:0x6042ca]
# movzx      edi, byte [ds:0x6042e8]
# add        eax, edx
# xor        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042da,0x6042d1,0x6042c7,0x6042d4,0x6042e9],				# 0x128

# movzx      eax, byte [ds:0x6042da] ; XREF=sub_400590+334
# movzx      edx, byte [ds:0x6042d1]
# movzx      ecx, byte [ds:0x6042c7]
# movzx      esi, byte [ds:0x6042d4]
# movzx      edi, byte [ds:0x6042e9]
# xor        eax, edx
# xor        eax, ecx
# xor        eax, esi
# cmp        dil, al

[0x6042c1,0x6042f2,0x6042dc,0x6042ea],						# 0x129

# movzx      eax, byte [ds:0x6042c1] ; XREF=sub_400590+341
# movzx      edx, byte [ds:0x6042f2]
# movzx      ecx, byte [ds:0x6042dc]
# movzx      esi, byte [ds:0x6042ea]
# add        eax, edx
# sub        eax, ecx
# cmp        sil, al

[0x6042e1,0x6042ee,0x6042cf,0x6042eb],						# 0x12a

# movzx      eax, byte [ds:0x6042e1] ; XREF=sub_400590+348
# movzx      edx, byte [ds:0x6042ee]
# movzx      ecx, byte [ds:0x6042cf]
# movzx      esi, byte [ds:0x6042eb]
# add        eax, edx
# sub        eax, ecx
# cmp        sil, al

[0x6042ea,0x6042d8,0x6042d0,0x6042d5,0x6042ed,0x6042ec],	# 0x12b

# movzx      eax, byte [ds:0x6042ea] ; XREF=sub_400590+355
# movzx      edx, byte [ds:0x6042d8]
# movzx      edi, byte [ds:0x6042d0]
# add        eax, edx
# add        edi, eax
# movzx      eax, byte [ds:0x6042d5]
# movzx      esi, byte [ds:0x6042ed]
# movzx      ecx, byte [ds:0x6042ec]
# xor        eax, esi
# xor        eax, edi
# cmp        cl, al

[0x6042d6,0x6042e8,0x6042ed],								# 0x12c

# movzx      eax, byte [ds:0x6042d6] ; XREF=sub_400590+362
# movzx      ecx, byte [ds:0x6042e8]
# movzx      edx, byte [ds:0x6042ed]
# sub        eax, ecx
# cmp        dl, al

[0x6042cc,0x6042ee,0x6042c7,0x6042e3,0x6042ee],				# 0x12d

# movzx      eax, byte [ds:0x6042cc] ; XREF=sub_400590+369
# movzx      edx, byte [ds:0x6042ee]
# movzx      ecx, byte [ds:0x6042c7]
# movzx      esi, byte [ds:0x6042e3]
# movzx      edi, byte [ds:0x6042ee]
# sub        eax, edx
# sub        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042da,0x6042cf,0x6042e7,0x6042cc,0x6042ef],				# 0x12e

# movzx      eax, byte [ds:0x6042da] ; XREF=sub_400590+376
# movzx      edx, byte [ds:0x6042cf]
# movzx      ecx, byte [ds:0x6042e7]
# movzx      esi, byte [ds:0x6042cc]
# movzx      edi, byte [ds:0x6042ef]
# add        eax, edx
# xor        eax, ecx
# sub        eax, esi
# cmp        dil, al

[0x6042cf,0x6042c8,0x6042cb,0x6042f0],						# 0x12f

# movzx      eax, byte [ds:0x6042cf] ; XREF=sub_400590+383
# movzx      edx, byte [ds:0x6042c8]
# movzx      esi, byte [ds:0x6042cb]
# movzx      ecx, byte [ds:0x6042f0]
# sub        eax, edx
# xor        eax, esi
# cmp        cl, al

[0x6042e5,0x6042db,0x6042f1],								# 0x130

# movzx      eax, byte [ds:0x6042e5] ; XREF=sub_400590+390
# movzx      ecx, byte [ds:0x6042db]
# movzx      edx, byte [ds:0x6042f1]
# xor        eax, ecx
# cmp        dl, al

[0x6042c8,0x6042cd,0x6042d1,0x6042cf,0x6042d8,0x6042f2]]	# 0x131

# movzx      eax, byte [ds:0x6042c8] ; XREF=sub_400590+397
# movzx      edx, byte [ds:0x6042cd]
# movzx      edi, byte [ds:0x6042d1]
# add        eax, edx
# add        edi, eax
# movzx      eax, byte [ds:0x6042cf]
# movzx      esi, byte [ds:0x6042d8]
# movzx      ecx, byte [ds:0x6042f2]
# xor        eax, esi
# xor        eax, edi
# cmp        cl, al

print hex(0xFF + len(indexes))
addr = 0x6042c0
for row in indexes:
	for index in row:
		print "buffer[%d] " % ( index - addr ),
	print "\n" + "#"*10
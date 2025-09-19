#   DESKEDIT STUDIOS
#   M/B Harry Roberts with Python 3.13.7
#
#   Symon 6502 rom maker for the default machine 
#
#
#
#



# rom code
code = bytearray([
    0xA9, 0xff,          # lda #$ff
    0x8d, 0x02, 0x60,    # sta $6002

    0xa9, 0x88,          # lda #$08
    0x8d, 0x00, 0x70,    # sta $7000

    0xa9, 0x89,          # lda #$09
    0x8d, 0x01, 0x70,    # sta $7001

    0xa9, 0xa2,          # lda #$22
    0x8d, 0x02, 0x70#,    # sta $7002

    #0x4c, 0x05, 0xc0     # jmp $c005
])
# make rom data have (16384 - len(code)) NOP at the end
rom = code + bytearray([0xea] * (16384 - len(code)))
# add jmp $c000 at 0x2aea in the code
rom[0x2aea] = 0x4c
rom[0x2aeb] = 0x00
rom[0x2aec] = 0xc0
# write rom[] to build\\rom.6502
with open("build\\rom.6502", "wb") as out_file:
    out_file.write(rom)
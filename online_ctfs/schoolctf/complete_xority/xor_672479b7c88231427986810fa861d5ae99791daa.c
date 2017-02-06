#include <stdint.h>
#include <stdio.h>

int main() {
    const char *flag="SchoolCTF{#####################}";
    uint32_t *iflag = (uint32_t *)flag;
    uint32_t A;
    int i;
    for (i = 0; i < 8; i++) {
        A = iflag[i];
        A = (A << 3) ^ A;
        A = (A << 1) ^ A;
        A = (A >> 3) ^ A;
        A = (A << 3) ^ A;
        A = (A << 7) ^ A;
        printf("%x",A);
    }
    printf("\n");
}

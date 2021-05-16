#编译四个步骤

预编译：
gcc -E main.c -o .\temp\main.i

编译：
gcc -S .\temp\main.i -o .\temp\main.s

汇编：
gcc -c .\temp\main.s -o .\temp\main.o

链接：
gcc .\temp\main.o -o .\temp\main.exe

运行：
cd .\temp\
.\main.exe

"""
 * Write for loops to produce the following output, with each line 40
 * characters wide:
 *
 * ----------------------------------------
 * _-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-_-^-
 * 1122334455667788990011223344556677889900
 * ----------------------------------------
 *
 for(int j = 0; j < 2; j++) {
    for(int i = 1; i <= 10; i++) {
        System.out.print(i%10);
        System.out.print(i%10);
    }
}
"""
for i in range(1, 41):
    print("-", end='')

print()
for i in range(1, 11):
    print("_-^-", end='')
print()
for i in range(0, 2):
    for j in range(1,11):
        print(j%10, end='')
        print(j%10, end='')
print()
for i in range(1, 41):
    print("-", end='')
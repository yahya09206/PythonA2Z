"""
 * Write for loops to produce the following output:
 *
 * *
 * **
 * ***
 * ****
 * *****
 *

 for(int i = 1; i <= 5; i++) {
    for(int j = 0; j < i; j++)
        System.out.print("*");
    System.out.println();
}
"""

for i in range(1,6):
    for j in range(0,i):
        print("*", end='')
    print()
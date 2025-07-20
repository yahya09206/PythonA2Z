"""
 * Write nested for loops to produce the following output:
 *
 *     1
 *    2
 *   3
 *  4
 * 5
 *
 for(int i = 1; i <= 5; i++) {
    for(int j = 5 - i; j > 0; j--) {
        System.out.print(" ");
    }
    System.out.println(i);
}
"""
for i in range(1,6):
    for j in range(6-i, 0, -1):
        print(" ", end='')
    print(i)
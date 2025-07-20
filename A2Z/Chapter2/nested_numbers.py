"""
Write nested for loops that produce the following output:
000111222333444555666777888999
000111222333444555666777888999
000111222333444555666777888999
for(int i = 1; i <= 3; i++){
			for(int j = 0; j < 10; j++){
				for(int k = j; k <= j; k++){
					System.out.print(k%10);
					System.out.print(j);
				}
				System.out.print(j);
			}
			System.out.println();

"""

# print 3 rows of numbers
for i in range(0, 3):
    # range of numbers from 0-10
    for j in range(0, 10):
        for k in range(j, i):
            print(k%10, end='')
            print(j, end='')
        print(j, end='')
    print()

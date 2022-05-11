nterms = int(input("How long the field is? "))

table = [int(input(f"T[{i}]=")) for i in range(nterms + 1)]

print(table)

# rabbit_way = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]
# print(rabbit_way)

# Program to display the Fibonacci sequence up to n-th term


def fibonacci():
    fib = []
    # first two terms
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        fib.append(n1)
        fib.append(n2)
        while count < nterms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            fib.append(nth)
    return fib



fibo = fibonacci()


def road(way: list) -> int:
    count = 0
    current_u = 0

    for u in range(0, len(way)):
        if way[u] == 0:
            dif = u - current_u
            for j in range(0, len(fibo) - 1):

                if dif == fibo[j] and dif != 0:
                    current_u = u
                    count += 1
                    break
                else:

                    if j == len(fibo) - 2:
                        break
                    else:
                        continue

    return count


# print("A rabbit has to jump ", road(rabbit_way), "times to cross the field")
wyniki = open("wyniki_c2.txt", "w")
wyniki.write("Length of field is ")
wyniki.write(str(nterms))
wyniki.write('\n')
wyniki.write(str(table))
wyniki.write('\n')
wyniki.write("A rabbit has to jump ")
wyniki.write(str(road(table)))
wyniki.write("times to cross the field")

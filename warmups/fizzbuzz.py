#!?usr/bin/env python3
def main():
    with open('numfile.txt') as f:
        content = f.readlines()
    fizzbuzz_list = []
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for line in content:
        line = line.replace("\n","")
        if int(line) % 3 == 0 and int(line) % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
            fizzbuzz += 1
        elif int(line) % 3 == 0:
            fizzbuzz_list.append("Fizz")
            fizz += 1
        elif int(line) % 5 == 0:
            fizzbuzz_list.append("Buzz")
            buzz += 1
        else:
            fizzbuzz_list.append(line)
    print(fizzbuzz_list)
    print(f"Fizz: {fizz} Buzz: {buzz} FizzBuzz: {fizzbuzz}")
if __name__ == "__main__":
    main()

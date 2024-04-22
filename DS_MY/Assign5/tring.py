def main():
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        print(i, end=' ')
    print(0)

    try:
        token = 0
        while True:
            s, r, d = map(int, input("Enter sender, receiver, and data: ").split())
            print("Token passing:", end='')
            i, j = token, token
            while i % n != s:
                print(f" {j}->", end='')
                i += 1
                j = (j + 1) % n
            print(f" {s}")

            print(f"Sender {s} sending data: {d}")
            i = (s + 1) % n
            while i != r:
                print(f"Data {d} forwarded by {i}")
                i = (i + 1) % n
            print(f"Receiver {r} received data: {d}")
            token = s
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
from time import sleep


def ft_progress(lst):
    index = 1
    for i in lst:
        pourcent = int(index / len(lst) * 100)
        print(f"\rETA: 8.76s [{pourcent:3}%]i", end='')
        index += 1
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

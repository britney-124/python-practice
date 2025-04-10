from turtle import *
def main():
    color("blue")
    n = int(input())
    for i in range(n):
        forward(100)
        backward(100)
        left(360/n)
    done()
main()

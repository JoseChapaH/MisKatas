def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
try:
     open('config.py')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")
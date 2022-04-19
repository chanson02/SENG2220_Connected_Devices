import sys, serial, json

def get_input():
    response = None
    while response is None:
        print('\n\nCommand Line Interface\n0. Quit\n1. View Current Temperature\n2. Set LED On\n3. Set LED Off')
        usr_in = input('Your response: ')

        try:
            response = int(usr_in)
            if response not in [0, 1,2,3]:
                response = None
        except ValueError:
            print('That was an invalid response')

    if response == 0:
        sys.exit()
    return response

def read_serial():
    with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
        line = ser.readline()
    reading = line.decode('utf-8')
    return reading.replace('\n', '')

def write_serial(output):
    with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
        ser.write(output)
    return


def main():
    usr_in = get_input()

    if usr_in == 1:
        print(f"The current temperature is {read_serial()}")
    elif usr_in == 2:
        write_serial(b'1')
    else:
        write_serial(b'0')

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('exiting')
            break

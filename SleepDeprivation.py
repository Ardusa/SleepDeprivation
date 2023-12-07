import pigpio

def main() :
    pi = pigpio.pi("sleepdeprivation", 8888, False)
    pi.set_mode(17, pigpio.OUTPUT)
    pi.set_mode(27, pigpio.OUTPUT)
    print("Sleep Deprivation")
    print(pi.get_mode(17))

main()
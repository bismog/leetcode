# import time
# import io
# def block(file,size=65536):
 # while True:
     # nb = file.read(size)
     # if not nb:
        # break
     # yield nb

# def getLineCount(filename):
  # with io.open(filename,"r",encoding="utf-8") as f:
  # with open(filename,"r") as f:
      # return sum(line.count("\n") for line in block(f))

if __name__ == "__main__":
    import sys
    import os
    import string
    if len(sys.argv) != 2:
        print("error imput argument")
        sys.exit(-1)
    # if not os.path.isfile(sys.argv[1]) :
       # print(sys.argv + " is not a file")
       # sys.exit(-1)
    year_mask = 0xFFF00000
    month_mask = 0xF0000
    day_mask = 0xF800
    hour_mask = 0x7C0
    minute_mask = 0x3F
    input_time = string.atoi(sys.argv[1])
    year = (input_time & year_mask) >> 20
    month = (input_time & month_mask) >> 16
    day = (input_time & day_mask) >> 11
    hour = (input_time & hour_mask) >> 6
    minute = input_time & minute_mask

    print "formatted time is %r/%r/%r %r:%r(y/m/d h:m)" % (year, month, day, hour, minute)

    # start_time = time.time()
    # print(getLineCount(sys.argv[1]))
    # print time.time() - start_time , 'seconds'

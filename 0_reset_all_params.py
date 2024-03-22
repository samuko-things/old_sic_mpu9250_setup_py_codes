import time
from sic_pyserial_lib import SIC # samuko IMU compute


# portName = '/dev/ttyACM0'
portName = '/dev/ttyUSB0'
imu = SIC(portName)

for i in range(5):
  time.sleep(1.0)
  print(i+1, " sec")


if __name__ == "__main__":
  
  isSuccessful = imu.send("reset")
  if isSuccessful:
    print("\nSUCCESS: parameters reset successful\nrestart the imu cct to see effect.\n")
  else:
    print("\nERROR: parameters reset not successful\n")
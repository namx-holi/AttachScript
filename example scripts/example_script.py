
import time

f = open("example scripts/example_access_log.txt", "a")

f.write("[{}] Opened a file.\n".format(time.time()))

f.close()
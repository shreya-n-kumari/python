"""
This scripty prints the system date.
"""
import datetime
print(datetime.date.today())

time = datetime.datetime.now().time()

if __name__ == '__main__':
	print(time)


print("\nanother way....")
from datetime import datetime
def get_the_time():				#defining function without argument.
	return datetime.now()

print(get_the_time())
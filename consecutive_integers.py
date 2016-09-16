from itertools import groupby, chain
from operator import itemgetter
from datetime import datetime, timedelta

formatstr = '%H:%M'
#midnight = '00:00'

def startend2blocks(_start,_end,block=15):
	current = datetime.strptime(_start, formatstr)
	_end = datetime.strptime(_end, formatstr)
	blocks = []
	index = 0
	while current < _end:
		blocks.append((index, current))
		current += timedelta(0, 60*block)
		index += 1
	return blocks

#print(dayblock)
#data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
def findcontinuous_blocks(data):
	#import pdb; pdb.set_trace()
	continuous_blocks = []
	for k, g in groupby(enumerate(data), lambda ix: ix[0]-ix[1][0]):
		#import pdb; pdb.set_trace()
		block = list(map(itemgetter(1), g))
		continuous_blocks.append(block)

	return continuous_blocks




def get_start_time(schedules, duration):
	block_length = duration/15
	dayblocks = startend2blocks('09:00', '19:00', block=15)	
	blocks = list(set(sum([startend2blocks(*meeting) for meeting in chain(*schedules)],[])))
	for block in blocks:
		for dayblock in dayblocks:
			if dayblock[1] == block[1]:
				dayblocks.remove(dayblock)
				break

	for conblock in findcontinuous_blocks(dayblocks):
		if len(conblock) >= block_length:
			return datetime.strftime(conblock[0][1], formatstr)
	return None

schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]

print(get_start_time(schedules, 60))


import json
import sys
import operator

d = json.loads(sys.stdin.read())
print json.dumps(sorted(d.iteritems(), key=operator.itemgetter(1)))

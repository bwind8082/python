f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

## tshirt dai dyo bhai ena mate comment nakhu chhe sanket pachhi delete mari deje 

class Node:
	# A constructor to create a new Binary tree Node
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

var fs = require('fs'); 
var parse = require('csv-parse');

var csvData=[];
fs.createReadStream(req.file.path)
    .pipe(parse({delimiter: ':'}))
    .on('data', function(csvrow) {
        console.log(csvrow);
        //do something with csvrow
        csvData.push(csvrow);        
    })
    .on('end',function() {
      //do something with csvData
      console.log(csvData);
    });

def rightViewUtil(root, level, max_level):

	# Base Case
	if root is None:
		return

	# If this is the last node of its level
	if (max_level[0] < level):
		print "%d " % (root.data),
		max_level[0] = level

	# Recur for right subtree first, then left subtree
	rightViewUtil(root.right, level+1, max_level)
	rightViewUtil(root.left, level+1, max_level)


def rightView(root):
	max_level = [0]
	rightViewUtil(root, 1, max_level)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightView(root)


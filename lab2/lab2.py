import magic
import glob
import hashlib

filenames = glob.glob("Dokaz4/*")
CHALLENGE = "c15e32d27635f248c1c8b66bb012850e5b342119"


for filename in filenames: 
    # print(filename, magic.from_file(filename))
    # print(filename, magic.from_buffer(open(filename, "rb").read(2048)))
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        # print('-------------', filename, '-------------')
        # print(hashlib.md5(data).hexdigest())
        # print(hashlib.sha1(data).hexdigest())
        # print(hashlib.sha256(data).hexdigest())
        if hashlib.sha1(data).hexdigest() == CHALLENGE:
            print('----------', filename, '----------')
            print(filename, magic.from_file(filename))
            break

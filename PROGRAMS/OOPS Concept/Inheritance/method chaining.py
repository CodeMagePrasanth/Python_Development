class a:
    def call(self):
        print('Audio calling...')
    def message(self):
        print('message calling...')
class b(a):
    def call(self):
        a.call(self)
        print('video calling...')
    def fm(self):
        print('fm calling...')
    def listening(self):
        print('listening calling...')
obj = b()
obj.call()


'''
o/p ---.>

Audio calling...
video calling...
'''
#  i did changes

class a:
    def call(self):
        print('Audio calling...')
    def message(self):
        print('message calling...')
class b(a):
    def call(self):
        print('video calling...')
    def message(self):
        a.message(self)
        a.call(self)
        print('fm calling...')
    def listening(self):
        print('listening calling...')
obj = b()
obj.message()

'''
o/p
message calling...
Audio calling...
fm calling...

'''
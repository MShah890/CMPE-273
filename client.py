'''
################################## client.py #############################
# 
################################## client.py #############################
'''
import grpc
import datastore_pb2

class DatastoreClient():
    '''
    '''

    def __init__(self, host='192.168.0.1', port=3000):
        '''
        '''
        # TODO
        print('Client is connecting to Server at 192.168.0.1:3000...')
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

    def put(self, data):
        '''
        '''
        # TODO
        print('PUT Request: value = ' + data)
        return self.stub.put(datastore_pb2.Request(data=data))

    def get(self, id):
        '''
        '''
        # TODO
        print('GET Request: key = ' + id)
        return self.stub.get(datastore_pb2.Request(data=id))


client = DatastoreClient()

resp = client.put(data = 'foo')

print('PUT Response: key = ' + resp.data)

resp2 = client.get(id = resp.data)

print('GET Response: value = ' + resp2.data)


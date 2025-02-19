import grpc
from orders.proto import user_pb2, user_pb2_grpc

def fetch_user_details(user_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_pb2_grpc.UserServiceStub(channel)
    request = user_pb2.UserRequest(user_id=user_id)
    try:
        response = stub.GetUser(request)
        return {
            "user_id": response.user_id,
            "username": response.username,
            "email": response.email,
            "first_name": response.first_name,
            "last_name": response.last_name,
        }
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")
        return None

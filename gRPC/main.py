from fastapi import FastAPI
import time
import grpc

import send_text_pb2
import send_text_pb2_grpc

app = FastAPI()


def send_text_with_grpc(text):
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = send_text_pb2_grpc.SendTextStub(channel)  # Use the correct stub class
        request = send_text_pb2.Text(text=text)  # Create the request message
        response = stub.Send(request)  # Send the request message
        return response.sucess


@app.post("/send_text_grpc")
async def send_text_grpc(text: str):
    start_time = time.time()
    success = send_text_with_grpc(text)
    if success:
        print(f"Sending text using gRPC speed:{time.time() - start_time}")
        return {"message": f"Text received!"}
    else:
        return {"message": f"Failed to send text"}

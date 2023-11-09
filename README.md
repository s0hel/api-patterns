# API Architecture Patterns

This repository has examples of some of the most popular API architecture patterns seen throughout the web:
REST, GraphQL, gRPC, and WebSockets.

<h2>GraphQL</h2>

Taken from <a href="graphql.org">graphql.org</a>


A query language for your API

GraphQL is a query language for APIs and a runtime for fulfilling those queries with 
your existing data. GraphQL provides a complete and understandable description of the 
data in your API, gives clients the power to ask for exactly what they need and 
nothing more, makes it easier to evolve APIs over time, and enables powerful developer 
tools.


<h2>gRPC</h2>

Taken from <a href="https://aws.amazon.com/compare/the-difference-between-grpc-and-rest/">amazon</a>

gRPC is an open-source API architecture and system governed by the Cloud Native Computing Foundation. It’s based on the Remote Procedure Call (RPC) model. While the RPC model is broad, gRPC is a specific implementation.

<h3>What is RPC?</h3>
In RPC, client-server communications operate as if the client API requests were a local operation, or the request was internal server code.

In RPC, a client sends a request to a process on the server that is always listening for remote calls. In the request, it contains the server function to call, along with any parameters to pass. An RPC API uses a protocol like HTTP, TCP, or UDP as its underlying data exchange mechanism.

<h3>How is gRPC different from RPC?</h3>
gRPC is a system that implements traditional RPC with several optimizations. For instance, gRPC uses Protocol Buffers and HTTP 2 for data transmission.

It also abstracts the data exchange mechanism from the developer. For example, another widely used RPC API implementation, OpenAPI, requires developers to map RPC concepts to the HTTP protocol. But gRPC abstracts the underlying HTTP communication. These optimizations make gRPC faster, easier to implement, and more web-friendly than other RPC implementations. 

<h2>REST</h2>

<H3>What is REST?</H3>

REST is a software architecture approach that defines a set of rules to exchange data between software components. It’s based on HTTP, the standard communication protocol of the web. RESTful APIs manage communications between a client and a server through HTTP verbs, like POST, GET, PUT, and DELETE for create, read, update, and delete operations. The server-side resource is identified by a URL known as an endpoint. 


REST works as follows:

<ul>
<li>The client makes a request to create, modify, or delete a resource on the server</li>
<li>The request contains the resource endpoint and may also include additional parameters</li>
<li>The server responds, returning the entire resource to the client once the operation is complete</li>
<li>The response contains data in JSON format and status codes</li>
<li>APIs built using REST guidelines are called RESTful APIs or REST APIs.</li>
</ul>

Read about <a href="https://aws.amazon.com/what-is/restful-api/">RESTful APIs</a>

<h2>WebSockets</h2>

Taken from <a href="https://www.geeksforgeeks.org/web-socket-in-python/">geeksforgeeks</a>

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20191203183429/HTTP-Connection.png"/>

WebSocket is bidirectional, a full-duplex protocol that is used in the same scenario of client-server communication, unlike HTTP it starts from ws:// or wss://. It is a stateful protocol, which means the connection between client and server will keep alive until it is terminated by either party (client or server). After closing the connection by either of the client and server, the connection is terminated from both ends. 

Let’s take an example of client-server communication, there is the client which is a web browser and a server, whenever we initiate the connection between client and server, the client-server made the handshaking and decide to create a new connection and this connection will keep alive until terminated by any of them. When the connection is established and alive the communication takes place using the same connection channel until it is terminated. 

This is how after client-server handshaking, the client-server decide on a new connection to keep it alive, this new connection will be known as WebSocket. Once the communication link establishment and the connection are opened, message exchange will take place in bidirectional mode until connection persists between client-server. If anyone of them (client-server) dies or decide to close the connection is closed by both of the party. The way in which socket works is slightly different from how HTTP works, the status code 101 denotes the switching protocol in WebSocket. 
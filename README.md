# Server-Client-based-multiple-users-CHAT-Application
In this project you are going to build a networking system based application that has a server which can accept multiple client requests. You can use python based socket
programming in order to create the system. Each client can connect to the server anytime by sending a network request containing an IP, the server's port address and a unique name. Client’s name can never be ‘ALL’. The following tasks on the server side need to be done carefully.
  ● The server will print on its screen a confirmation message like “[The latest client name] just joined the chat” after receiving each request. And broadcast a message     “‘[The latest client name] just joined the server”.
  ● If the server accepts a request with a name “ALL”, it will immediately discard the request.
  ● If the server accepts a request with a name that is already on the server, it will immediately discard the request.

After connection setup, a client can send a message either to a specific client or to all of the clients.
1. When client A(Ashik) sends a message to client B (Rafid), a specific protocol has to be followed:
      ##Rafid*Hello, How are you?
Basically, the format is RecevierName*Message
The server then will handle this issue and send the message to the specific
receiver client.
2. Another protocol needs to be followed by the sender when it wants to
broadcast a message, that is, to send a message to all of the clients

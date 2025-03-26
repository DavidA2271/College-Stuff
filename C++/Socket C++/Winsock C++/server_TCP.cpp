#include <iostream>
#include <WinSock2.h>
#include <WS2tcpip.h>
using namespace std;


int main(int argc, char* argv[]) {
	SOCKET serverSocket, acceptSocket;
	int port = 6103;

	cout << "\n\nLocating WinSock.\n" << endl;

	WSADATA wsaData;
	int wsaerr;
	WORD wVersionRequested = MAKEWORD(2, 2);
	wsaerr = WSAStartup(wVersionRequested, &wsaData);
	// WSAStartup() return 0 on success and 1 on failure
	// WSAStartup() specifies required version of Windows Sockets and finds it
	if (wsaerr != 0) {
		cout << "The Winsock DLL not found!" << endl;
		return 0;
	}
	else {
		cout << "The Winsock DLL was found!" << endl;
		cout << "Status: " <<wsaData.szSystemStatus << endl;
	}

	cout << "\n\nCreating server socket.\n" << endl;

	// Creating the server socket
	serverSocket = INVALID_SOCKET;
	// socket() creates a socket
	// AF_INET is IPv4
	// SOCK_STREAM is a sequenced two-way byte stream
	// IPPROTO_TCP means it is using TCP protocol
	serverSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (serverSocket == INVALID_SOCKET) {
		cout << "Error at socket(): " << WSAGetLastError() << endl;
		WSACleanup();
		return 0;
	}
	else {
		cout << "Server socket created." << endl;
	}

	cout << "\n\nBinding server to IP and port 127.0.0.1:6103\n" << endl;

	sockaddr_in service;
	service.sin_family = AF_INET;
	// InetPton converts IPv4 to binary
	// AF_INET is IPv4
	// "127.0.0.1" is local host address
	// AF_INET is IPv4
	// last argument is a pointer to a buffer to store the binary IP
	InetPton(AF_INET, "127.0.0.1", &service.sin_addr.s_addr);
	service.sin_port = htons(port);
	if (bind(serverSocket, (SOCKADDR*)&service, sizeof(service)) == SOCKET_ERROR) {
		cout << "bind() failed: " << WSAGetLastError() << endl;
		closesocket(serverSocket);
		WSACleanup();
		return 0;
	}
	else {
		cout << "Binded successfully." << endl;
	}

	cout << "\n\nStart listening for clients.\n" << endl;

	// listen(socket, num_of_clients)
	// currently listening for one client
	if (listen(serverSocket, 1) == SOCKET_ERROR) {
		cout << "listen() failed: " << WSAGetLastError() << endl;
	}
	else {
		cout << "Listening... Waiting for a connection..." << endl;
	}

	// Accepting client
	acceptSocket = accept(serverSocket, NULL, NULL);
	if (acceptSocket == SOCKET_ERROR) {
		cout << "accept() failed: " << WSAGetLastError() << endl;
		WSACleanup();
		return -1;
	}
	
	cout << "\nAccepted Connection\n" << endl;

	cout << "\n\nWaiting to receive message from client.\n" << endl;

	// receive from client
	char buffer[200];
	// recv() takes socket, pointer to the buffer, size of buffer, and optional flags: default 0
	// returns the number of bytes sent
	while (true) {
		int byteCount = recv(acceptSocket, buffer, sizeof(buffer), 0);
		if (byteCount > 0) {
			cout << "Message received: " << buffer << "\n" << endl;
		}
		else {
			cout << "Message failed to send" << endl;
			WSACleanup();
			return 0;
		}
	}

	system("pause");
	WSACleanup();
}

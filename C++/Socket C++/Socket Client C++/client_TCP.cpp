#include <iostream>
#include <WinSock2.h>
#include <WS2tcpip.h>
using namespace std;


int main(int argc, char* argv[]) {
	SOCKET clientSocket;
	int port = 6103;

	cout << "\n\nLocating WinSock.\n" << endl;
	WSADATA wsaData;
	int wsaerr;
	WORD wVersionRequested = MAKEWORD(2, 2);
	wsaerr = WSAStartup(wVersionRequested, &wsaData);
	if (wsaerr != 0) {
		cout << "The Winsock DLL not found." << endl;
		return 0;
	}
	else {
		cout << "The Winsock DLL was found." << endl;
		cout << "Status: " << wsaData.szSystemStatus << endl;
	}

	cout << "\n\nCreating client socket.\n" << endl;
	// Create client socket
	clientSocket = INVALID_SOCKET;
	clientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (clientSocket == INVALID_SOCKET) {
		cout << "Error at socket(): " << WSAGetLastError() << endl;
		WSACleanup();
		return 0;
	}
	else {
		cout << "Socket has been created." << endl;
	}

	// Client socket binds automatically when connecting to server
	// so it is not needed to code that manually


	cout << "\n\nConnecting to server at 127.0.0.1:6103\n" << endl;

	sockaddr_in clientService;
	clientService.sin_family = AF_INET;
	InetPton(AF_INET, "127.0.0.1", &clientService.sin_addr.s_addr);
	clientService.sin_port = htons(port);
	if (connect(clientSocket, (SOCKADDR*)&clientService, sizeof(clientService)) == SOCKET_ERROR) {
		cout << "Failed to connect: " << WSAGetLastError() << endl;
		WSACleanup();
		return 0;
	}
	else {
		cout << "Connected..." << endl;
		cout << "Client can send and receive data" << endl;
	}

	cout << "\n\nPreparing to send message to server." << endl;

	// Send message to server
	char buffer[200];

	while (true) {
		cout << "\nEnter a message..." << endl;
		cin.getline(buffer, sizeof(buffer));

		// send takes a socket, a buffer to write data to, the length of the buffer, and optional flags
		int byteCount = send(clientSocket, buffer, sizeof(buffer), 0);
		if (byteCount > 0) {
			cout << "\nMessage sent: " << buffer << endl;
		}
		else {
			cout << "\nMessage failed to send" << endl;
			WSACleanup();
			return 0;
		}
	}	

	system("pause");
	WSACleanup();
	return 0;
}
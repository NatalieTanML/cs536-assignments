/*****************************************************************************
 *
 *     This file is part of Purdue CS 536.
 *
 *     Purdue CS 536 is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     Purdue CS 536 is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with Purdue CS 536. If not, see <https://www.gnu.org/licenses/>.
 *
 *****************************************************************************/

/*
 * server.c
 * Name:  Ming Li, Natalie Tan
 * PUID:  0035368455
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <errno.h>

#define QUEUE_LENGTH 10
#define RECV_BUFFER_SIZE 2048

/* TODO: server()
 * Open socket and wait for client to connect
 * Print received message to stdout
 * Return 0 on success, non-zero on failure
 */
int server(char *server_port)
{
  char buf[RECV_BUFFER_SIZE];
  int numbytes;
  int sockfd, connfd;
  struct addrinfo hints, *servinfo, *p;

  memset(&hints, 0, sizeof hints);
  hints.ai_family = AF_UNSPEC; 
  hints.ai_socktype = SOCK_STREAM; 
  hints.ai_flags = AI_PASSIVE; 

  if (getaddrinfo(NULL, server_port, &hints, &servinfo) != 0) 
  {
    fprintf(stderr, "server: getaddrinfo\n");
    return 1;
  }

  for (p = servinfo; p != NULL; p = p->ai_next) 
  {
    if ((sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1) 
    {
      continue;
    }

    if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1) 
    {
      close(sockfd);
      continue;
    }

      break;
  }

  if (p == NULL) 
  {
    fprintf(stderr, "server: bind failed\n");
    return 1;
  }

  freeaddrinfo(servinfo);

  if (listen(sockfd, RECV_BUFFER_SIZE) == -1) 
  {
    fprintf(stderr, "server: listen failed\n");
    return 1;
  }

  while (1) {
    struct sockaddr addr;
    socklen_t addrlen;

    connfd = accept(sockfd, &addr, &addrlen);
    if (connfd == -1)
    {
      continue;
    }

    numbytes = recv(connfd, buf, RECV_BUFFER_SIZE, 0);
    while (numbytes > 0) 
    {
      fwrite(buf, numbytes, 1, stdout);
      fflush(stdout);
      numbytes = recv(connfd, buf, RECV_BUFFER_SIZE, 0);
    }

    close(connfd);
  }

  return 0;
}

/*
 * main():
 * Parse command-line arguments and call server function
 */
int main(int argc, char **argv)
{
  char *server_port;

  if (argc != 2)
  {
    fprintf(stderr, "Usage: ./server-c (server port)\n");
    exit(EXIT_FAILURE);
  }

  server_port = argv[1];
  return server(server_port);
}

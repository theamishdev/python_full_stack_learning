import threading
import http.server
import socketserver

def start_server(port, server_ref):
    """Starts the server on the given port and stores the instance in server_ref."""
    Handler = http.server.SimpleHTTPRequestHandler
    # Allow faster restart
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        # Create the server
        with socketserver.TCPServer(("", port), Handler) as httpd:
            # Store the httpd instance in the list passed as argument so main() can access it
            server_ref[0] = httpd
            print(f"\n[Server] Serving HTTP on port {port}...")
            httpd.serve_forever()
    except OSError as e:
        print(f"\n[Error] Could not start server on port {port}: {e}")

def stop_server(server_ref):
    """Stops the server instance stored in server_ref."""
    if server_ref[0]:
        print("[Server] Stopping current server...")
        server_ref[0].shutdown()
        server_ref[0].server_close() 
        server_ref[0] = None

def change_port(new_port, server_ref):
    """Stops the current server and starts a new one on the new port."""
    stop_server(server_ref)
    
    # Start new server thread
    t = threading.Thread(target=start_server, args=(new_port, server_ref))
    t.daemon = True
    t.start()
    return t

def main():
    # Use a list as a mutable container to hold the server instance
    # This avoids using global variables
    current_server_ref = [None] 
    
    # Get initial port
    while True:
        try:
            port = int(input("Enter port number: "))
            change_port(port, current_server_ref)
            break
        except ValueError:
            print("Invalid input")

    print("Server running. Enter new port to switch, 'exit' to quit.")

    while True:
        user_input = input(">> ")
        
        if user_input.lower() == 'exit':
            stop_server(current_server_ref)
            break
            
        try:
            new_port = int(user_input)
            change_port(new_port, current_server_ref)
        except ValueError:
            print("Please enter a valid port number.")

if __name__ == "__main__":
    main()

from flask import jsonify, request
import time
import random

def init_api(app):
    """Initialize API routes for the Flask application."""
    
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'ok'})
    
    @app.route('/api/hello')
    def hello():
        try:
            print("Hello endpoint called")  # Debug log
            return jsonify({'message': 'Hello from Flask backend!'})
        except Exception as e:
            print(f"Error in hello endpoint: {str(e)}")  # Debug log
            return jsonify({'error': str(e)}), 500

    @app.route('/api/echo', methods=['POST'])
    def echo():
        try:
            print("Echo endpoint called")  # Debug log
            data = request.get_json()
            print(f"Received data: {data}")  # Debug log
            
            if not data:
                print("No data received in request")  # Debug log
                return jsonify({'error': 'No data received'}), 400
                
            message = data.get('message', '')
            if not message:
                print("No message in request data")  # Debug log
                return jsonify({'error': 'No message provided'}), 400
            
            # Simulate random delay between 0.5 and 2 seconds
            delay = random.uniform(0.5, 2)
            print(f"Simulating delay of {delay:.2f} seconds")  # Debug log
            time.sleep(delay)
            
            response = {
                'message': f'echo: {message}',
                'delay': round(delay, 2)
            }
            print(f"Sending response: {response}")  # Debug log
            return jsonify(response)
            
        except Exception as e:
            print(f"Error in echo endpoint: {str(e)}")  # Debug log
            return jsonify({'error': str(e)}), 500 
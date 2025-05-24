import time
import random
from typing import Dict, Union

def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {'status': 'ok'}

def hello() -> Union[Dict[str, str], Dict[str, str]]:
    """Hello endpoint."""
    try:
        return {'message': 'Hello from Python backend!'}
    except Exception as e:
        return {'error': str(e)}

def echo(message: str) -> Union[Dict[str, Union[str, float]], Dict[str, str]]:
    """Echo endpoint that simulates a delay."""
    try:
        if not message:
            return {'error': 'No message provided'}
        
        # Simulate random delay between 0.5 and 2 seconds
        delay = random.uniform(0.5, 2)
        time.sleep(delay)
        
        response = {
            'message': f'echo: {message}',
            'delay': round(delay, 2)
        }
        return response
        
    except Exception as e:
        print(f"Error in echo endpoint: {str(e)}")
        return {'error': str(e)} 
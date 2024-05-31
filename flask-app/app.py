from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    config_map_value = os.getenv('CONFIG_MAP_VALUE', 'Default ConfigMap Value')
    secret_value = os.getenv('SECRET_VALUE', 'Default Secret Value')
    env_value = os.getenv('ENV_VALUE', 'Default Env Value')

    return f"""
    <h1>Configuration Values</h1>
    <p><strong>ConfigMap Value:</strong> {config_map_value}</p>
    <p><strong>Secret Value:</strong> {secret_value}</p>
    <p><strong>Env Variable Value:</strong> {env_value}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


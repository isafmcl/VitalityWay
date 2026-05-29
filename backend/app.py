from flask import Flask, request, make_response
from flask_cors import CORS
from routes import register_routes


def create_app():
    app = Flask(__name__)
    # Global handler for OPTIONS preflight must be registered before Flask-CORS
    @app.before_request
    def handle_preflight():
        if request.method == 'OPTIONS':
            resp = make_response(('', 200))
            origin = request.headers.get('Origin', '*')
            resp.headers['Access-Control-Allow-Origin'] = origin
            resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
            return resp

    CORS(
        app,
        resources={
            r"/*": {
                "origins": "*",
                "allow_headers": ["Content-Type", "Authorization"],
                "allowed_headers": ["Content-Type", "Authorization"],
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            }
        },
        headers=["Content-Type", "Authorization"],
        supports_credentials=True,
    )
    app.config["CORS_HEADERS"] = "Content-Type,Authorization"
    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    port = int(__import__("os").environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)

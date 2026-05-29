def register_routes(app):
    from .auth import bp as auth_bp
    from .medico import bp as medico_bp
    from .consulta import bp as consulta_bp
    from .catalog import bp as catalog_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(medico_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(catalog_bp)

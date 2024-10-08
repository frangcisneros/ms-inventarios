class RouteMainApp:
    def init_app(self, app):
        from app.resources.stock_resource import stock_bp

        app.register_blueprint(stock_bp, url_prefix="/api/v1")

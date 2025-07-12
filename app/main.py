from fastapi import FastAPI
from nicegui import app, ui, run
import uvicorn
from pathlib import Path

from nicegui import app as nicegui_app
from app.config import Settings
from app.backend.api.billing import router as billing_router
from app.backend.api.sap import router as sap_router
from app.backend.api.masterdata import router as masterdata_router
from app.backend.api.health import router as health_router
from app.frontend.pages.home import home_page
from app.frontend.pages.billing_request import billing_request_page
from app.frontend.pages.order_search import order_search_page
from app.frontend.pages.about import about_page
from app.frontend.layouts.main_layout import setup_main_layout
from app.frontend.styles.sky_theme import apply_sky_theme

# Initialize settings
settings = Settings()

# Initialize FastAPI
fastapi_app = FastAPI(
    title="O2C Billing Portal",
    description="Order-to-Cash Billing Request Portal",
    version="1.0.0"
)

# Add API routes
fastapi_app.include_router(billing_router, prefix="/api/billing", tags=["billing"])
fastapi_app.include_router(sap_router, prefix="/api/sap", tags=["sap"])
fastapi_app.include_router(masterdata_router, prefix="/api/masterdata", tags=["masterdata"])
fastapi_app.include_router(health_router, prefix="/api/health", tags=["health"])

# Configure NiceGUI app
app.add_static_files('/static', Path(__file__).parent.parent / 'static')

# Apply global theme
apply_sky_theme()

# Setup routing
@ui.page('/')
def index():
    home_page()

@ui.page('/billing')
def billing():
    billing_request_page()

@ui.page('/search')
def search():
    order_search_page()

@ui.page('/about')
def about():
    about_page()

# Run the application
if __name__ in {"__main__", "__mp_main__"}:
    nicegui_app.mount("/api", fastapi_app)
    
    ui.run(
        title="O2C Billing Portal",
        port=8080,
        show=True,
        reload=True if settings.environment == "development" else False
    )
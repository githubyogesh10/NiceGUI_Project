from nicegui import ui

def apply_sky_theme():
    """Apply Sky branding theme to the application"""
    
    # Sky brand colors
    sky_colors = {
        'primary': '#0072c6',
        'secondary': '#00a1de',
        'success': '#28a745',
        'warning': '#ffc107',
        'danger': '#dc3545',
        'light': '#f8f9fa',
        'dark': '#343a40'
    }
    
    # Custom CSS for Sky branding
    ui.add_head_html('''
        <style>
            :root {
                --sky-primary: #0072c6;
                --sky-secondary: #00a1de;
                --sky-gradient: linear-gradient(to right, #ff8c00 5%, #f80032 25%, #ff00a0 45%, #8c28ff 65%, #0023ff 82%, #19a0ff 96%);
                --sky-blue-light: #eff6ff;
                --sky-blue-lighter: #dbeafe;
                --sky-success: #10b981;
                --sky-warning: #f59e0b;
                --sky-danger: #ef4444;
                --sky-text: #1f2937;
                --sky-text-light: #6b7280;
                --sky-border: #e5e7eb;
                --sky-background: #ffffff;
                --sky-background-light: #f9fafb;
            }

            /* Sky Header Gradient */
            .sky-header {
                background: var(--sky-gradient);
                color: white;
                padding: 1rem 1.5rem;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 1000;
                height: 80px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }

            /* Main content area */
            .main-content {
                margin-top: 90px;
                padding: 1.5rem;
                background: linear-gradient(to bottom right, #eff6ff, #e0e7ff);
                min-height: calc(100vh - 90px);
            }

            /* Sky buttons */
            .sky-button-primary {
                background: linear-gradient(to right, var(--sky-primary), var(--sky-secondary));
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 0.375rem;
                cursor: pointer;
                font-weight: 500;
                transition: opacity 0.2s;
            }

            .sky-button-primary:hover {
                opacity: 0.9;
            }

            .sky-button-success {
                background: linear-gradient(to right, #059669, #10b981);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 0.375rem;
                cursor: pointer;
                font-weight: 500;
                transition: opacity 0.2s;
            }

            .sky-button-success:hover {
                opacity: 0.9;
            }

            /* Sky cards */
            .sky-card {
                background: white;
                border-radius: 0.5rem;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                border: 1px solid var(--sky-border);
                overflow: hidden;
            }

            /* Form styling */
            .sky-form-group {
                margin-bottom: 1rem;
            }

            .sky-label {
                display: block;
                font-size: 0.875rem;
                font-weight: 500;
                color: var(--sky-text);
                margin-bottom: 0.5rem;
            }

            .sky-input {
                width: 100%;
                padding: 0.75rem;
                border: 1px solid var(--sky-border);
                border-radius: 0.375rem;
                font-size: 0.875rem;
                transition: border-color 0.2s, box-shadow 0.2s;
            }

            .sky-input:focus {
                outline: none;
                border-color: var(--sky-primary);
                box-shadow: 0 0 0 3px rgba(0, 114, 198, 0.1);
            }

            .sky-select {
                width: 100%;
                padding: 0.75rem;
                border: 1px solid var(--sky-border);
                border-radius: 0.375rem;
                font-size: 0.875rem;
                background: white;
                cursor: pointer;
                transition: border-color 0.2s, box-shadow 0.2s;
            }

            .sky-select:focus {
                outline: none;
                border-color: var(--sky-primary);
                box-shadow: 0 0 0 3px rgba(0, 114, 198, 0.1);
            }

            /* Navigation */
            .sky-nav-item {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 0.75rem 1rem;
                border-radius: 0.5rem;
                font-size: 0.875rem;
                font-weight: 500;
                transition: all 0.2s;
                text-decoration: none;
                color: var(--sky-text);
                border: none;
                background: transparent;
                cursor: pointer;
                width: 100%;
                text-align: left;
            }

            .sky-nav-item:hover {
                background-color: var(--sky-background-light);
            }

            .sky-nav-item.active {
                background: linear-gradient(to right, var(--sky-primary), var(--sky-secondary));
                color: white;
            }

            /* Progress steps */
            .sky-progress-step {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 2rem;
                height: 2rem;
                border-radius: 50%;
                font-size: 0.875rem;
                font-weight: 500;
            }

            .sky-progress-step.active {
                background: linear-gradient(to right, var(--sky-primary), var(--sky-secondary));
                color: white;
            }

            .sky-progress-step.inactive {
                background: var(--sky-border);
                color: var(--sky-text-light);
            }

            /* Table styling */
            .sky-table {
                width: 100%;
                border-collapse: collapse;
                background: white;
            }

            .sky-table th {
                padding: 0.75rem;
                text-align: left;
                font-weight: 600;
                color: var(--sky-text);
                background: var(--sky-background-light);
                border: 1px solid var(--sky-border);
            }

            .sky-table td {
                padding: 0.75rem;
                border: 1px solid var(--sky-border);
                color: var(--sky-text);
            }

            .sky-table tr:nth-child(even) {
                background: var(--sky-background-light);
            }

            /* Status badges */
            .sky-badge {
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.75rem;
                font-weight: 500;
            }

            .sky-badge-success {
                background: #10b981;
                color: white;
            }

            .sky-badge-warning {
                background: #f59e0b;
                color: white;
            }

            .sky-badge-info {
                background: var(--sky-primary);
                color: white;
            }

            /* Responsive design */
            @media (max-width: 768px) {
                .sky-header {
                    padding: 0.75rem 1rem;
                    height: 70px;
                }

                .main-content {
                    margin-top: 80px;
                    padding: 1rem;
                }

                .sky-button-primary,
                .sky-button-success {
                    padding: 0.625rem 1.25rem;
                    font-size: 0.875rem;
                }
            }

            /* Error styling */
            .sky-error {
                color: var(--sky-danger);
                font-size: 0.75rem;
                margin-top: 0.25rem;
            }

            .sky-input.error {
                border-color: var(--sky-danger);
            }

            /* Success/warning messages */
            .sky-alert {
                padding: 1rem;
                border-radius: 0.375rem;
                margin-bottom: 1rem;
            }

            .sky-alert-success {
                background: #ecfdf5;
                border: 1px solid #10b981;
                color: #065f46;
            }

            .sky-alert-warning {
                background: #fef3c7;
                border: 1px solid #f59e0b;
                color: #92400e;
            }

            .sky-alert-error {
                background: #fef2f2;
                border: 1px solid #ef4444;
                color: #991b1b;
            }

            /* Loading spinner */
            .sky-spinner {
                width: 20px;
                height: 20px;
                border: 2px solid transparent;
                border-top: 2px solid currentColor;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    ''')

    # Set default theme
    ui.colors(
        primary=sky_colors['primary'],
        secondary=sky_colors['secondary'],
        positive=sky_colors['success'],
        negative=sky_colors['danger'],
        warning=sky_colors['warning']
    )
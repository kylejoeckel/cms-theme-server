# theme_config.py

default_theme = {
    "palette": {
        "mode": "light",
        "primary": {
            "main": "#1976d2",
            "light": "#42a5f5",
            "dark": "#1565c0",
            "contrastText": "#fff"
        },
        "secondary": {
            "main": "#dc004e",
            "light": "#ff5983",
            "dark": "#9a0036",
            "contrastText": "#000"
        },
        "error": {
            "main": "#f44336",
            "light": "#e57373",
            "dark": "#d32f2f",
            "contrastText": "#fff"
        },
        "warning": {
            "main": "#ff9800",
            "light": "#ffb74d",
            "dark": "#f57c00",
            "contrastText": "rgba(0, 0, 0, 0.87)"
        },
        "info": {
            "main": "#2196f3",
            "light": "#64b5f6",
            "dark": "#1976d2",
            "contrastText": "#fff"
        },
        "success": {
            "main": "#4caf50",
            "light": "#81c784",
            "dark": "#388e3c",
            "contrastText": "rgba(0, 0, 0, 0.87)"
        },
        "background": {
            "default": "#fafafa",
            "paper": "#fff"
        },
        "text": {
            "primary": "#212121",
            "secondary": "#757575",
            "disabled": "#bdbdbd",
            "hint": "#9e9e9e"
        }
    },
    "typography": {
        "fontFamily": "\"Roboto\", \"Helvetica\", \"Arial\", sans-serif",
        "fontSize": 14,
        "fontWeightLight": 300,
        "fontWeightRegular": 400,
        "fontWeightMedium": 500,
        "button": {
            "textTransform": "none"
        }
    },
    "breakpoints": {
        "values": {
            "xs": 0,
            "sm": 600,
            "md": 960,
            "lg": 1280,
            "xl": 1920
        }
    },
    "shape": {
        "borderRadius": 8
    },
    "components": {
        "MuiButton": {
            "styleOverrides": {
                "root": {
                    "fontSize": "1rem"
                }
            },
            "defaultProps": {
                "disableRipple": true
            }
        }
    }
}

from cx_Freeze import setup, Executable


setup(
    name="MyApp",
    version="0.1",
    description="My Flask web application",
    executables=[Executable("app.py", base="Console")],
    options={
        'build_exe': {
            'include_files': [('templates', 'templates')],
            'packages': [
                'flask', 
                'blinker',
                'click',
                'itsdangerous', 
                'jinja2', 
                'markupsafe',
                'werkzeug'
            ],
        }
    }
)

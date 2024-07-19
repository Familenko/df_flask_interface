from cx_Freeze import setup, Executable
# python setup.py build


setup(
    name="MyApp",
    version="0.1",
    description="My Flask web application",
    executables=[Executable("app.py", base="Console")],
    options={
        'build_exe': {
            'include_files': [
                ('static', 'static'),
                ('templates', 'templates')
                ],
            'packages': [
                'flask', 
                'blinker',
                'click',
                'itsdangerous', 
                'jinja2', 
                'markupsafe',
                'werkzeug',
                'pandas',
            ],
        }
    }
)

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #rerun our code everytime we make a change
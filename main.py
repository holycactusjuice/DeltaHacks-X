from website import create_app

app = create_app()

app.secret_key = "DeltaHacks10"

if __name__ == '__main__':
    app.run(debug=True) #rerun our code everytime we make a change
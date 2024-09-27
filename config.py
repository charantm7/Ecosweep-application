from app import create_app

mod= create_app


if __name__ == '__main__':
    mod.run(debug=True)
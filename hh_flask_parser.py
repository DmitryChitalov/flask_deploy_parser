from flask_parser import create_app
import multiprocessing as ml
from flask_parser.parser_app import main as pr
app = create_app()

if __name__ == '__main__':

    par_service = ml.Process(name="HH Parser", target=pr.main)
    par_service.start()

    app.run(debug=True)

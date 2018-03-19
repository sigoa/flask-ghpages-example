import                     os
from   FlaskProject import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    main.app.run(host='0.0.0.0', port=port)   # for running locally, but on github pages, port# 5000 does not apply

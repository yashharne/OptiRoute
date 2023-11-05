from flask import (
    Blueprint, request, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import pandas as pd

bp = Blueprint('route', __name__ , url_prefix='/route')



@bp.route('/', methods=(['GET', 'POST']))
@login_required
def create():
    # if request.method == 'POST':
        db = get_db()
        data = request.get_json()
        items = data.get('items', [])
        filter_string = '(' + ','.join(['"' + item + '"' for item in items]) + ')'

        res = db.table('items').select("item_id , shop_id ,name , price , quantity  , shops(id , Name , latitude , longitude)").filter('name' , 'in' , filter_string).execute()
        
        df = pd.DataFrame(res.data)

        # Print the DataFrame
        print(df)
        return jsonify(res.data)
    

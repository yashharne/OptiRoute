from flask import (
    Blueprint, request, jsonify
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import pandas as pd
import os
from . import tsp_Optimised

bp = Blueprint('route', __name__ , url_prefix='/route')


@bp.route('/', methods=(['GET', 'POST']))
@login_required
def create():
    # if request.method == 'POST':
        db = get_db()
        data = request.get_json()
        items = data.get('items', [])
        filter_string = '(' + ','.join(['"' + item + '"' for item in items]) + ')'
        start_lat = data.get('start_lat')
        start_lon = data.get('start_lon')

        res = db.table('items').select("item_id , shop_id ,name , price , quantity  , shops(id , Name , latitude , longitude)").filter('name' , 'in' , filter_string).execute()
        
        df = pd.DataFrame(res.data)
        output_folder = "flaskr/data"
        output_file = "data.csv"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        file_path = os.path.join(output_folder, output_file)
        df.to_csv(file_path, index=False)
        
        routes = tsp_Optimised.find_path_points(float(start_lat), float(start_lon))
        print(routes)
        return jsonify(routes)
    